if 'Alarm' in r2.recognize_google(audio):
    speak("What time should I set the alarm?")
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url + get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
# filename = 'alarm.wav'
# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
# play_obj.wait_done()
