# dtmf_py

This module allows you to get a list of tone dialing RTP packets.

## Installation:
poetry
```commandline
poetry add dtmf-py
```
pip
```commandline
pip install dtmf-py
```

## Usage:

```python
from dtmf_py import DTMF
from rtp import PayloadType


payload: list[bytes] = DTMF.make_numbers_packets(
    numbers='123*',
    payload_type=PayloadType.DYNAMIC_101,
    tone_packets_count=10
)
```
This code returns a list of tone dialing RTP packets for the transmitted number. 
<br/>What to do with them next is up to you.
