import datetime
import os
import smtplib
import webbrowser as wb

import pyautogui
import psutil
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = "user-name@xyz.com"
EMAIL_PASSWORD = "pwd"
SCREENSHOT_PATH = "C:\\Users\\226898\\Pictures\\Screenshots\\ss.png"
MUSIC_DIR = "C://Music"
WEATHER_API_KEY = "2b840a555ccef7ae830adfe3ba2c2ac2"
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
VOICE_RATE = 180
MAX_VOLUME = 10
KELVIN_TO_CELSIUS_OFFSET = 273.15

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', MAX_VOLUME)


def voice_change(voice_index) -> None:
    """Change the voice of the text-to-speech engine."""
    engine.setProperty('voice', voices[voice_index].id)
    speak("Voice has been changed sir")


def speak(audio) -> None:
    """Speak the given audio string."""
    engine.say(audio)
    engine.runAndWait()


def get_time() -> None:
    """Get and speak the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("sir, right now time is ")
    speak(current_time)


def get_date() -> None:
    """Get and speak the current date."""
    current_year = int(datetime.datetime.now().year)
    current_month = int(datetime.datetime.now().month)
    current_date = int(datetime.datetime.now().day)
    speak("sir, Today is")
    speak(current_date)
    speak(current_month)
    speak(current_year)


def check_time(time_of_day) -> None:
    """Check the time of day and greet accordingly."""
    hour = datetime.datetime.now().hour
    if ("morning" in time_of_day):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir, how are you feeling this morning?")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in time_of_day):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir, dont go to bed, late, sir it"\
                      "affects your daily sleep cycle, causing daily"\
                      "mood swings, with stress and anxiety")
    else:
        speak("it's night sir!, you should probably get some sleep")


def wish_me() -> None:
    """Greet the user and acknowledge that the assistant is online."""
    speak("Welcome Back sir")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning ")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon ")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening ")
    else:
        speak("Goodnight sir")

    speak("I have indeed been uploaded , i am online and ready sir, How can"\
          "i help you today?")


def wish_me_end() -> None:
    """Greet the user and shut down the assistant."""
    speak("alright i am going to sleep now sir, wake me up if you need"\
          "anything")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Get some sleep sir! We got a lot to do tomorrow.")
    quit()


def take_command() -> str:
    """Listen to the user's command and return it as a string."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        speak("vocal authorization complete, identity confirmed")
        user_command = recognizer.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        speak("sir, i am having difficulty hearing you, can you please speak"\
              "up?...")

        return "None"

    return user_command


def send_email(to, content) -> None:
    """Send an email to the specified address with the given content."""
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to, content)
    server.close()


def take_screenshot() -> None:
    """Capture a screenshot and save it to the specified location."""
    screenshot_image = pyautogui.screenshot()
    screenshot_image.save(SCREENSHOT_PATH)


def get_cpu() -> None:
    """Get and speak the current CPU usage and battery status."""
    usage = str(psutil.cpu_percent())
    speak('current CPU status of your system is ' + usage +
          "sir, dont let too many unnecessary background processes run at"\
          "the same time, for the system to perform operation smoothly, and"\
          "you can work efficiently on this system")
    print('current CPU status of your system is ' + usage +
          "sir, dont let too many unnecessary background processes run at"\
          "the same time, for the system to perform operation smoothly, and"\
          "you can work efficiently on this system")
    battery = psutil.sensors_battery()
    speak("Your battery usage currently is at")
    speak(battery.percent)
    print("Your system is running at:" + str(battery.percent) +
          " battery power, sir. always provide regular power supply to the"\
          "system")


def tell_jokes() -> None:
    """Tell a joke to the user."""
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
    speak("was it a good joke, sir?")


def get_weather() -> None:
    """Get the weather information for a specified city and speak it."""
    speak("Of which city would you like to know the weather sir?")
    city_name = take_command()
    weather_api_url = (WEATHER_BASE_URL + "appid=" + WEATHER_API_KEY +
                       "&q=" + city_name)
    response = requests.get(weather_api_url)
    response_data = response.json()
    if response_data["cod"] != "404":
        weather_data = response_data["main"]
        current_temperature = weather_data["temp"]
        current_temp_celsius = current_temperature - KELVIN_TO_CELSIUS_OFFSET
        current_pressure = weather_data["pressure"]
        current_humidiy = weather_data["humidity"]
        weather_condition = response_data["weather"][0]["description"]
        weather_report = ("in " + city_name + "Current Temperature is " +
             str(int(current_temp_celsius)) + " degree celsius " +
             ", with atmospheric pressure of " + str(current_pressure) + 
             " hpa unit" + ", and humidity is  " + str(current_humidiy) + 
             " percent" " and " + str(weather_condition))
        print(weather_report)
        speak(weather_report)
    else:
        speak(" the city you are refering to, was not Found in our database"\
              "sir")


