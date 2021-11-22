import COVID19Py
import os
import pandas as pd  # pip install numpy==1.19.3
import playsound
from google.cloud import texttospeech  # outdated or incomplete comparing to v1
from google.cloud import texttospeech_v1
import random

# Instantiates a client


def SpeechSynthesizer(audio):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = """
    {
  "type": "service_account",
  "project_id": "empyrean-app-332014",
  "private_key_id": "6fdfdc87b1dfc464e3d435c1ff670ae428959e27",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDsPmQTlLhB1cOA\nb1gr350bFyS++XeTqP/kQz9DRlE3sWIMQwn7iaDwtdDgNQz0CaJzbLM3pc5R3kF4\ngrwmIXPsDPpB8TFfODdyjF+jqcwnDdhentVv1GKGHwzI8Cu69Ty0UNjUokI3APxt\n0uMIyq1ebuGLve0OXclEc+AKcaXrK1dTWFChpcL3IbeI4BYBup+C9DYNQckMKfVI\n3ulCvRGLhOE449UbNGiY0XK4hOmUjWIzdJ2KvtBJH+2fOn7QxnF9ChuxhWyMYVwr\n9/KcNiyLODCbUPSiZ0T3Jylj+k0jHcyirlUsqKHUYbxvnFwgceCBXuxIgwojxnzC\nxPI49dPNAgMBAAECggEADXtSArwN99PXIFE6Wuab9JvRgQSDim2ujLw5tAEjSWZa\nDhEVVMF56cK2dNUSNCsIlkWxxI81wv5IBjSPwC1QjDwBXBoDk0eGAod4PcLG38Ou\ngVfXHlakeLr049Kw7C5qlG+4sAnCdZkczremNS47zpPNU0g3awZ3Iezq8C2kJlNq\nyY5pfYUOxi5b505LJBzYbr5uBd7BI4vlunK4pksKCjqYBavlX8Tv3dgbui5C4xRs\nQZwBKovXIvp3Ha/S+JLg42g+hX6Rj/PkKQgCEWHja/7ZVk7ePU2wQ/QdntuGOOl1\nuHLNoP+RiyM/pYGLBeo25yR9oK/W62DmAdEiW7loEQKBgQD6fzqESuq3JiAgVm+5\nBUWfiCaqEjU7aVu2s86AHNGonKKUtKmeil2jwp/J33fyR8QafashqBY61n7i5X9c\nJ1eAjPhnuEHKBPdTDpQD0G6js1jRPnv7d4Kmu9sq1/HZQ2T4ZTTfviEJfvGELm0I\nLj6tl6thlIO09u6LhxIs2JuZowKBgQDxbwDXS5q30Bt1Z/PkWdKZ4bEE+nK/TzoI\ne9gSAuUW+ylU/G4GrJunWZ4/07ZfhlSwKU+6aQYbak42P7Cvo9SxiMUuhAEqtQns\n2cBDk+2JiSMu0kbV1gVdxug5e8z2/iKbtRZ503qNeG4c0sNqbz2ME+hU9VWbDAAY\neVyDVSSTzwKBgQDy9aX/HF7NpzfvxYZ1UUy3MCo4OJLS/hyLd5ipn8omnU3/p78A\n27l5FVNATPQc1Ui6XPs4GLz+8n59ehTuf+YZ9CEXEJsW43wzXedoT6iQNGrIAK/m\nNoNNTtWDl5GmpfxwBFGlVdbbS/nat+De12PJoVsDuTWJtxulzytsvecluwKBgQDp\nHYQTXWXLW75Xk4LTlsMZX+jbZLNM80OWk3Wilnb6xJI5A+98tEcqxAZfnJ04CO1W\nltzroaKK8A8KpF6GiMrCjMvPSRgTU3B86BeTaI7vwKFfARvyNs9Bp9/sORRD3Egw\nTh6gjMiFNqYjYIHdEAG+ci5fce8xYNnqx6vDB3/k0wKBgQChdqx8MgVIk/w24IXd\nPPq4OTIIeAKN9Eyr5GIWnU2GuMN7DL5WcSHwnZVOeBquIyfpVAXwbWsLau3GuAJv\ne9AWyAJLVshEymCMEn7mD8tjPfNiWcUqnjzjuT2CHzprv7h3AGpzjIYgxadpGUdN\n8w2xKjZbS/K/4o6soJjJNjqRWA==\n-----END PRIVATE KEY-----\n",
  "client_email": "seventexttospeech@empyrean-app-332014.iam.gserviceaccount.com",
  "client_id": "108636702627397812418",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/seventexttospeech%40empyrean-app-332014.iam.gserviceaccount.com"
}

    """
    client = texttospeech_v1.TextToSpeechClient()

    voice_list = []
    for voice in client.list_voices().voices:
        voice_list.append([voice.name, voice.language_codes[0],
                           voice.ssml_gender, voice.natural_sample_rate_hertz])
    df_voice_list = pd.DataFrame(voice_list, columns=['name', 'language code', 'ssml gender', 'hertz rate']).to_csv(
        'Voice List.csv', index=False)

    # Set the text input to be synthesized
    quote = audio
    synthesis_input = texttospeech_v1.SynthesisInput(text=quote)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-in", ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    voice = texttospeech_v1.VoiceSelectionParams(
        # name='ar-XA-Wavenet-B', language_code="en-GB"
        name='en-GB-Wavenet-D', language_code="en-GB"
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
    filename = "./output" + str(random.randint(1, 100)) + ".mp3"
    with open(filename, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    playsound.playsound(filename)
    os.remove(filename)

def CoronaGet():
    covid = COVID19Py.COVID19(data_source="jhu")

    data = covid.getAll()

    latest = covid.getLatest()

    locations = covid.getLocations(timelines=True,
                                   rank_by='confirmed')

    print("Latest Data, \nConfirmed: " + str(latest["confirmed"]) + "\n. Deaths: " + str(
        latest["deaths"]) + "\n. Recovered: " + str(latest["recovered"]))


CoronaGet()
