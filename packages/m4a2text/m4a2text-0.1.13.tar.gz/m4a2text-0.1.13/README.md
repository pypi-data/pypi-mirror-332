# m4a2text

Convert M4A audio files to WAV and transcribe speech to text using Azure Speech API.

## Installation

```bash
pip install m4a2text
```

## Usage
```python
from m4a2text import M4A2Text

m4a2text = M4A2Text(
    subscription_key='your_subscription_key',
    region='your_region'
)

m4a2text.convert_and_transcribe(
    m4a_file='example.m4a',
    make_output_file=True
)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

