from json import load
import operator
from http import server
from pickle import NONE
from re import U
import sys
from bs4 import BeautifulSoup
import instaloader
import requests
import pyttsx3
import datetime
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import pyjokes
import time
import pyautogui
from bot.twitterbot import tweet_func
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pywikihow import search_wikihow
from dotenv import load_dotenv
from karenUi import Ui_KarenUi

load_dotenv()

import webbrowser
chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register("chrome",NONE, webbrowser.BackgroundBrowser(chrome_path))
browser = webbrowser.get('chrome')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('peraltajake884@gmail.com','#hritik@2001')
    server.sendmail('peraltajake884@gmail.com', to, content)
    server.close()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    ct = time.strftime("%I:%M %p")
    speak("It's "+ct)
    speak("I am Karen. How may I help you?")
    
def news():
        news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b319e72baf5542689a5cb4f9e1f384cf"
        main_page = requests.get(news_url).json()
        news_num = ["first", "second", "third", "fourth", "fifth"]
        articles = main_page["articles"]
        head = []
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(news_num)):
            speak(f"todays {news_num[i]} news is: {head[i]}")
    
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.karen()
        while True:
            permission = self.takecommand()
            if "wake up" in permission:
                self.karen()
            elif "exit" in permission:
                sys.exit()
           
        
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, 1, 5)
            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
        except Exception as e:
            #speak("Please say that again...")
            return 'none'
        return query
        
    def karen(self):
        wishMe()
        while True:
            self.query = self.takecommand().lower()
            
            if "how are you" in self.query:
                speak("I am fine. How are you?")
                
            if "i am fine" in self.query:
                speak("That's great. How can I help you?")
            
            if "open notepad" in self.query:
                nppath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(nppath)
                
            elif "close notepad" in self.query:
                speak('closing notepad')
                os.system("taskkill /f /im notepad.exe")
                
            elif "thank you" in self.query or "thanks" in self.query:
                speak("You are welcome!")
                
            elif "open command prompt" in self.query:
                os.system("start cmd")
                
            elif "close command prompt" in self.query:
                speak("closing command prompt")
                os.system("taskkill /f /im cmd.exe")
                
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, frame = cap.read()
                    cv2.imshow("cam", frame)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
                
            elif "play music" in self.query:
                music_dir = "C:\\Users\\Hritik\\Music"
                songs = os.listdir(music_dir)
                #rdmsong = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,song))
                
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            
            elif "wikipedia" in self.query:
                speak("Searching in wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences= 3)
                speak("According to wikipedia")
                speak(results)
                print(results)
                    
            elif "open youtube" in self.query:
                browser.open("youtube.com")
                
            elif "close youtube" in self.query:
                speak("closing youtube")
                os.system("taskkill /f /im chrome.exe")
                
            elif "open facebook" in self.query:
                browser.open('facebook.com')
                
            elif "close facebook" in self.query:
                speak("closing facebook")
                os.system("taskkill /f /im chrome.exe")
                
            elif "open stackoverflow" in self.query:
                browser.open('stackoverflow.com')
                
            elif "close stackoverflow" in self.query:
                speak("closing stackoverflow")
                os.system("taskkill /f /im chrome.exe")
                
            elif "open whatsapp" in self.query:
                browser.open('web.whatsapp.com')
            
            elif "close whatsapp" in self.query:
                speak("closing whatsapp")
                os.system("taskkill /f /im chrome.exe")
                
            elif "open google" in self.query:
                speak("What you want to search in google?")
                search = self.takecommand().lower()
                browser.open(f'{search}')
                
            elif "close youtube" in self.query:
                speak("closing whatsapp")
                os.system("taskkill /f /im chrome.exe")
                
            elif "play song on youtube" in self.query:
                speak("Which song you want to play?")
                sname = self.takecommand()
                kit.playonyt(sname)
                
            elif "send email" in self.query:
                try:
                    speak("What you want to say?")
                    content = self.takecommand()
                    to = "raijinhritik@gmail.com"
                    sendEmail(to, content)
                except Exception as e:
                    print(e)
                    
            elif "alarm" in self.query:
                speak("Tell me alarm time")
                try:
                    t = self.takecommand()
                    t = t.replace(".","")
                    t = t.upper()
                    import MyAlarm
                    MyAlarm.alarm(t)
                except Exception as e:
                    speak("Could not recognize time")
                    
            elif "Tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
                
            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
                
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
                
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    
            elif "switch the window" in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
                
            elif "tell me the news" in self.query or "tell me news" in self.query:
                speak("Fetching the news. Please wait...")
                news()
            
            elif "twitter" in self.query:
                speak("What do you want to tweet")
                tweet = self.takecommand().lower()
                speak("Please wait. Tweeting...")
                tweet_func(tweet)
                
            elif "where am i" in self.query or "where are we" in self.query:
                speak("let me check our location...")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    region = geo_data['region']
                    country = geo_data['country']
                    speak(f"We are in {city} city of {region} state of {country}")
                except Exception as e:
                    speak("Due to network issues location can't be checked")
                    pass
            
            elif "check a profile on instagram" in self.query or "search for a profile on instagram" in self.query or "instagram profile" in self.query:
                speak("Sir, please enter username correctly")
                usname = input("Enter the username here: ")
                browser.open("instagram.com/"+usname)
                speak("Here is the profile of user "+usname)
                time.sleep(5)
                speak("Do you want to download the profile picture")
                answer = self.takecommand().lower()
                if "yes" in answer:
                    mod = instaloader.Instaloader()
                    mod.download_profile(usname,profile_pic_only=True )
                    speak("Download complete. Picture is saved in main folder")
                else:
                    pass
                
            elif "take screenshot" in self.query or "take a screenshot" in self.query or "take ss" in self.query:
                speak("Give a name for screenshot")
                name = self.takecommand().lower()
                speak("Please hold the screen for some time. Taking screenshot...")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Screenshot taken")
            
            elif "read pdf" in self.query:
                speak("Please give the complete path of the pdf")
                pdf_path = input("Enter the path:")
                book = open(pdf_path,'rb')
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.numPages
                speak(f"This pdf has {pages} pages")
                speak("Please enter the page number you want me to read")
                pn = int(input("Enter page number: "))-1
                page = pdfReader.getPage(pn)
                text = page.extractText()
                speak(text)
                
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("Please tell me if you want to hide or make this folder visible")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("All the files in this folder are hidden")
                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("All files are now visible")
                elif "leave it" in condition or "leave it for now" in self.query:
                    speak("Ok sir")
            
            elif "do some calculations" in self.query or "do some calculation" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What you want to calculate? example 1 plus 1")
                    print("Listening...")
                    try:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    except Exception as e:
                        print(e)
                my_string = r.recognize_google(audio)
                print(my_string)
                def operator_fn(op):
                    return {
                        '+' : operator.add, #plus
                        '-' : operator.sub, #minus
                        'x' : operator.mul, #multiplied by
                        'divided': operator.__truediv__, #divided
                    }[op]
                try:
                    def eval_bin_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return operator_fn(oper)(op1,op2)
                    speak("Result is ")
                    speak(eval_bin_expr(*(my_string.split())))
                except Exception as e:
                    speak("oops! Calculation was not recognized properly")
                
                
            elif "temperature" in self.query:
                speak("Which city temperature you want?")
                city = self.takecommand()
                url = f"https://www.google.com/search?q=temperature in {city}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current temperature in {city} is {temp}")
                
            elif "activate how to do mod" in self.query:
                speak("How to do mode is activated.")
                while True:
                    speak("What you want to know?")
                    search = self.takecommand()
                    try:
                        if "deactivate how to do mod" in search:
                            speak("Closing how to do mode")
                            break
                        else:
                            maxRes = 1
                            howTo = search_wikihow(search, maxRes)
                            assert len(howTo) == 1
                            howTo[0].print()
                            speak(howTo[0].summary)
                    except Exception as e:
                        speak("Sorry search failed")
                        
            elif "how much battery is remaining" in self.query or "how much power is left" in self.query or "tell me battery percentage" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percent = battery.percent
                speak(f"We have {percent} percent battery left")
                if percent >= 75:
                    speak("We can work without plugging the charger")
                elif percent < 75 and percent >= 40:
                    speak("It is recommended to plug in charger")
                elif percent < 40 and percent >= 20:
                    speak("Battery is low. Please connect the charger")
                elif percent < 20:
                    speak("Battery is crictically low. Please connect the charger or pc may shut down.")
                
            elif "internet speed" in self.query:
                speak("Checking internet speed. Please wait...")
                import speedtest
                s = speedtest.Speedtest()
                ds = round(s.download()/8000000)
                us = round(s.upload()/8000000)
                speak(f"We have {ds} megabytes per second download speed and {us} megabytes per second upload speed")
                
            elif "send message" in self.query:
                speak("What is the message?")
                msg = self.takecommand()
                from twilio.rest import Client
                account_sid = os.getenv('TWILIO_ACC_SID')
                auth_token = os.getenv('TWILIO_AUTH_TOKEN')
                client = Client(account_sid, auth_token)
                message = client.messages\
                    .create(
                        body = msg,
                        from_='+18597626533',
                        to='+919325336372'
                    ) 
                print(message.sid)
                speak("Message has been sent") 
                
            elif "call" in self.query:
                from twilio.rest import Client
                account_sid = os.getenv('TWILIO_ACC_SID')
                auth_token = os.getenv('TWILIO_AUTH_TOKEN')
                client = Client(account_sid, auth_token)
                message = client.calls.create(
                    twiml='<Response><Say>This is testing message from karen...</Say></Response>',
                    from_='+18597626533',
                    to='+919325336372'
                )
                print(message.sid)
                
            elif "open mobile camera" in self.query:
                import urllib.request
                import cv2
                import numpy as np
                import time
                url = "http://192.168.167.44:8080/shot.jpg"
                while True:
                    imgArr = np.array(bytearray(urllib.request.urlopen(url).read()),dtype=np.uint8)
                    img = cv2.imdecode(imgArr, -1)
                    cv2.imshow('WebCam', img)
                    q = cv2.waitKey()
                    if q == ord('q'):
                        break
                    cv2.destroyAllWindows()
                
            elif "increase volume" in self.query or "volume up" in self.query:
                pyautogui.press("volumeup")
                
            elif "decrease volume" in self.query or "volume down" in self.query:
                pyautogui.press("volumedown")
                
            elif "mute" in self.query:
                pyautogui.press("volumemute")
            
            elif "you can sleep" in self.query or "sleep" in self.query or "sleep now" in self.query:
                speak("Going to sleep now. You can wake me up any time.")
                break
            
            elif "exit" in self.query:
                sys.exit()
    
startExecution = MainThread()
    
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_KarenUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("run.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("tl.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("plexus___3.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        
app = QApplication(sys.argv)
karen = Main()
karen.show()
exit(app.exec_())