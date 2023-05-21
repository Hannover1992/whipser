import whisper

model = whisper.load_model("base")

name_of_file = "00_Organisatorisches/Audiokommentar_Organisatorisches.mp3"

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio(name_of_file)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)

# define the filename
transcript_file = name_of_file + ".txt"

# open the file with write permissions
with open(transcript_file, "w") as out_file:
    # write the transcription to the file
    out_file.write(result.text)
