import speech_recognition as sr
import pyttsx3
import requests
import time

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def set_reminder(reminder, delay_seconds):
    time.sleep(delay_seconds)
    speak(f"Reminder: {reminder}")

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_report = (f"Weather in {city}:\n"
                          f"Temperature: {temperature}°C\n"
                          f"Humidity: {humidity}%\n"
                          f"Description: {weather_desc}")
        return weather_report
    else:
        return "City not found."

def get_news():
    api_key = "your_newsapi_api_key"
    base_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(base_url)
    articles = response.json()["articles"]
    news = []
    for article in articles[:5]:
        news.append(article["title"])
    return "\n".join(news)

def main():
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()

        if "reminder" in command:
            speak("What should I remind you about?")
            reminder = listen()
            speak("In how many seconds should I remind you?")
            delay = int(listen())
            speak(f"Setting a reminder for {reminder} in {delay} seconds.")
            set_reminder(reminder, delay)
        
        elif "weather" in command:
            speak("Please tell me the city.")
            city = listen()
            weather_report = get_weather(city)
            speak(weather_report)
        
        elif "news" in command:
            news_report = get_news()
            speak("Here are the top news headlines.")
            speak(news_report)
        
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
