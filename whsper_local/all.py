import os
import glob
import torch
from transformers import pipeline
import soundfile as sf

# Function for speech recognition
def transcribe_audio(pipe, audio_path):
    audio_input, sample_rate = sf.read(audio_path)
    if audio_input.ndim > 1:
        audio_input = audio_input.mean(axis=1)

    chunk_length_s = 30
    chunk_length_samples = chunk_length_s * sample_rate

    gesamter_text = ""
    for start in range(0, len(audio_input), chunk_length_samples):
        end = start + chunk_length_samples
        chunk = audio_input[start:end]
        whisper_input = {"raw": chunk, "sampling_rate": sample_rate}
        prediction = pipe(whisper_input, batch_size=1, return_timestamps=True)["chunks"]
        for chunk in prediction:
            gesamter_text += chunk['text'] + " "
    return gesamter_text

# Main function
def main():
    # device = "cuda:0" if torch.cuda.is_available() else "cpu"
    device = "cpu"

    pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=device)

    # Get all the .mp3 files
    audio_files = glob.glob("**/*.mp3", recursive=True)

    # Transcribe each audio file
    for audio_file in audio_files:
        transcribed_text = transcribe_audio(pipe, audio_file)

        # Save the transcription to a .txt file
        transcript_file = audio_file.rsplit('.', 1)[0] + '.txt'
        with open(transcript_file, "w") as out_file:
            out_file.write(transcribed_text)

        print(f"Transcription for {audio_file} saved successfully!")

if __name__ == "__main__":
    main()
