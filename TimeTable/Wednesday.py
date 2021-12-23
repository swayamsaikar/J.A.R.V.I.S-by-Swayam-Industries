import datetime
import pyttsx3

# Initializing Text to speech module
engine = pyttsx3.init('sapi5')
# print this voices array to see the list of all voices that are in your pc
voices = engine.getProperty('voices')
# You can change the voices according to yourself by analyzing the voices array
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)
# You can Change All The code according to yourself


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Todo Variables
Sixto7 = '''
    Sir Now you have to get up from your Bed and do your essentials and Then you have to Meditate
'''

Sevento8 = '''
    In This time you have to get Up From Meditation and Code
'''

Eightto9 = '''
    In This time you have to attend your Social Science Class
'''

Nineto10 = '''
    In This time you have to attend your Science Class
'''

Tento11 = '''
    In This time you have to attend your Odia Class
'''

Elevento12 = '''
    In This time you have to Code
'''

Twelveto13 = '''
    Sir In this time you have to research on your coding class topic
'''

Thirteento14 = '''
    Sir now you have to attend your coding class. Best of Luck!
'''

Fourteento15 = '''
    Sir In This time you have to take bath and do your lunch and then you have to complete your tution homework
'''

Fiveteento17 = '''
    Sir now you have to attend your tution class. Best of Luck! .
'''

SeventeenTo19 = '''
    Sir Now you have to complete your coding projects and Practice
'''

Nineteento22 = '''
    Sir In this time you have to study for your exams
'''
TwentyTwo_to_24 = '''
    Sir In this time you have to Practice In Coding
'''


def time():
    current_time = int(datetime.datetime.now().hour)
    if current_time >= 6 and current_time < 7:
        speak(Sixto7)
        return Sixto7

    elif current_time >= 7 and current_time < 8:
        speak(Sevento8)
        return Sevento8

    elif current_time >= 8 and current_time < 9:
        speak(Eightto9)
        return Eightto9

    elif current_time >= 9 and current_time < 10:
        speak(Nineto10)
        return Nineto10

    elif current_time >= 10 and current_time < 11:
        speak(Tento11)
        return Tento11

    elif current_time >= 11 and current_time < 12:
        speak(Elevento12)
        return Elevento12

    elif current_time >= 12 and current_time < 13:
        speak(Twelveto13)
        return Twelveto13

    elif current_time >= 13 and current_time < 14:
        speak(Thirteento14)
        return Thirteento14

    elif current_time >= 14 and current_time < 15:
        speak(Fourteento15)
        return Fourteento15

    elif current_time >= 15 and current_time < 17:
        speak(Fiveteento17)
        return Fiveteento17

    elif current_time >= 17 and current_time < 19:
        speak(SeventeenTo19)
        return SeventeenTo19

    elif current_time >= 19 and current_time < 22:
        speak(Nineteento22)
        return Nineteento22

    elif current_time >= 22 and current_time < 24:
        speak(TwentyTwo_to_24)
        return TwentyTwo_to_24

    else:
        speak("Sir You have to Sleep")
        return "Sir You have to Sleep"


