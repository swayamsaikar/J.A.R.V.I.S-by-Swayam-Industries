# If your pyaudio is not installing then please type this command in your terminal :- pipwin install pyaudio
# This function will take the text from you as input and speak it using sapi5 (windows speech api)

from PyPDF2 import pdf
from gtts import gTTS  # Google Text to speech
import pyttsx3
import datetime  # using datetime module to get the current date
import speech_recognition as sr  # This module will convert your voice into text
# Using webbrowser module to open websites using webbrowser.open("www.google.com")
import webbrowser
# Using os module to open windows system programs using os.startfile(filepath)
import os
import pyjokes  # Using Pyjokes module to get jokes
import random  # Using random module to play random songs an*/d to generate random image names using random.randint()
import time  # Using time module to get the current time
import cv2  # Using openCV python module to open camera and take pictures
import requests
import wikipedia  # using wikipedia module to get wikipedia information of any thing
import pywhatkit as kit
import smtplib  # a module to send email using python
# Using This module to find the answer of any question
from pywikihow import search_wikihow

# Using googletrans module to translate the text
# Using Google Translator module to convert english pdf text to hindi
from googletrans import Translator
from playsound import playsound  # Using Playsound Module to play sounds
import keyboard
import pyautogui
import psutil
import platform
import math
import wolframalpha
from notifypy import Notify

# MY OWN ALARM MODULE
import MyAlarm
from FaceDetector import face_Detector


# code to solve the segmentation fault in python
import faulthandler
faulthandler.enable()


PYTHONFAULTHANDLER = 1


# ! To add a jarvis voice please open this file - How To Add The Jarvis Voice.txt

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


def wishMe():
    # Initializing Jarvis
    # playsound('mp3_files/Jarvis_Startup_sounds.mp3')

    hour = int(datetime.datetime.now().hour)
    current_time = datetime.datetime.now().strftime(
        '%I:%M %p')

    if hour >= 0 and hour < 12:
        speak(f"Good Morning Sir! now is {current_time}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon Sir! now is {current_time}")
    else:
        speak(f"Good Evening Sir! now is {current_time}")

    speak("I am Jarvis. Online and ready Sir. Please tell me how may I help you")


# This takecommand function will listen to your microphone input and store it in audio variable
# and we are using googles recognize engine to recognize and
# covert our audio input into text and return it
# This takeCommandForMainFunction() will only run on the main function
# takeCommandForMainFunction() will listen to me infinitely and if i do not say anything in my query it will speak this -> speak("Sorry Sir not able to recognize your voice") in the exception block
def takeCommandForMainFunction():
    # initialized the recognizer variable using the recognizer class in speech_recognition module
    recognizer = sr.Recognizer()

    # using the microphone as a source for input
    with sr.Microphone() as source:
        # source means microphone

        print("Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(
            audio, language="en-in")
        print(f"User Said : {query}\n")

    except Exception as e:  # try catch block in javascript
        speak("Sorry Sir not able to recognize your voice")
        print("Say That Again Please...")
        return "None"

    return query


# This takeCommandForWakeup() will only run while wakeup on the 585 line
# This function will keep listening to me and do not say anything if i dont speak, wheareas in the takeCommandForMainFunction() will listen to me infinitely and if i do not say anything in my query it will speak this -> speak("Sorry Sir not able to recognize your voice") in the exception block
def takeCommandForWakeup():
    # initialized the recognizer variable using the recognizer class in speech_recognition module
    recognizer = sr.Recognizer()

    # using the microphone as a source for input
    with sr.Microphone() as source:
        # source means microphone

        print("Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(
            audio, language="en-in")
        print(f"User Said : {query}\n")

    except Exception as e:  # try catch block in javascript
        #  it will say nothing in this function it will keep listening and when i speak anything it will go inside the if block
        return "None"

    return query


def sendMail(your_email, your_password, receiver_email_id, message):
    try:

        # SMTP => Simple Mail Transfer Protocol
        # creates a secure SMTP_SSL session
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        # You have to login with your account in order to send a mail
        smtp.login(your_email, your_password)

        # sending the mail
        smtp.sendmail(your_email, receiver_email_id, message)

        splitted_receiver_email_id = receiver_email_id.split('@')

        speak(
            f"Messsage sent Successfully to {splitted_receiver_email_id[0]} ")

        # terminating the session
        smtp.quit()

    except:
        print("Something Went Wrong!")
        speak("Something Went Wrong!")


