import openai
import speech_recognition as sr
import pyttsx3

text_speech = pyttsx3.init()
openai.api_key = "YOUR API KEY HERE"

text_speech.say("Neptune at your service sir")
text_speech.runAndWait()
text_speech.say("Please give command")
text_speech.runAndWait()


def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
        
        try:
            
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": str(r.recognize_google(audio))}])
            print(completion.choices[0].message.content)
            text_speech.say(completion.choices[0].message.content)
            text_speech.runAndWait()
            main()
 
 
        except Exception as e:
            print("Error/No Response :  " + str(e))
            text_speech.say(str(e))
            text_speech.runAndWait()
            main()
 
 
main()