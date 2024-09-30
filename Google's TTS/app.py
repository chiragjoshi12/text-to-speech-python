import os
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys.json' ## Add your `.json` file from Googlr Cloud

client = texttospeech.TextToSpeechClient()

text_block = '''Once upon a time, in a big green forest, there lived a little squirrel named Sam. Sam was very friendly and loved to share his food with other animals. One day, he found a big acorn and decided to share it with his friends.
'''

synthesis_input = texttospeech.SynthesisInput(text=text_block)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ## You can change Language here.
    name='en-US-Studio-O'
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    effects_profile_id=['small-bluetooth-speaker-class-device'],
    speaking_rate=1,
    pitch=1
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

with open("output.mp3", "wb") as output:
    output.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")
    