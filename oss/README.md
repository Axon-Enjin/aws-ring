# signsync-oss

Built for the AWS AppDev 2026 hackathon.

A small Python library for two jobs any Ring doorbell app can reuse. It checks that a webhook really came from Ring, and it turns hand landmarks into a yes-or-no: are there hands at the door, and did they move? SignSync uses that as the gate in front of sign-language translation. The library does not know what was signed.

This folder is meant to be published on its own.

## What it does

Ring signs every webhook with your app's HMAC Signature Key. The signature is HMAC-SHA256 of the raw request body, hex-encoded, in the `X-Signature` header as `sha256=<hex>`. `verify_signature` checks that digest in constant time. `handle` then parses a webhook v1.1 payload and remembers `meta.request_id`, so a retry does not run twice.

`hand_event` takes hand landmarks only. A frame is a list of hands, and a hand is a list of `(x, y)` points (or objects with `.x` and `.y`, the shape MediaPipe uses). It returns how many hands are in the last frame, whether they moved, and a bounding box. `should_translate` is true for a doorbell press or a motion event when those hands are moving. A `vehicle` motion event stays closed.

## Why

Doorbell video is sensitive, and a signature check is easy to get wrong: hashing a re-serialized JSON body never matches, and a duplicate delivery will double-fire whatever you do next. This library keeps both of those in one place, and it keeps faces out. You pass points you already extracted. Images, video, and face landmarks are not inputs.

It does not call Ring, download clips, or recognize signs. Landmark extraction and translation stay in your app. Webhook details are documented by Ring at <https://developer.amazon.com/docs/ring/api-documentation.html>.

## How to use

```python
from signsync_oss import Seen, hand_event, handle, parse_event, should_translate
import json

seen = Seen()
status, body = handle(raw_body, signature_header, signing_key, seen)
if status == 200 and body["status"] == "ok":
    event = parse_event(json.loads(raw_body))
    hands = hand_event([previous_frame, latest_frame])
    if should_translate(event, hands):
        ...  # your translator, not this library
```

`raw_body` is the request bytes before you parse JSON. `signing_key` is the HMAC Signature Key from the Ring developer portal. Keep it on the server.

Movement is the mean shift of landmarks between the last two frames. A hand that appears counts as movement. One frame is never enough to call it moving. The default threshold is `0.02` (2% of the frame). Pass `move` if the camera is far from the person.

`handle` does no network work, so it returns inside Ring's five-second webhook window. Do the slow work after you have answered.

## Example

Offline demo, with a fake key that is not a credential:

```bash
python3 examples/receive.py
```

Local receiver. Supply your own key. Nothing in this repo is a live secret:

```bash
SIGNING_KEY=your-hmac-key python3 examples/receive.py --serve
```

That listens on `http://127.0.0.1:8080` (override with `PORT`). POST the raw body and send `X-Signature`.

## Tests

From this directory, on Python 3.9+:

```bash
python3 -m unittest discover -s tests -t . -v
```

No third-party packages.

## License

MIT, Copyright (c) 2026 Axon Enjin. See [LICENSE](LICENSE).
