# D-ID Python API Wrapper

This Python library allows you to interact with the D-ID API easily. You can use it to create text-to-video clips and retrieve clip information, among other things.

## Installation

You can install the `did-api` module using `pip`:

```bash
pip install did-api
```

## Getting Started

1. Obtain your D-ID API Key from [D-ID Studio](https://studio.d-id.com/account-settings).

2. Import the library and initialize it with your API Key:

```python
from D_ID import Clips

api_key = "your_api_key_here"
d_id = Clips(api_key)
```

## Creating a Text-to-Video Clip

To create a text-to-video clip, use the `create_text_to_video_clip` method:

```python
text = "Your text here"
result = d_id.create_text_to_video_clip(text)
```

This function takes the following optional parameters:
- `presenter_id` (default: 'amy-jcwCkr1grs')
- `driver_id` (default: 'uM00QMwJ9x')
- `voice_provider_name` (default: 'microsoft')
- `voice_id` (default: 'en-US-JennyNeural')
- `WEBHOOK_URL` (default: None)
- `background_color` (default: '#ffffff')
- `extra_data` (default: {})

The `result` variable will contain the API response, including information about the created clip.

## Retrieving Clip Information

You can retrieve clip information using the `get_clip_by_id` method:

```python
clip_id = "your_clip_id_here"
clip_info = d_id.get_clip_by_id(clip_id)
```

The `clip_info` variable will contain the API response, providing details about the specified clip.

## Examples

Here are some examples of how to use this library:

```python
# Create a text-to-video clip
text = "Hello, D-ID!"
result = d_id.create_text_to_video_clip(text) 
"result => {'id': 'clip_id', 'created_at': '2023-09-06T21:45:50.298Z', 'object': 'clip', 'status': 'created'}"

# Get information about a specific clip
clip_id = "your_clip_id_here"
clip_info = d_id.get_clip_by_id(clip_id)
```

## License

This library is provided under the [MIT License](LICENSE).

For more information about the D-ID API, please refer to the [official documentation](https://docs.d-id.com/).