import speech_recognition as sr
import pyttsx3
import datetime
import pyowm

recognizer = sr.Recognizer()
engine = pyttsx3.init()
owm = pyowm.OWM('your-owm-api-key')  # Replace 'your-owm-api-key' with your actual API key

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error during speech recognition: {e}")

    return None

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # 12-hour format
    return current_time

def get_date():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return current_date

def get_weather():
    observation = owm.weather_at_place('city, country')  # Replace 'city, country' with your location
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    status = weather.get_detailed_status()
    return f"The weather today is {status} with a temperature of {temperature} degrees Celsius."

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I assist you today?")

    while True:
        command = listen()
        
        if command is not None:
            if "hello" in command.lower():
                speak("Hello there!")
            elif "how are you" in command.lower():
                speak("I'm fine, thank you!")
            elif "time" in command.lower():
                current_time = get_time()
                speak(f"The current time is {current_time}")
            elif "date" in command.lower():
                current_date = get_date()
                speak(f"Today is {current_date}")
            elif "weather" in command.lower():
                current_weather = get_weather()
                speak(current_weather)
            elif "goodbye" in command.lower():
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")