def ActivateHomeAutomationSetup(appliances_to_activate):

    try:
        # This function will check that if bluestack is opening then it will close it else it will print the exception
        os.system('TASKKILL /F /im HD-Player.exe')
    except Exception as e:
        print(e)

    speak("Activating The Home Automation Setup sir...")

    # This function will press windows + s and search for bluestacks and open it
    keyboard.press_and_release('windows + s')

    time.sleep(2)

    # This function will type bluestack on the search bar
    keyboard.write('bluestack')

    time.sleep(1)

    # and press enter to open bluestacks(android emulator)
    keyboard.press('enter')

    time.sleep(12)

    # This function will click on the maximize button on bluestacks
    pyautogui.click(x=1838, y=144)

    time.sleep(2.5)

    # These if and else if conditions will check that if ac or light or tv is passed in the argument if true then execute that if else block
    if appliances_to_activate == "computer_room_light":

        # This function will click on the my smitch app to on the lights
        pyautogui.click(x=1735, y=277)

        time.sleep(3.3)

        # This function will click on the power button to turn the bulb on
        pyautogui.click(x=1161, y=210)

        time.sleep(1)

        os.system('TASKKILL /F /im HD-Player.exe')

        time.sleep(2)

        speak("Lights are on successfully Sir!")

    elif appliances_to_activate == "ac":
        speak("Sir The Order will be available on saturday and you will write the code to turn on the ac by me")
    elif appliances_to_activate == "tv":
        speak("Sir The Order will be available on saturday and you will write the code to turn on the tv by me")
    elif appliances_to_activate == "allLights":
        # there is current one smart blub in my house so if there will be multiple ones then i will write the code to turn on all the lights automatically
        # This function will click on the my smitch app to on the lights
        pyautogui.click(x=1735, y=277)

        time.sleep(3.3)

        # This function will click on the power button to turn the bulb on
        pyautogui.click(x=1161, y=210)

        time.sleep(1)

        os.system('TASKKILL /F /im HD-Player.exe')

        time.sleep(2)

        speak("Lights are on successfully Sir!")


def DeactivateHomeAutomationSetup(appliances_to_deactivate):
    try:
        # This function will check that if bluestack is opening then it will close it else it will print the exception
        os.system('TASKKILL /F /im HD-Player.exe')
    except Exception as e:
        print(e)

    speak("Deactivating The Home Automation Setup sir...")

    # This function will press windows + s and search for bluestacks and open it
    keyboard.press_and_release('windows + s')

    time.sleep(2)

    keyboard.write('bluestack')

    time.sleep(1)

    keyboard.press('enter')

    time.sleep(12)

    # This function will click on the maximize button on bluestacks
    pyautogui.click(x=1838, y=144)

    time.sleep(2.5)

    # if the value of the argument given is computer_room_light then do this
    if appliances_to_deactivate == "computer_room_light":

        # This function will click on the my smitch app to on the lights
        pyautogui.click(x=1735, y=277)

        time.sleep(3.3)

        # This function will click on the power button to turn the bulb on
        pyautogui.click(x=1161, y=210)

        time.sleep(1)

        os.system('TASKKILL /F /im HD-Player.exe')

        time.sleep(2)

        speak("Lights are off successfully Sir!")

    elif appliances_to_deactivate == "ac":
        speak("Sir The Order will be available on saturday and you will write the code to turn on the ac by me")
    elif appliances_to_deactivate == "tv":
        speak("Sir The Order will be available on saturday and you will write the code to turn on the tv by me")
    elif appliances_to_deactivate == "allLights":
        # there is current one smart blub in my house so if there will be multiple ones then i will write the code to turn on all the lights automatically
        # This function will click on the my smitch app to on the lights
        pyautogui.click(x=1735, y=277)

        time.sleep(3.3)

        # This function will click on the power button to turn the bulb on
        pyautogui.click(x=1161, y=210)

        time.sleep(1)

        os.system('TASKKILL /F /im HD-Player.exe')

        time.sleep(2)

        speak("Lights are off successfully Sir!")


