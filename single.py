import os
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the path of the first audio file
audio_file = "00_Organisatorisches/Audiokommentar_Organisatorisches.mp3"

# Transcribe the audio file
with open(audio_file, "rb") as file:
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=file,
        language="de"
    )
    transcription = response.transcription
    print(transcription)

    # Save the transcription to a .txt file
    transcript_file = audio_file.rsplit('.', 1)[0] + '.txt'
    with open(transcript_file, "w") as out_file:
        out_file.write(transcription)

    print(f"Transcription for {audio_file} saved successfully!")
