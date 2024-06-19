import gradio as gr
import whisper

# Load the Whisper model
model = whisper.load_model("base")

def transcribe(audio_filepath):
    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_filepath)
    audio = whisper.pad_or_trim(audio)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # Return the recognized text
    return result.text

gr.Interface(
    title='Real-time AI-based Audio Transcription, Recognition and Translation Web App', 
    fn=transcribe, 
    inputs=gr.Audio(type="filepath"), 
    outputs=gr.Textbox(),
    live=True
).launch()
