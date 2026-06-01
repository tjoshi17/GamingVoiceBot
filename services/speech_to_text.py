import os
import whisper

os.environ["PATH"] = "/opt/homebrew/bin:" + os.environ["PATH"]

def load_whisper():

    return whisper.load_model(
        "base"
    )

model = load_whisper()

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]