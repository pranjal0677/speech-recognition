# speech-recognition

Save the above script as app.py.

## Install Dependencies:

Ensure you have gradio, whisper, and ffmpeg installed:

pip install gradio whisper
sudo apt install ffmpeg


## Run the Script:

python3 app.py


## Explanation of the Code:

Model Loading: The Whisper model is loaded using whisper.load_model("base").
Transcription Function: The transcribe function handles loading the audio, processing it, detecting the language, decoding the audio, and returning the transcribed text.
Gradio Interface: The Gradio interface is set up with a title, the transcription function, an audio input component, and a textbox output component. The live=True parameter allows for real-time processing.
This script sets up a web interface where users can upload an audio file, and the application will display the transcribed text. The print statement within the transcribe function helps with debugging by outputting the detected language to the console.
