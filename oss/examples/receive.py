"""Ring webhook receiver, plus the hand-landmark gate.

No network, using the sample key printed below:

    python3 examples/receive.py

Listen for signed POSTs. The key comes from the environment, never from this file:

    SIGNING_KEY=your-hmac-key python3 examples/receive.py --serve
"""

import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from signsync_oss import Seen, hand_event, handle, parse_event, should_translate, sign

EXAMPLE_KEY = "example-hmac-key"
MAX_BODY = 1_000_000


def sample_motion():
    body = {
        "meta": {
            "version": "1.1",
            "time": "2026-02-13T13:39:57Z",
            "request_id": "req-demo",
            "account_id": "acct_example",
        },
        "data": {
            "id": "dev_example_motion_1",
            "type": "motion_detected",
            "attributes": {
                "source": "dev_example",
                "source_type": "devices",
                "timestamp": 1786715596787,
                "sub_type": "human",
                "component_ids": ["0"],
            },
        },
    }
    return json.dumps(body, separators=(",", ":")).encode()


def demo():
    raw = sample_motion()
    signature = sign(EXAMPLE_KEY, raw)
    seen = Seen()
    status, body = handle(raw, signature, EXAMPLE_KEY, seen)
    event = parse_event(json.loads(raw))
    # Two frames of one hand. The second frame drops, so the gate opens.
    hands = hand_event([[[(0.42, 0.40), (0.55, 0.48)]], [[(0.42, 0.62), (0.55, 0.70)]]])
    translate = should_translate(event, hands)
    if status != 200 or body["status"] != "ok" or not translate:
        raise SystemExit("demo failed")
    duplicate, _ = handle(raw, signature, EXAMPLE_KEY, seen)
    if duplicate != 200:
        raise SystemExit("duplicate demo failed")
    print("webhook", body["type"], body["device_id"], "request", body["request_id"])
    print(
        "hands",
        hands.hands,
        "moving",
        hands.moving,
        "bbox",
        tuple(round(v, 2) for v in hands.bbox),
    )
    print("translate", translate)
    print("second delivery is a duplicate and stays HTTP", duplicate)


def serve():
    key = os.environ.get("SIGNING_KEY")
    if not key:
        raise SystemExit("Set SIGNING_KEY to the Ring HMAC Signature Key.")
    port = int(os.environ.get("PORT", "8080"))
    seen = Seen()

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                length = -1
            if length < 0 or length > MAX_BODY:
                self._send(413, {"error": "body too large"})
                return
            raw = self.rfile.read(length)
            status, body = handle(raw, self.headers.get("X-Signature", ""), key, seen)
            self._send(status, body)

        def _send(self, status, body):
            data = json.dumps(body).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, fmt, *args):
            print(fmt % args)

    HTTPServer.allow_reuse_address = True
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"listening on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    if "--serve" in sys.argv:
        serve()
    else:
        demo()