def tell_about_self() -> None:
    """Provide information about the assistant."""
    speak(
        " Hello, I am Cypher, version 1.8.7, I am a basic design of voice"\
        "assistant, a program without any form or physical presence, i only"\
        "exist in the lines of code, I was designed and developed, on 19"\
        "September 2022, by using a programming language called python with"\
        "the help of many imported modules, on a device named Dell Inspiron"\
        "15, with microsoft windows 64 bit operating system, consisting of"\
        "8 Giga bytes of Random access memory, intel core i 5 tenth"\
        "generation processor, 4 gigabytes n vidia m x two thirty of"\
        "graphics memory, and 2 gigabytes of intel integrated graphics, i"\
        "have a network database running in background for your service at"\
        "all time, as you can ask me anything, anytime, i will provide you"\
        "with the information you are looking for."
    )
    speak("Now i hope you know me well, i hope i will be of some help to you"\
          "in the future. Just take my name and i will be powered up and"\
          "ready for you sir")


if __name__ == "__main__":
    wish_me()
    while (True):
        query = take_command().lower()

        if ('time' in query):
            get_time()

        elif ('date' in query):
            get_date()

        elif ("tell me about yourself" in query):
            tell_about_self()
        elif ("about you" in query):
            tell_about_self()
        elif ("who are you" in query):
            tell_about_self()
        elif ("yourself" in query):
            tell_about_self()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

        elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content = take_command()
                send_email(EMAIL_ADDRESS, content)
                speak("sir, your Email has been sent")
            except Exception as e:
                print(e)
                speak(
                    "Unable to send email sir, check whether the address of"\
                    "the recipient is correct")
        elif ("search on google" in query or "open website" in query):
            speak("What would you like me to search on the web, sir?")
            chromepath = ('C:/ProgramData/Microsoft/Windows/Start Menu/'
                          'Programs/chrome.exe %s')
            search = take_command().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

        elif ("play songs" in query):
            speak("Alright...")
            songs = os.listdir(MUSIC_DIR)
            os.startfile(os.path.join(MUSIC_DIR, songs[1]))
            quit()

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What would you like me to remind you of sir?")
            data = take_command()
            speak("sir You told me to remind you of" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("sir you told me to remind you of " + reminder_file.read())

        elif ("screenshot" in query):
            take_screenshot()
            speak("i have captured and saved, what was on your screen sir"\
                  "right now")

        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            get_cpu()

        elif ("tell me a joke" in query or "joke" in query):
            tell_jokes()

        elif ("weather" in query or "temperature" in query):
            get_weather()

        elif ("tell me your features" in query or "powers" in query
             or "features" in query):
            features = (
            "I can help you with many things, such as:\n"
            "- Telling you the current time and date.\n"
            "- Providing weather updates for any city across the globe.\n"
            "- Showing the current CPU and battery usage.\n"
            "- Creating reminders, so you don't miss important tasks, "
            "meetings, or events.\n"
            "- Capturing and saving a screenshot of your screen.\n"
            "- Lightening your mood with a joke, although I can't guarantee "
            "you'll laugh.\n"
            "- Sending emails for you to your boss, family, or friends "
            "while you're busy.\n"
            "- Shutting down, logging out, or putting your system to sleep.\n"
            "- Opening websites for you.\n"
            "- Searching information on Wikipedia.\n"
            "- Changing my voice from male to female and vice versa.\n"
            "- My developer is working on adding more features.\n"
            "Now tell me, what can I do for you?"
            )
            print(features)
            speak(features)

        elif ("hi" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                check_time(query)
            else:
                speak("what can i do for you sir?")

        elif ("voice" in query):
            speak("if you want to change my voice to female or male, just"\
                  "say female, or, male, and i will change my voice for you")
            q = take_command()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

        elif ('i am done cypher' in query or 
              'bye cypher' in query or 
              'go offline cypher' in query or 
              'bye' in query or 
              'nothing' in query or 
              'go to sleep cypher' in query or 
              'sleep cypher' in query or 
              'shut down cypher' in query or 
              'thank you cypher you can go to sleep' in query or 
              'ok enough for today cypher, go to sleep' in query):
            wish_me_end()
 