import json
import unittest

from signsync_oss import (
    Seen,
    hand_event,
    handle,
    parse_event,
    should_translate,
    sign,
    verify_signature,
)

KEY = "example-hmac-key"


def motion_body(request_id="req-1", event_type="motion_detected", sub_type="human"):
    attributes = {
        "source": "dev_example",
        "source_type": "devices",
        "timestamp": 1786715596787,
        "component_ids": ["0"],
    }
    if sub_type is not None:
        attributes["sub_type"] = sub_type
    body = {
        "meta": {
            "version": "1.1",
            "time": "2026-02-13T13:39:57Z",
            "request_id": request_id,
            "account_id": "acct_example",
        },
        "data": {
            "id": "dev_example_motion_1",
            "type": event_type,
            "attributes": attributes,
        },
    }
    return json.dumps(body, separators=(",", ":")).encode()


class Point:
    def __init__(self, x, y, z=0.0):
        self.x = x
        self.y = y
        self.z = z


class VerifyTests(unittest.TestCase):
    def test_round_trip(self):
        raw = motion_body()
        signature = sign(KEY, raw)
        self.assertTrue(signature.startswith("sha256="))
        self.assertTrue(verify_signature(KEY, raw, signature))
        self.assertTrue(verify_signature(KEY, raw, signature.removeprefix("sha256=")))

    def test_rejects_tampered_body_and_wrong_key(self):
        raw = motion_body()
        signature = sign(KEY, raw)
        self.assertFalse(verify_signature(KEY, raw + b" ", signature))
        self.assertFalse(verify_signature("other-key", raw, signature))

    def test_rejects_reserialized_json(self):
        raw = b'{"z":1,"a":2}'
        signature = sign(KEY, raw)
        pretty = json.dumps(json.loads(raw)).encode()
        self.assertNotEqual(raw, pretty)
        self.assertFalse(verify_signature(KEY, pretty, signature))

    def test_rejects_bad_header(self):
        raw = b"{}"
        self.assertFalse(verify_signature(KEY, raw, ""))
        self.assertFalse(verify_signature(KEY, raw, "sha256=abcd"))
        self.assertFalse(verify_signature(KEY, raw, None))

    def test_refuses_str_body(self):
        with self.assertRaises(TypeError):
            verify_signature(KEY, "{}", "sha256=00")


class ParseTests(unittest.TestCase):
    def test_motion_fields(self):
        event = parse_event(json.loads(motion_body()))
        self.assertEqual(event.request_id, "req-1")
        self.assertEqual(event.account_id, "acct_example")
        self.assertEqual(event.event_type, "motion_detected")
        self.assertEqual(event.device_id, "dev_example")
        self.assertEqual(event.timestamp_ms, 1786715596787)
        self.assertEqual(event.sub_type, "human")
        self.assertEqual(event.component_ids, ("0",))

    def test_button_press_without_subtype(self):
        event = parse_event(json.loads(motion_body(event_type="button_press", sub_type=None)))
        self.assertEqual(event.event_type, "button_press")
        self.assertIsNone(event.sub_type)

    def test_bad_shape(self):
        with self.assertRaises(ValueError):
            parse_event({"hello": "world"})

    def test_seen_forgets_oldest(self):
        seen = Seen(2)
        self.assertTrue(seen.first("a"))
        self.assertTrue(seen.first("b"))
        self.assertFalse(seen.first("b"))
        self.assertTrue(seen.first("c"))
        self.assertTrue(seen.first("a"))


class HandleTests(unittest.TestCase):
    def test_ok_then_duplicate(self):
        raw = motion_body()
        seen = Seen()
        status, body = handle(raw, sign(KEY, raw), KEY, seen)
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["type"], "motion_detected")
        self.assertEqual(body["device_id"], "dev_example")
        again, dup = handle(raw, sign(KEY, raw), KEY, seen)
        self.assertEqual(again, 200)
        self.assertEqual(dup, {"status": "duplicate", "request_id": "req-1"})

    def test_bad_signature_is_not_parsed(self):
        status, body = handle(b"not-json", "sha256=nope", KEY, Seen())
        self.assertEqual(status, 401)
        self.assertEqual(body["error"], "invalid signature")

    def test_valid_signature_bad_payload(self):
        raw = b"[]"
        status, body = handle(raw, sign(KEY, raw), KEY, Seen())
        self.assertEqual(status, 400)
        self.assertEqual(body["error"], "bad payload")


class HandTests(unittest.TestCase):
    def test_still_hand_is_not_signing(self):
        frame = [[(0.40, 0.40), (0.50, 0.50)]]
        event = hand_event([frame, frame])
        self.assertEqual(event.hands, 1)
        self.assertFalse(event.moving)
        self.assertFalse(event.signing)
        self.assertEqual(event.bbox, (0.40, 0.40, 0.50, 0.50))

    def test_movement_and_attribute_points(self):
        start = [[Point(0.40, 0.40), Point(0.50, 0.50)]]
        shifted = [[Point(0.40, 0.40), Point(0.50, 0.70, 0.1)]]
        event = hand_event([start, shifted])
        self.assertTrue(event.moving)
        self.assertTrue(event.signing)
        self.assertEqual(event.bbox[3], 0.70)

    def test_hand_entering_counts_as_movement(self):
        event = hand_event([[], [[(0.2, 0.3)]]])
        self.assertEqual(event.hands, 1)
        self.assertTrue(event.signing)

    def test_empty(self):
        self.assertEqual(hand_event([]), hand_event([]).__class__(0, False, None))
        self.assertFalse(hand_event([[[]]]).signing)

    def test_rejects_faces_and_nan(self):
        with self.assertRaises(ValueError):
            hand_event([{"faces": [[0.1, 0.2]]}])
        with self.assertRaises(ValueError):
            hand_event([[[float("nan"), 0.2]]])

    def test_translate_gate(self):
        moving = hand_event([[[(0.2, 0.2)]], [[(0.2, 0.5)]]])
        still = hand_event([[[(0.2, 0.2)]], [[(0.2, 0.2)]]])
        human = parse_event(json.loads(motion_body()))
        vehicle = parse_event(json.loads(motion_body(sub_type="vehicle")))
        press = parse_event(json.loads(motion_body(event_type="button_press", sub_type=None)))
        added = parse_event(json.loads(motion_body(event_type="device_added", sub_type=None)))
        self.assertTrue(should_translate(human, moving))
        self.assertTrue(should_translate(press, moving))
        self.assertFalse(should_translate(human, still))
        self.assertFalse(should_translate(vehicle, moving))
        self.assertFalse(should_translate(added, moving))


if __name__ == "__main__":
    unittest.main()
