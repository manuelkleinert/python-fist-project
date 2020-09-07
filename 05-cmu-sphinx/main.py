# #!/usr/bin/env python3.6
# import os
# from pocketsphinx import LiveSpeech, get_model_path
#
# model_path = get_model_path()
#
# speech = LiveSpeech(
#     verbose=False,
#     sampling_rate=16000,
#     buffer_size=2048,
#     no_search=False,
#     full_utt=False,
#     hmm=os.path.join(model_path, 'en-us'),
#     lm=os.path.join(model_path, 'en-us.lm.bin'),
#     dic=os.path.join(model_path, 'cmudict-en-us.dict')
# )
#
# for phrase in speech:
#     print(phrase)

import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("Please say something")

    audio = r.listen(source)

    print("Recognizing Now .... ")


    # recognize speech using google

    try:
        print("You have said \n" + r.recognize_google(audio))
        print("Audio Recorded Successfully \n ")


    except Exception as e:
        print("Error :  " + str(e))




    # write audio

    with open("recorded.wav", "wb") as f:
        f.write(audio.get_wav_data())
