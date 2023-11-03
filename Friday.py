import sys
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import winshell
import pywhatkit as kit
from pytube import YouTube
from requests import get
import wikipedia
import webbrowser
import subprocess
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import webbrowser
import os
import json
import pyjokes
import ctypes
import time
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets  import *
from PyQt5.uic import loadUiType
from FRIDAY_GUI_1 import Ui_FRIDAY 
import wolframalpha
import smtplib
import win32com.client as wincl
from urllib.request import urlopen

# Computational Intelligence
try:
    wolfra = wolframalpha.Client("A522QE-E3RPAAJHE8")
except Exception as e:
    print("Wolframalpha is not working!")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("tombriddle28@gmail.com", "voldemort123@")
    server.sendmail('tombriddle28@gmail.com', to, content)
    server.close()

class location:  
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    ip = data['ip']
    city = data['city']
    region = data['region']
    country = data['country']
    org = data['org']
    postal = data['postal']
    timezone = data['timezone']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

current_state = "wait..."

class MainThread(QThread):
    def __init__(self) -> None:
        super(MainThread, self).__init__()
    
    def run(self):
        self.main()
    
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        tt = time.strftime("%I:%M %p")
        if hour >= 0 and hour < 12:
            speak(f"Good Morning sir!,its {tt}  ")

        elif hour >= 12 and hour < 17:
            speak(f"Good Afternoon sir! its  {tt} ")

        else:
            speak(f"Good Evening sir! its {tt} ")

        speak("Good to see you again")
        speak("How may I help you")
        
           
    def takecommand(self):
        global current_state
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            current_state = "listening....."
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)

        try:
            current_state = "Recognizing..." 
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception:
            return "none"
        return query

    def main(self):
        if __name__ == "__main__":
            clear = lambda: os.system('cls')
            clear()
            self.wishMe()

            while (True):

                self.query = self.takecommand().lower()
                local = location

                # Aplications to run

                if "open notepad" in self.query:
                    speak("openning notepad sir")
                    path = "C:\\Windows\\system32\\notepad.exe"
                    os.startfile(path)

                elif "open arduino" in self.query:
                    speak("openning arduino sir")
                    path = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
                    os.startfile(path)

                elif "open command prompt" in self.query:
                    speak("openning command prompt sir")
                    os.system("start cmd")
                    
                elif "open pycharm" in self.query:
                    speak("openning pycharm sir")
                    path = "D:\\blog post's\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
                    os.startfile(path)

                        
                        
                elif "password" in self.query or "passwords" in self.query:
                    speak("Extracting Wifi Passwords")
                    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
                    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                    for i in profiles:
                        try:
                            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
                                                'key=clear']).decode('utf-8').split('\n')
                            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                            speak ("{:<30}| password is {:<}".format(i, results[0]))
                        except Exception as e:
                            e

                elif "wifi" in self.query:
                    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
                    wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
                    for signal in wifis:
                        speak(signal)
 
                #  Play Music
                elif "play music" in self.query or "friday play the music" in self.query or "play the music" in self.query or "friday play music" in self.query:
                    speak("Yeah sure but what you want to listen sir?")
                    pp = self.takecommand().lower()
                    kit.playonyt(pp)


                # Operations
                elif "What" in self.query:
                    speak("searching sir....")
                    res = wolfra.query(self.query)
                    answer = next(res.results).text
                    speak(answer)


                elif "where am i" in self.query or "location" in self.query or "where i am" in self.query:
                    speak("let me find sir")
                    speak(f"I guess sir we are in {local.city} city in {local.country}")
                    speak("Should i find more details")
                    tt = self.takecommand().lower()
                    if "yes" in tt or "yep" in tt or "yeah" in tt:
                        print("Latitude : ", local.latitude)
                        print("Longitude : ", local.longitude)
                        print("IP : ", local.ip)
                        print("City : ", local.city)
                        print("Region : ", local.region)
                        print("Country : ", local.country)
                        print("Org : ", local.org)
                        print("Postal : ", local.postal)
                        print("Timezone : ",local.timezone)


                elif "time" in self.query:
                    timee = time.strftime("%I:%M %p")
                    speak(f"Sir its {timee}")
                    

                elif 'exit' in self.query or 'quit' in self.query  or "abort" in self.query or "bye" in self.query:
                    speak("If you need something else just let me know sir")
                    speak("program terminating")
                    self.exit()
                    exit()

                elif 'joke' in self.query:
                    speak(pyjokes.get_joke())
            
                    
                elif "who made you" in self.query or "who created you" in self.query:
                    speak("I was created as a Minor project by Mister Ayush in 2019,, as a personal assistant")
                
                elif 'is love' in self.query:
                    speak("It is 7th sense that destroy all other senses")

                elif "who are you" in self.query or "about you" in self.query or "details" in self.query:
                    speak("I am personal assistant of Mister, Ayush")

                elif "like" in self.query or "felling" in self.query:
                    speak("i am feeling very good after meeting you")

                elif "say hi " in self.query:
                    spk = "sir whom should i say hi"
                    speak(spk)
                    shi = self.takecommand().lower()
                    speak(f"hi {shi} its nice to meet you , My name is Friday 2.0, and  I am a  program ")

                elif "restart" in self.query:
                    subprocess.call(["shutdown", "/r"])
                    
                elif "hibernate" in self.query or "sleep" in self.query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")

                elif "log off" in self.query or "sign out" in self.query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    subprocess.call(["shutdown", "/l"])

                elif "notifications" in self.query or "notification" in self.query:
                    speak("No Sir, It seems you are up to date")
                   
                elif "light" in self.query:
                    speak("Turning on light sir")    

                elif "write a note" in self.query:
                    speak("What should i write, sir")
                    note = self.takecommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = self.takecommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime =time.strftime("%I:%M %p")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                
                elif "show note" in self.query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    for lines in file:
                        speak(lines)

                elif 'lock window' in self.query:
                        speak("locking the device")
                        ctypes.windll.user32.LockWorkStation()

                elif 'shutdown' in self.query:
                        speak("Hold On a Sec ! Your system is on its way to shut down")
                        subprocess.call('shutdown / p /f')
                        
                
                        
                elif 'empty recycle bin' in self.query or 'empty recyclebin' in self.query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")

                # Whatsapp message
                elif "message prabhat" in self.query :
                    speak("sir what should I say?")
                    pk3 = self.takecommand()

                    hour = int(datetime.datetime.now().hour)
                    tt = time.strftime("%I:%M %p")
                    hourAA = tt[:-6]
                    minA = tt[3:]
                    minAA = minA[:-3]
                    print(
                        f"tt = {tt}",
                        f"hour = {hour}",
                        f"hourAA = {hourAA}",
                        f"minA = {minA}",
                        f"minAA = {minAA}",
                        )
                    kit.sendwhatmsg("+918127051202", f" {pk3} ",int(f"{hourAA}"),int(int(f"{minAA}") + 1))
                    speak("sending message! to prabhat")


                # Email's
                elif "send email to Ayush singh" in self.query or "send mail to Ayush singh" in self.query:
                    try:
                        speak("What should I say?")
                        see = self.takecommand().lower()
                        to = "littledemon110901@gmail.com"
                        sendEmail(to, see)
                        speak("Sir email has been sent to", to)
                    except Exception as e:
                        print(e)
                        speak("sorry sir i am unable to send email")

                # Closing Tags
                elif "close Notepad" in self.query:
                    speak("okay sir,Closing notepad")
                    os.system("taskkill /f /im notepad.exe")

                elif "close command prompt" in self.query:
                    speak("okay sir,Closing notepad")
                    os.system("taskkill /f /im command prompt.exe")


                elif "close arduino" in self.query:
                    speak("okay sir,Closing notepad")
                    os.system("taskkill /f /im arduino.exe")


                elif "close pycharm" in self.query:
                    speak("okay sir,Closing notepad")
                    os.system("taskkill /f /im pycharm64.exe")




                elif "don't listen" in self.query or "stop listening" in self.query:
                    speak("for how much time in seconds you want me to  stop listening")
                    try:
                        a = int(self.takecommand())
                        time.sleep(a)
                        print(a)
                    except Exception as e:
                        print("Give time in seconds eg-> 10")

                elif "good morning" in self.query:
                    speak("A warm morning sir")
                    speak("How are you")
                    
                elif "friday" in self.query:
                    speak("Yeah Sir")
                    speak("What can i do for you")
                
                elif " i am fine" in self.query or "i am good" in self.query or "great" in self.query:
                    speak("its good to see you again sir . how may i help you")


                elif "will you be my gf" in self.query:  
                    speak("I'm not sure about that, may be you should give me some time")

                elif "what's up" in self.query or "how are you" in self.query or "whatsapp friday" in self.query :
                    prmsg = ["just doing my thing sir !, how are you sir?", "i am fine!, what's about you? ",
                            "i am doing good sir!, how are you?", "i am okay sir!, how are you?"]
                    ans = random.choice(prmsg)
                    speak(ans)

                elif "i love you" in self.query:
                    speak("not more than i do")
                
                elif "calculate" in self.query:
                    
                    try:           
                        indx = self.query.lower().split().index('calculate')
                        self.query = self.query.split()[indx + 1:]
                        res = wolfra.query(' '.join(self.query))
                        answer = next(res.results).text
                        speak("The answer is " + answer)
                    except Exception as e:
                        print(" Sorry can't understand try again")
                    
                        
                elif "temperature" in self.query:
                    try:
                        res = wolfra.query(self.query)
                        speak(next(res.results).text)
                    except Exception as e:
                        print("Something is wrong")
                        
                        
                elif "youtube" in self.query:
                    webbrowser.open_new_tab("www.youtube.com")

                
                elif "instagram" in self.query:
                    speak("sure sir")
                    webbrowser.open_new_tab("www.instagram.com")

                elif "google" in self.query:
                    speak("sir, what should i search on google")
                    num = self.takecommand().lower()
                    webbrowser.open_new_tab(f"{num}")

                elif "stackoverflow" in self.query or "stack overflow" in self.query:
                    webbrowser.open_new_tab("www.stackoverflow.com")
                    

                elif "blogger" in self.query:
                    webbrowser.open_new_tab("www.blogger.com")

                elif "play" in self.query:
                    speak("yeah sure sir")
                    self.query = self.query.replace("youtube", "")
                    kit.playonyt(self.query)
                
                elif 'news' in self.query:             
                    try:
                        jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=44f5b481da124269bcef6d41e51a3061''')
                        data = json.load(jsonObj)
                        i = 1
                        
                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============'''+ '\n')
                        
                        for item in data['articles']:                     
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:
                        print(str(e))
                            
                
                elif "ip" in self.query:
                    ip = get('https://api.ipify.org').text
                    speak(f"Your IP address is {ip}")

                elif self.query == "none":
                    continue


Execution = MainThread() 


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FRIDAY()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis_gui/2RNb.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("Jarvis_gui/download.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("Jarvis_gui/NearEnlightenedBushbaby-size_restricted.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        
        timer = QTimer(self)
        self.res = wolfra.query("temprature in Kanpur")
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        Execution.start()
        
    def showTime(self):
        current_time = time.strftime("%I:%M:%S  %p")
        current_date = datetime.datetime.now()
        label_Date = current_date.strftime("%d-%b-%Y")
        label_whether = str(next(self.res.results).text[0:5])
        day = current_date.strftime("%A")
        self.ui.textBrowser.setText(current_time)
        self.ui.textBrowser.setAlignment(Qt.AlignCenter)
        self.ui.textBrowser_2.setText(label_Date)
        self.ui.textBrowser_2.setAlignment(Qt.AlignCenter)
        self.ui.textBrowser_3.setText(f"{label_whether}  {day}")
        self.ui.textBrowser_3.setAlignment(Qt.AlignCenter)
        self.ui.textBrowser_4.setText(current_state)
        self.ui.textBrowser_4.setAlignment(Qt.AlignCenter)
        
        

app = QApplication(sys.argv)
Friday = Main()
Friday.show()
exit(app.exec_())