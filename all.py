import os
import glob
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get all the .mp3 files
audio_files = glob.glob("**/*.mp3", recursive=True)

# Transcribe each audio file
for audio_file in audio_files:
    with open(audio_file, "rb") as file:
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=file,
            language="de"
        )
        transcription = response.transcription

        # Save the transcription to a .txt file
        transcript_file = audio_file.rsplit('.', 1)[0] + '.txt'
        with open(transcript_file, "w") as out_file:
            out_file.write(transcription)

        print(f"Transcription for {audio_file} saved successfully!")
