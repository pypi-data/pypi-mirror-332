# MetaidigitSTT

MetaidigitSTT is a lightweight Speech-to-Text (STT) recognition module utilizing Groq's Whisper model for high-accuracy transcription. It enables real-time audio recording and transcription using Python.

## Features
- Records audio via microphone and saves it as an MP3 file.
- Uses Groq's Whisper-Large-V3 model for transcription.
- Simple and easy-to-use API.

## Installation

Ensure you have Python 3.10 or higher installed.

### Using Pip
```sh
pip install -r requirements.txt
```

### Required Dependencies
- `ffmpeg`
- `SpeechRecognition`
- `pyaudio`
- `pydub`
- `groq`
- `python-dotenv`

You may need to install `ffmpeg` manually:
```sh
# Ubuntu/Linux
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

## Usage

### 1. Recording Audio

The `record_audio` function records audio from the microphone and saves it as an MP3 file.

```python
from metaidigitstt import record_audio

record_audio("audio/test.mp3", timeout=20, phrase_time_limit=10)
```

### 2. Transcribing Audio

The `transcribe_with_groq` function transcribes recorded audio using Groq's Whisper model.

```python
from metaidigitstt import transcribe_with_groq

GROQ_API_KEY = "your_api_key_here"
stt_model = "whisper-large-v3"
audio_filepath = "audio/test.mp3"

transcription = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
print(transcription)
```

## Environment Variables
Set up your API key in a `.env` file:
```sh
GROQ_API_KEY=your_api_key_here
```

## Setup for Development

### Install Locally
```sh
pip install .
```

### Running Tests
Ensure dependencies are installed and run:
```sh
pytest tests/
```

## Packaging & Deployment

To package the module:
```sh
python setup.py sdist bdist_wheel
```

To install the package locally:
```sh
pip install .
```

## License
This project is licensed under the MIT License.

## Author
[Suhal Samad](mailto:samadsuhal@gmail.com)

