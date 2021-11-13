import os
import pandas as pd #  pip install numpy==1.19.3
import playsound
from google.cloud import texttospeech # outdated or incomplete comparing to v1
from google.cloud import texttospeech_v1

# Instantiates a client

def SpeechSyntesizer(audio, path="main/data/speech/empyrean-app-332014-6fdfdc87b1df.json"):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path
    client = texttospeech_v1.TextToSpeechClient()

    voice_list = []
    for voice in client.list_voices().voices:
        voice_list.append([voice.name, voice.language_codes[0], voice.ssml_gender, voice.natural_sample_rate_hertz])
    df_voice_list = pd.DataFrame(voice_list, columns=['name', 'language code', 'ssml gender', 'hertz rate']).to_csv(
        'Voice List.csv', index=False)

    # Set the text input to be synthesized
    quote = audio
    synthesis_input = texttospeech_v1.SynthesisInput(text=quote)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-in", ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    voice = texttospeech_v1.VoiceSelectionParams(
        name='ar-XA-Wavenet-B', language_code="en-GB"
        # name='vi-VN-Wavenet-D', language_code="vi-VN"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech_v1.AudioConfig(
        # https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1#audioencoding
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("./output2.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
        playsound.playsound('output2.mp3')
        os.remove("output2.mp3")


