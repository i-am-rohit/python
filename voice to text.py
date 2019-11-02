import speech_recognition as sr
r = sr.Recognizer()

while True:

    with sr.Microphone() as source:
        print("say something")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("recognising")
        audio = r.recognize_google(audio, language='en-in')
        print(f"User said: {audio}\n");

    except Exception as e:
        print("say that again")
