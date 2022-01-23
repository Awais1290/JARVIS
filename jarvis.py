from math import factorial, trunc
from sys import path
from typing import Text
from urllib.parse import quote_from_bytes
from weakref import WeakKeyDictionary
from cv2 import destroyAllWindows, destroyWindow
from pip import main
import pyttsx3
from pyttsx3 import engine, speak
from pywhatkit.main import playonyt, search
import requests
import speech_recognition as sr
import datetime
import os
import sys
import cv2
import random
from requests import get
import pywhatkit as kit
import wikipedia
import webbrowser
import smtplib
from bs4 import BeautifulSoup
from pyttsx3 import engine
import requests
from requests import get
from bs4 import *
from time import *
import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import QTimer ,QTime ,QDate , Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyautogui
from PyQt5.uic import loadUiType
from AdvanceGui import Ui_JARVIS
from LoadingNew import Ui_LoadingNew
from Location import Ui_MainWindow
import pyttsx3
from keyboard import *
import speech_recognition as sr
import os
import cv2
import numpy as np
import pyautogui as p


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.myface(),Main(), self.wish(), self.speak(), self.TaskExecution()

    def wish(self):
        hour = int(datetime.datetime.now().hour)

        if hour>=0 and hour<=12:
            speak("good morning sir")
        elif hour>=12 and hour<=18:
            speak("good afternoon sir")
        else:
            speak("good evening sir")
        speak('hello sir, i am jarvis sir, please tell me how may i help you')

    def speak(audio):
            engine.say(audio)
            print(audio)
            engine.runAndWait()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold =1.5
            audio = r.listen(source)
        try:
            print("Recognizing...") 
            query = r.recognize_google(audio, language='en-pk')
            print(f"user said: {query}")
        except Exception as e:
            speak('i think i am still building on this function sir')
            return "none"
        query = query.lower()
        return query

    def TaskExecution(self):
        p.press('esc')
        speak("verification successful")
        self.wish()

        while True:
            self.query = self.takecommand()

            if 'sleep' in self.query:
                speak('ok sir i am going sleep you can call me anytime')
                break

            elif "exit" in self.query:
                sys.exit()

            elif 'thanks jarvis' in self.query:
                speak('no problem sir this is my job')
            
            elif 'real program' in self.query:
                speak('ok sir starting real gui')
                jarvis = Main()
            
            elif 'jarvis scan my face' in self.query:
                self.myface()

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
            
            elif 'volume down' in self.query:
                pyautogui.press("volumedown")
            
            elif 'volume mute' in self.query:
                pyautogui.press("volumemute")

            elif 'open notepad' in self.query:
                npath = 'C:\\Windows\\system32\\notepad.exe'
                speak('ok sir opening notepad')
                os.startfile(npath)
                    
            elif 'open command prompt' in self.query:
                speak('ok sir opening command prompt')
                os.system('start cmd')

            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                cv2.WINDOW_FULLSCREEN
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
                speak('sir your camera is on')
            
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'close camera' in self.query:
                speak('i think i am still building on this function')

            elif 'play music' in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("i think you will like it")
            
            elif 'print music' in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                speak(songs)

            elif 'track my location' in self.query:
                    ip_add = requests.get('https://api.ipify.org').text
                    url = 'https://get/geojs.io/v1/ip/geo/' + ip_add + '.json'
                    geo_q = requests.get(url)
                    geo_d = geo_q.json()
                    state = geo_d['city']
                    country = geo_d['country']
                    speak(f'Sir, You are in {state , country} .')

            elif 'Ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif 'wikipedia' in self.query:
                speak("searching wikipedia.........")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak(results)
                print(results)

            elif 'open youtube' in self.query:
                speak('opening youtube')
                webbrowser.open('www.youtube.com')
                speak('done')

            elif 'open google' in self.query:
                speak('ok sir opening google')
                webbrowser.open ("www.google.com")
                speak('done')

            elif 'weather outside' in self.query:
                search = "temperature in Multan"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_= "BNeawe").text
                speak(f"Sir, The Temperature Outside is {temp}")

            elif 'open facebook' in self.query:
                speak('opening facebook')
                webbrowser.open('www.facebook.com')
                speak('done')

            elif 'open stackoverflow' in self.query:
                speak('opening stackoverflow')
                webbrowser.open('www.stackoverflow.com')
                speak('done')
            elif 'open Amazon' in self.query:
                speak('opening Amazon')
                webbrowser.open('www.amazon.com')
                speak('done')
                
            elif 'open daraz' in self.query:
                speak('opening daraz')
                webbrowser.open('www.daraz.com')
                speak('done')
                
            elif 'open instagram' in self.query:
                speak('opening instagram')
                webbrowser.open('www.instagram.com')
                speak('done')

            elif 'open subnautica' in self.query:
                subnauticapath = 'C:\\Users\\awais ahsan\\Desktop\\Subnautica' 
                speak('ok sir opening subnautica')
                os.startfile(subnauticapath)

            elif 'hello' in self.query:
                speak('hello sir')

            elif 'hello by the way' in self.query:
                speak('oh, hello sir')
        
            elif 'is my system fully operational' in self.query:
                speak('yes sir your system is fully operational')

            elif 'tell me my compuyour computer password is, wait first i have to scan your face password' in self.query:
                speak("your computer password is, wait first i have to scan your face")
                self.myface
                speak('Face Recognition Successful your password is 1454')
            
            elif 'open emergency mode' in self.query:
                speak('ok sir, but first i have to scan your face')
                self.myface()
                speak("opening emergence mode")
                speak("all securitys are down")
                speak("all teminats are down")
                speak("your location is now available everywere")
                speak("all trackers are online")
                speak("i am exiting in emergence mode")
                sys.exit()

            elif 'i need to download a game' in self.query:
                webbrowser.open("https://steamunlocked.net/")
                speak("ok sir opening a website for you")

            elif 'how are you jarvis' in self.query:
                speak('i am fine sir, what about you')

            elif 'i am fine' in self.query:
                speak('thats good to you, so whats are new plans for today')

            elif 'google search' in self.query:
                ('ok sir this is what i found on your search')
                self.query = self.query.replace("google search", "")
                youweb = 'https://www.google.com/search?q=' + self.query
                webbrowser.open(youweb)
                speak("Done Sir!")
            
            elif 'youtube search' in self.query:
                speak('ok sir , this is what i found on you search')
                self.query = self.query.replace("Jarvis", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                speak("done sir")

            elif 'what are you doing' in self.query:
                speak('just waiting for your commands sir')

            elif 'just' in self.query:
                speak('ok sir let me know if you have any help')

            elif 'send message' in self.query:
                kit.sendwhatmsg("+923346077165", "this is a message from jarvis for test do not reply",00,00)

            elif 'play a song on youtube' in self.query:
                speak('what song should i play on youtube')
                s = self.takecommand()
                kit.playonyt(s)   
            
    def hotwords(self):
        permission = self.takecommand()
        if permission == ("wake up"):
            self.TaskExecution()

    def myface(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


        id = 2 #number of persons you want to Recognize


        names = ['','MasterAwais']  #names, leave first empty bcz counter starts from 0


        cam = cv2.VideoCapture(1, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight

        speak('scanning face')

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        # flag = True

        while True:

            ret, img =cam.read() #read the frames using the above created object

            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 

                if (accuracy < 70):
                    id = names[id]
                    accuracy = "  {0}%".format(round(70 - accuracy))
                    cv2.destroyAllWindows()
                    self.TaskExecution()

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    speak('sir you are not my master')
                    p.press("Esc")
                    self.close()

                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  

            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows()

startExecution = MainThread()

class Face(QMainWindow):     
        def __init__(self):
                super().__init__()
                self.ui = Ui_LoadingNew()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.startTask)
                self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
                self.ui.movie = QtGui.QMovie("../../Downloads/ForsakenImpoliteIaerismetalmark-size_restricted.gif")
                self.ui.label.setMovie(self.ui.movie)
                self.ui.movie.start()
                startExecution.start()
                Main()

class Main(QMainWindow):     
        def __init__(self):
                super().__init__()
                self.ui = Ui_JARVIS()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.startTask)
                self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
                self.ui.movie = QtGui.QMovie("../../Downloads/f889323d87ae92dbd5da3b1193708dc3.gif")
                self.ui.ironman.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie = QtGui.QMovie("../../Downloads/preview.gif")
                self.ui.circle2.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie = QtGui.QMovie("../../Downloads/FreshAnyHanumanmonkey-size_restricted (1).gif")
                self.ui.circle.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie = QtGui.QMovie("../../Downloads/T8bahf (1).gif")
                self.ui.loading.setMovie(self.ui.movie)
                self.ui.movie.start()
                timer = QTimer(self)
                timer.timeout.connect(self.showTime)
                timer.start(1000)
                startExecution.start()

        def showTime(self):
                current_time = QTime.currentTime()
                current_date = QDate.currentDate()
                label_time = current_time.toString("hh:mm:ss")
                label_date = current_date.toString(Qt.ISODate)
                self.ui.textBrowser_1.setText(label_time)
                self.ui.textBrowser_2.setText(label_date)
                self.ui.textBrowser_3.setText("Pakistan")
                self.ui.textBrowser_4.setText("Multan")
                self.ui.textBrowser_5.setText("JARVIS")
                self.ui.textBrowser_6.setText("Made By Awais Siddique")

class Location(QMainWindow):     
        def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.startTask)
                self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
                self.ui.movie = QtGui.QMovie("../../Downloads/BitesizedUnfortunateDonkey-size_restricted.gif")
                self.ui.label_2.setMovie(self.ui.movie)
                self.ui.movie.start()
                startExecution.start()

app = QApplication(sys.argv)
#jarvis = Face()
#jarvis.show()
jarvis = Main()
jarvis.show()
#jarvis = Location()
#jarvis.show()
exit(app.exec_())