def joinClass(className):
    classNames = {
        "english": "https://meet.google.com/uvm-tevn-vek",
        "odia": "https://meet.google.com/rdu-gsbb-gzj",
        "science": "http://meet.google.com/wxp-vpka-sdi",
        "hindi": "https://meet.google.com/jgq-kpbn-ecd",
        "sst": "https://meet.google.com/uzk-kahz-omu"
    }

    # This function will search the name of the class which is passed in the className(parameter) in the classNames Dictionary
    classLink = classNames[className]
    speak(f"Opening {className} class Link sir")
    # This function will open the classLink in the browser
    webbrowser.open(classLink)

    # This function will click on the switch account button in the google meet
    time.sleep(4)
    pyautogui.click(x=1798, y=144)

    # This function will choose the account
    time.sleep(3)
    pyautogui.click(x=904, y=550)

    # This function will click on th mute button
    time.sleep(2.5)
    pyautogui.click(x=688, y=731)

    # This function will switch off the video (or click on the Switch-Off Video Button)
    time.sleep(1)
    pyautogui.click(x=769, y=726)

    # This function will Join The meeting
    time.sleep(0.5)
    pyautogui.click(x=1258, y=597)

    speak("Joining class")
    speak(f"{className} class Successfully opened sir")


def takeCommandForTranslation():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # source means microphone
        print("Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        # This function will recognize our voice in hindi and then it will convert it into string(so that we can perform if and else operations ) and store it in query variable ans return it
        query = recognizer.recognize_google(
            audio, language="hi")
        print(f"User Said : {query}\n")

    except Exception as e:  # try catch block in javascript
        speak("Sorry Sir not able to recognize your voice")
        print("Say That Again Please...")
        return "None"

    return query


def Translate():
    # Initializing the Translator class
    translator = Translator()
    speak("Sir Please tell the line in hindi that you want to translate in english ?")
    # taking the voice input from the user and storing it in this variable called text
    # This function returns our voice input as a string
    text = takeCommandForTranslation().lower()
    # This function will translate the Hindi text into english and extract the translated text from it and speak it
    translatedText = translator.translate(text, "en").text
    print(f"Translated Text :- {translatedText}")
    speak(translatedText)


def remember(text_to_remember):
    # The idea is that i will store the remembered_text in a new file and whenever the user will tell me ("jarvis what do you remember") then i will retrive the text data from that file and show it to the user
    remembered_text = str(text_to_remember).replace("remember that", "")
    remembered_text = remembered_text.replace("jarvis", "")
    speak(f"sir you told me to remember that :- {remembered_text}")

    # I am creating a new file called remembered_text.txt in write mode as f and we are simply writing the remembered text in that txt file
    with open("remembered_text.txt", "w") as f:
        f.write(remembered_text)
        speak("Sir what you told now to remember is successfully stored in the remembered_text.txt file")


def convert_size(size_bytes):
    # This function wil take a size in its argument and convert it to gigabytes
    c = size_bytes/1024/1024/1024
    return math.floor(c)


def AboutMyPC():
    # This function returns a tuple of your system information line processor,pc name,release,OS version and Machine Type
    systemDetails = platform.uname()

    # This function will tell your OS Type ex - Windows or Mac or linux
    print(f"System OS is : {systemDetails.system}")
    speak(f"Sir Your system OS is : {systemDetails.system}")

    # This function will tell your desktop/laptop's name
    print(f"System Name is : {systemDetails.node}")
    speak(f"Sir Your system name is : {systemDetails.node}")

    # This function will tell your system's release version
    print(f"System Release version is : {systemDetails.release}")
    speak(f"System Release version  is: {systemDetails.release}")

    # This function will tell your system's current OS build version
    print(f"System OS version is : {systemDetails.version}")
    speak(f"System OS version is : {systemDetails.version}")

    # This function will tell your Machine Type eg. 'i386' or 'AMD64'
    print(f"Machine Type is : {systemDetails.machine}")
    speak(f"Sir Your Machine Type is : {systemDetails.machine}")

    # This function will give your processor Info
    print(f"Processor info is : {systemDetails.processor}")
    speak(f"Sir your Processor Info is : {systemDetails.processor}")


def CPU_stats():
    CPU_Percentage = str(psutil.cpu_percent(interval=1))
    Used_Ram = convert_size(psutil.virtual_memory().used)
    Total_Ram = convert_size(psutil.virtual_memory().total)
    # so if you are in laptop you can uncomment this line
    # Battery_Percentage = psutil.sensors_battery().percent

    print(
        f'Sir currently {CPU_Percentage} % of CPU, {Used_Ram} GB of RAM out of total {Total_Ram} GB is being used.')
    speak(
        f"Sir currently {CPU_Percentage} percent of CPU, {Used_Ram}GB of RAM out of total {Total_Ram}GB is being used.")


def askQuestion(question):

    q = question.replace("what is the", "")
    q = q.replace("what is", "")
    q = q.replace("jarvis", "")
    q = q.replace(".", "")

    api_key = "3TY68L-YEEKT5E64L"

    # creating an instance of wolframalpha class with its api_key
    WolframAlpha = wolframalpha.Client(api_key)

    # it will try to get the answer. if it gets the answer then it returns it
    # if it does not able to get the answer then it will move to the except block
    try:
        # This function will take the question as query and return the response(result)
        Question = WolframAlpha.query(q)
        # we are simple extracting the text from the result and returning it
        result = next(Question.results).text
        return result

    except:
        speak("Sorry Sir Something went wrong !")
        print("Sorry Sir Something went wrong !")
        return "Sorry cannot find answer of your question"


def calculate(query):
    q = query.replace("jarvis", "")
    q = q.replace("plus", "+")
    q = q.replace("minus", "-")
    q = q.replace("multiply", "*")
    q = q.replace("divide", "/")
    q = q.replace("by", "/")
    q = q.replace("into", "*")
    q = q.replace("what is ", "")

    FinalQuery = str(q)
    answer = askQuestion(FinalQuery)
    return answer


def whatsappAutomation(username, message=None, call=False):
    # Below function will check wheather whatsapp is opened or not if open it will close it and run the below programs
    os.system('taskkill /F /IM WhatsApp.exe')

    try:

      # search for whatsapp app by pressing windows + s
        keyboard.press_and_release("windows + s")
        time.sleep(1)

        # It will search for Whatsapp
        keyboard.write("Whatsapp")
        time.sleep(1)

        # Then Press Enter
        keyboard.press_and_release("enter")

        # The The program will wait 5 seconds for whatsapp to open
        time.sleep(6.5)

        # first it will click on the search box and then search for the username
        time.sleep(1)
        pyautogui.click(x=106, y=107)
        time.sleep(1)
        keyboard.write(username)
        time.sleep(2)

        # after searching it will click on a specific position
        time.sleep(1)
        pyautogui.click(x=181, y=256)

        if call == False:
            speak(f"Messaging to {username} Sir")
            print(f"Messaging to {username} Sir")
            # click on the text input and write the message and then press enter if the call parameter is set to false
            time.sleep(0.5)
            pyautogui.click(x=880, y=991)
            time.sleep(1)
            keyboard.write(message)
            time.sleep(0.5)
            keyboard.press_and_release('enter')

            print(f"Messaged successfully to {username} sir")
            speak(f"Messaged successfully to {username} sir")

        # else if the call parameter is set to True then it will click on the call button
        else:
            speak(f"Calling to {username} Sir")
            print(f"Calling to {username} Sir")

            # click on the call button
            time.sleep(1)
            pyautogui.click(x=1764, y=65)
            print(f"successfully called to {username} sir")
            speak(f"successfully called to {username} sir")
    except:
        speak("Sorry Sir There is some problem")


def main():
    while True:
        query = takeCommandForMainFunction().lower()

        if "hello" in query:
            speak("Hi Sir How are you ?")

        elif "upload my project to github" in query:
            speak("ok sir uploading your project in github")
            # this git_automation program will take the project name,project path and commit message as input and host the project automatically for you in github using github
            from automation_files import git_automation

            git_automation

        elif "call to" in query:
            username = query.replace("call to ", "")
            username = username.replace("jarvis", "")
            # send whatsapp message function
            whatsappAutomation(username, call=True)

        elif "message to" in query:
            MessageUsername = query.replace("message to ", "")
            MessageUsername = MessageUsername.replace("jarvis", "")
            speak("What message to send sir ?")
            message = takeCommandForMainFunction().lower()
            speak(f"Messaging to {MessageUsername}...")
            print(f"Messaging to {MessageUsername}...")
            whatsappAutomation(MessageUsername, message)

        elif "schedule" in query:
            # Code to find the current week day ex - lets say today is tuesday so the weekday of tuesday is 1 and the weekday of monday is 0 ...
            TodaysWeekDay = datetime.datetime.now().weekday()

            # If todays week day is equal to 0 that is moday then run this if block
            if TodaysWeekDay == 0:
                # imported my time() function from Moday.py file in TimeTable directory
                from TimeTable.Monday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

            if TodaysWeekDay == 1:
                # imported my time() function from Tuesday.py file in TimeTable directory
                from TimeTable.Tuesday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

            if TodaysWeekDay == 2:
                # imported my time() function from Wednesday.py file in TimeTable directory
                from TimeTable.Wednesday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

            if TodaysWeekDay == 3:
                # imported my time() function from Thursday.py file in TimeTable directory
                from TimeTable.Thursday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

            if TodaysWeekDay == 4:
                # imported my time() function from Friday.py file in TimeTable directory
                from TimeTable.Friday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

            if TodaysWeekDay == 5:
                # imported my time() function from Saturday.py file in TimeTable directory
                from TimeTable.Saturday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

            if TodaysWeekDay == 6:
                # imported my time() function from Sunday.py file in TimeTable directory
                from TimeTable.Sunday import time

                # Here we have to create a instance of Notify class
                Notification = Notify()

                # Now we have to send the notification
                Notification.title = "Todays Time Table"

                # This time() will return what you have to do now (returns in the form of a string) and also speaks it
                Notification.message = time()

                # send the Notification
                Notification.send()

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("Alright")
                print(results)
                speak("According To Wikipedia")
                speak(results)
            except Exception as e:
                speak("Wikipedia Not Found")
                print("Wikipedia not found")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open('www.google.com')

        elif "sleep" in query:
            speak("Ok sir I am sleeping now and you can call me anytime you want!")
            break

        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open('www.youtube.com')

        elif "open stack overflow" in query:
            speak("Opening StackOverflow...")
            webbrowser.open('https://stackoverflow.com/')

        elif "lights on" in query:
            ActivateHomeAutomationSetup("allLights")

        elif "lights off" in query:
            DeactivateHomeAutomationSetup("allLights")

        elif "turn on the computer room" in query:
            ActivateHomeAutomationSetup("computer_room_light")

        elif "turn off the computer room" in query:
            DeactivateHomeAutomationSetup("computer_room_light")

        elif "ac on" in query:
            ActivateHomeAutomationSetup("ac")

        elif "ac off" in query:
            DeactivateHomeAutomationSetup("ac")

        elif "tv on" in query:
            ActivateHomeAutomationSetup("tv")

        elif "tv off" in query:
            DeactivateHomeAutomationSetup("tv")

        elif "react native" in query:
            speak("Opening react native documentation.")
            webbrowser.open(
                'https://reactnative.dev/docs/getting-started')

        elif "react navigation" in query:
            speak("Opening react navigation...")
            webbrowser.open(
                'https://reactnavigation.org/docs/getting-started')

        elif "white hat" in query:
            speak("Opening whitehat junior ...")
            webbrowser.open(
                'https://code.whitehatjr.com/s/dashboard')

        elif "how are you" in query:
            speak("I am Fine Sir,what about you ?")

        elif "code editor" in query:
            speak('opening your favorite code editor Visual Studio Code Sir ')
            print("opening Visual Studio Code ")
            os.startfile(
                "C:\\Users\\Swaya\\AppData\\Local\\Programs\\Microsoft VS Code")

        elif "english class" in query:
            joinClass("english")

        elif "odia class" in query:
            joinClass("odia")

        elif "sst class" in query:
            joinClass("sst")

        elif "science class" in query:
            joinClass("science")

        elif "hindi class" in query:
            joinClass("hindi")

        elif "thank you" in query:
            speak("Welcome Sir! Its my responsibility")
            print("Welcome Sir! Its my responsibility")

        elif "joke" in query:
            joke = pyjokes.get_joke(language='en', category="neutral")
            print(joke)
            speak(joke)

            print("Hahaha what a funny joke")
            speak("Hahaha what a funny joke")

        elif "made you" in query or "created you" in query or "developed you" in query:
            speak("I have been created by Swayam")

        elif "music" in query:
            speak("Here we go")
            musicDir = "music"
            music_list = os.listdir(musicDir)
            # random.choice() method return a random element from an array or tuple etc.
            random_song = random.choice(music_list)
            music_path = os.path.join(musicDir, random_song)
            os.startfile(music_path)

        elif "chrome" in query:
            speak("Opening Google Chrome...")
            os.startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")

        elif "github" in query:
            speak("Opening Github...")
            webbrowser.open("www.github.com/swayamsaikar")

        elif "time" in query:
            currentTime = datetime.datetime.now().time().strftime("%H:%M")
            print(f"The Time is {currentTime}")
            speak(f"The Time is {currentTime}")

        elif "minecraft" in query:
            speak("Opening Minecraft...")
            os.startfile(
                'C:\\Users\\Swaya\\AppData\\Roaming\\.minecraft\\TLauncher')

        elif "take image" in query:
            boolean = True
            random_imagename = random.randint(0, 100)
            speak("Capturing Image")
            cameraObject = cv2.VideoCapture(0)
            while(boolean):
                image_name = "C:\\Users\\Swaya\\\Pictures\\Saved Pictures\\image" + \
                    str(random_imagename)+'.png'
                ret, frame = cameraObject.read()
                cv2.imwrite(image_name, frame)
                boolean = False

            cameraObject.release()
            cv2.destroyAllWindows()
            # time.sleep(1.5)
            speak("Sir Image is now successfully saved in your pictures folder")
            os.startfile(
                image_name)

        elif "open notepad" in query:
            speak("Opening Notepad...")
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif "open command prompt" in query or "open cmd" in query:
            speak("Opening Command Prompt...")
            os.system("start cmd")

        elif "open webcam" in query:
            # specifying the camera
            camera_Object = cv2.VideoCapture(0)
            # generating a random number
            random_imagename2 = random.randint(0, 100)
            speak("Opening Webcam...")
            while(True):
                # This function will read each frame or image and store all the Image values in the frame variable
                ret, frame = camera_Object.read()
                # This will show each frame or image in a window named "Web cam"
                cv2.imshow("Web Cam", frame)
                # This will wait for the user for 50 milliseconds to press the key "Q" or C key on the keyboard
                key = cv2.waitKey(1)
                # 113 means Q key on keyboard
                if key == 113:
                    break
                # 99 means c
                elif key == 99:
                    # Remember You can only take one Image
                    ImageName = "C:\\Users\\Swaya\\Pictures\\Saved Pictures\\image" + \
                        str(random_imagename2) + \
                        '.png'  # This is the path where the image will be stored with a random name
                    # This will store the image in the specified path that is(ImageName)
                    cv2.imwrite(ImageName, frame)
                    speak("Sir Image is now successfully saved in your pictures folder")
                    # This function will open the image after capturing it
                    os.startfile(ImageName)

            # when the user will press the q key the program will break from the while loop and close the windows of the camera
            camera_Object.release()
            cv2.destroyAllWindows()

        elif "ip" in query:
            my_ip = requests.get("https://api.ipify.org").text
            print(f"Your IP-Address is {my_ip}")
            speak(f"Your IP-Address is {my_ip}")

        elif "search google" in query:
            speak("Sir,what should I search?")
            print("Sir,what should I search? :-")

            user_query = takeCommandForMainFunction().lower()
            speak("searching on google...")
            # This method will make a google search on the search query that you pass to it
            kit.search(user_query)

        elif "search youtube" in query:
            speak("Sir,what should I search on Youtube?")
            print("Sir,what should I search on Youtube? :-")

            search_query_youtube = takeCommandForMainFunction().lower()
            speak("searching...")
            # This method will make a youtube search on the search query that you pass to it and play the video
            kit.playonyt(search_query_youtube)

        elif "email" in query:
            speak(
                "Sir Please enter your email and password in the terminal in order to login into your gmail ")
            your_email = input("Sir Enter your email_id here \n")
            your_password = input("Sir Enter your password here \n")

            speak(
                "Sir Please enter the email id of the person you want to send the email")

            receiver_email_id = input(
                "Sir Please Enter the email id to whom you want to send the mail\n")

            splitted_receiver_email_id = receiver_email_id.split('@')

            speak(
                f"Sir now please tell the message you want to send to {splitted_receiver_email_id[0]} ")

            message = takeCommandForMainFunction().lower()

            sendMail(your_email, your_password, receiver_email_id, message)

        elif "how to" in query:
            speak("Searching From Internet...")
            search = query.replace('Jarvis', "")
            max_results = 1
            how_to = search_wikihow(search, max_results)
            if len(how_to) == 1:
                print(how_to[0].summary)
                speak(how_to[0].summary)

        elif "i am also good" in query or "i am also fine" in query:
            speak("Ok that's great to hear from you .")

        elif "internet speed" in query or "net speed" in query:
            import speedtest
            # Using Module to test internet speed
            speak("Checking Internet Speed Sir...")
            print("Checking Internet Speed Sir...")
            speed = speedtest.Speedtest()
            upload = speed.upload()
            correct_upload = int(int(upload)/80000)

            download = speed.download()
            correct_download = int(int(download)/80000)

            speak(
                f'Download Speed is {correct_download} MB Per Second and Upload Speed is {correct_upload} M B Per Second')
            print(
                f'Download Speed is {correct_download} MB Per Second and Upload Speed is {correct_upload} M B Per Second')

        elif "read a book" in query:
            speak("Sir Please write the name of the book that you want me to read")
            print("Sir Please write the name of the book that you want me to read")
            bookName = input('Enter The Name Of The Book: \n')

            try:
                # opens the pdf
                # Please set your PDF directory here
                os.startfile(
                    f"D:\\essentials\\Web developer\\{bookName}.pdf")

                with open(f"D:\\essentials\\Web developer\\{bookName}.pdf", "rb") as book:

                    # this function will read read that file and get all the info about that file
                    pdfReader = pdf.PdfFileReader(book)

                    # This function will print all the pages of the pdf
                    pages = pdfReader.getNumPages()

                    print(f"Sir, there are {pages} pages in this pdf file")
                    speak(f"Sir, there are {pages} pages in this pdf file")

                    # Asks the user to choose the page number which Jarvis will read
                    speak("So sir from which page i have to start reading ?")

                    # converting the page number into integer
                    pageNumber = int(
                        input("Sir Please enter the page number: \n"))

                    # getting all the details about that page
                    page = pdfReader.getPage(pageNumber-1)

                    # This function will extract all the text from that page and store it to bookContent variable
                    bookContent = page.extractText()

                    # This function will ask the to choose the language
                    speak('Sir In which language, I have to read ?')

                    # takecommand() function will listen to the user's input through microphone
                    languageQuery = takeCommandForMainFunction().lower()

                    #  If The user says hindi then the compiler will go into the if-block else it will go inside the else block
                    #  If the user says anything other than hindi then it will read the pdf file in english
                    if "hindi" in languageQuery:
                        try:
                            # created an instance of Translator class
                            translator = Translator()

                            # this function will translate the bookcontent to hindi and store that in translateTheTextInHindi variable
                            translateTheTextInHindi = translator.translate(
                                bookContent, 'hi').text

                            # This function will take that hindi Text Data and speak it using google's text to speech and save that audio file with the name called book.mp3 and we are playing that audio file
                            speech = gTTS(text=translateTheTextInHindi)

                            randomInt = random.randint(1, 100)
                            # saving that
                            speak("Saving The Audio file sir")
                            speech.save(f'mp3_files\\book{randomInt}.mp3')

                            speak("Sir Please Wait...")
                            print("Sir Please Wait...")

                            speak("Playing The audio file")
                            # play that audio file
                            # os.startfile(f"mp3_files\\book{randomInt}.mp3")
                            playsound(f"mp3_files\\book{randomInt}.mp3")

                            speak("Reading Completed Sir")

                            os.remove(f'mp3_files\\book{randomInt}.mp3')

                        except:
                            speak(
                                "Sorry Sir No Text To Speech Available for this file")
                            print(
                                "Sorry Sir No Text To Speech Available for this file")
                    else:
                        # This function will read the pdf file in  English
                        speak("reading it in english")
            except:
                speak(f"Sorry Sir no such file named {bookName} exists")

        elif "introduce yourself" in query:
            playsound("mp3_files/Jarvis_About.mp3")

        elif "temperature" in query:
            # removing the last word "jarvis" from the user query
            query = query.replace(" jarvis", "")

            # currently the output temperature is "27 °C (heat index: 30 °C)(1 hour 43 minutes ago)""
            speak("Measuring Temperature Sir...")
            temperature = askQuestion(query)

            # Now after spliting out the temperature by this -> "("
            splittedTemperature = temperature.split("(")
            # now the value of splittedTemperature variable is  ['27 °C ', 'heat index: 30 °C)\n', '1 hour 42 minutes ago)'] and i need the first element that is only the temperature

            splittedQuery = query.split(" ")
            # now after splitting out the query by space the output is = ['what', 'is', 'the', 'temperature', 'in', 'india'] and i need the last element of splittedQuery list

            # {splittedQuery[-1]} means that the last index element of the query and splittedTemperature[0] is the first element of splittedTemperature array

            if temperature == "Sorry cannot find answer of your question":
                speak("Sorry sir I cannot find the temperature")
            else:
                print(
                    f"Sir the current temperature in {splittedQuery[-1]} is {splittedTemperature[0]}")
                speak(
                    f"Sir the current temperature in {splittedQuery[-1]} is {splittedTemperature[0]}")

        elif "exit" in query:
            speak("Thanks for using me sir, have a nice day!")
            exit()

        elif "open translator" in query:
            Translate()

        elif "remember that" in query:
            remember(query)

        elif "what do you remember" in query:
            #  We are simply opening this file and reading all its content and printing it
            with open("remembered_text.txt", "r") as f:
                text = f.read()
                print(f"sir you told me to remember that :- {text}")
                speak(f"sir you told me to remember that :- {text}")

        elif "system info" in query or "system information" in query or "about my pc" in query:
            AboutMyPC()

        elif "system statistics" in query or "cpu statistics" in query or "cpu" in query:
            CPU_stats()

        elif "alarm" in query:
            try:

                speak("Sir please tell the time that you want to set the alarm in")

                # currently alarmInput value =  "set alarm to 2:30 a.m."
                # "set alarm to 2:30 a.m."

                alarmInput = takeCommandForMainFunction()

                command = alarmInput.replace(
                    "set alarm at ", "")  # "2:30 a.m."
                command = command.replace(".", "")  # "2:30 am"

                # Then i have to make the 2:30 **am** Uppercase
                command = command.upper()  # "2:30 AM"

                # Now i can call my module and pass my alarm time in string as an argument
                MyAlarm.alarm(command)

            except Exception as e:
                speak("Sorry sir unable to set alarm please provide a valid alarm time")

        elif "security system" in query:
            face_Detector()

        elif "what is" in query or "who is" in query:
            q = query.replace("the meaning of", "")
            q = q.replace("what is ", "")
            q = q.replace(".", "")
            q = q.replace("who is ", "")
            speak("Sir Please wait...")
            print("Sir Please wait...")

            if "plus" in q or "minus" in q or "by" in q or "into" in q:
                answer = calculate(q)
                if answer == "Sorry cannot find answer of your question":
                    speak("Sorry sir i am not able to find the answer of your question")
                else:
                    print(f"Sir The answer of your question is  -> {answer}")
                    speak(f"Sir The answer of your question is {answer}")

            else:
                answer = askQuestion(q)

                if answer == "Sorry cannot find answer of your question":
                    speak("Sorry sir i am not able to find the answer of your question")
                else:
                    print(f"Sir The answer of your question is  -> {answer}")
                    speak(f"Sir The answer of your question is {answer}")


if __name__ == '__main__':
    print('''
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗    ░██████╗░██╗░░░░░░░██╗░█████╗░██╗░░░██╗░█████╗░███╗░░░███╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝    ██╔════╝░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝██╔══██╗████╗░████║
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░    ╚█████╗░░╚██╗████╗██╔╝███████║░╚████╔╝░███████║██╔████╔██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░    ░╚═══██╗░░████╔═████║░██╔══██║░░╚██╔╝░░██╔══██║██║╚██╔╝██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗    ██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝    ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝
          ''')
    wishMe()
    # when
    main()
    while(True):
        query = takeCommandForWakeup().lower()

        if "wake up" in query:
            speak("Ok jarvis online and ready sir!")
            main()

        elif "exit" in query:
            speak("Thanks for using me sir, have a nice day!")
            exit()


# MADE BY SSK(SWAYAM SAI KAR)
