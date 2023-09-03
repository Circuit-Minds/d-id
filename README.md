# D_ID Python Package

The `D_ID` Python package is designed to interact with the D-ID API, allowing you to access various functionalities such as retrieving actor lists, creating text-to-video clips, and more.

## Installation

You can install the package via pip:

```bash
pip install d-id
```

## Getting Started

1. Import the `Clips` class from the `D_ID` package:

    ```python
    from D_ID.D_ID import Clips
    ```

2. Initialize the `Clips` class with your D-ID API key:

    ```python
    api_key = "<your_api_key>"
    clip = Clips(api_key)
    ```

## Usage Examples

### Get Actor List

```python
actor_list = clip.get_actor_list()
print(actor_list)
```

This function retrieves a list of actors available in the D-ID API.

### Create Text-to-Video Clip

```python
text = "This is the text you want to convert into a video clip."
presenter_id = "amy-jcwCkr1grs"
driver_id = "uM00QMwJ9x"
microsoft_voice_id = "en-US-JennyNeural"

result = clip.create_text_to_video_clip(text, presenter_id, driver_id, microsoft_voice_id)
print(result)
```

This function creates a video clip from the provided text using the specified presenter, driver, and Microsoft voice.

### Additional Functions

You can also use other functions provided by the `Clips` class to interact with the D-ID API, such as retrieving driver lists, presenter details, clips, and more.

[comment]: <> ## Documentation

[comment]: <> For detailed documentation on each function and its parameters, please refer to the inline comments in the `Clips` class definition within the package code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Support

If you encounter any issues or have questions about using this package, please [open an issue](https://github.com/Circuit-Minds/d-id/issues) on the GitHub repository.
