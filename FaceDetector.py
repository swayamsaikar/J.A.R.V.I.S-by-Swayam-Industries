import cv2
import random
import winsound
import pyttsx3

# Initializing Text to speech module
engine = pyttsx3.init('sapi5')
# print this voices array to see the list of all voices that are in your pc
voices = engine.getProperty('voices')
# You can change the voices according to yourself by analyzing the voices array
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def face_Detector():
    speak("Opening Camera sir")
    CameraObject = cv2.VideoCapture(0)

    # Initializing the model
    model = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

    speak("Face Detector Online Sir")

    while(True):
        # generating a random image name
        randomImageName = random.randint(0, 100)
        # Reading Every Frame Through Camera
        _, frame = CameraObject.read()

        # Converting it to gray scale
        gray_scaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # This function will detect our face in the gray_scaled_Image and return our face coordinates
        face_coordinates = model.detectMultiScale(gray_scaled_frame)

        # if there will be multiple faces then our face detector will make a rectangle on each and every face
        # so to do that we are going to loop through all the x,y,w,h coordinates and make a rectangle
        for (x, y, w, h) in face_coordinates:
            # creating a rectangle on each and every face's x,y,w,h coordinates with a green color outline and thickness=2
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # capturing each detected image and saving it with a random image file name
            cv2.imwrite(
                f"CCTV_Detected_Images\image{randomImageName}.png", frame)

        # if a face is detected then the length of the face_coordinates variable is always greater than 0

        if len(face_coordinates) > 0:
            # This will Play a beep sound whenever it detects someone
            winsound.Beep(frequency=500, duration=winsound.SND_LOOP)

        # showing The Image or frame
        cv2.imshow("Swayam's Face Detector", frame)

        # waiting for the user 10 milliseconds to press a key
        # and if the user will press the q key on the keyboard this will break through the loop
        if cv2.waitKey(10) == ord("q"):
            CameraObject.release()
            cv2.destroyAllWindows()
            speak("Face Detector successfully closed sir")
            speak(
                "sir all the detected images are successfully saved in the CCTV Detected Images folder")
            break
