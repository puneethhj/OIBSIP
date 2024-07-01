import speech_recognition as sr
import pyttsx3
import smtplib
import requests
from datetime import datetime
import json
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set up the lemmatizer for NLP
lemmatizer = WordNetLemmatizer()

# Function to speak text
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to recognize speech and convert it to text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return ""

# Function to send email
def send_email(recipient_email, subject, message):
    sender_email = "youremail@example.com"
    sender_password = "yourpassword"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        speak("Email has been sent successfully.")
    except Exception as e:
        speak("Failed to send email. Please check the configuration.")
        print(e)

# Function to set a reminder
def set_reminder(time, message):
    # For demonstration, we'll simply print the reminder details
    speak(f"Reminder set for {time}: {message}")

# Function to get weather updates
def get_weather(city):
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        speak(f"The weather in {city} is {weather_desc} with a temperature of {temp - 273.15}°C.")
    else:
        speak("City Not Found")

# Function to control smart home devices (stub function for demo)
def control_smart_home(command):
    speak(f"Executing smart home command: {command}")

# Function to answer general knowledge questions
def answer_question(query):
    # For simplicity, we'll use a predefined set of answers
    answers = {
        "what is the capital of France": "The capital of France is Paris.",
        "who is the president of the United States": "As of now, the president of the United States is Joe Biden."
    }
    response = answers.get(query.lower(), "I'm sorry, I don't know the answer to that question.")
    speak(response)

# Main function to process commands
def process_command(command):
    tokens = word_tokenize(command)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    if "email" in lemmatized_tokens:
        speak("Who is the recipient?")
        recipient = recognize_speech()
        speak("What is the subject?")
        subject = recognize_speech()
        speak("What is the message?")
        message = recognize_speech()
        send_email(recipient, subject, message)
    elif "reminder" in lemmatized_tokens:
        speak("What time should I set the reminder for?")
        time = recognize_speech()
        speak("What is the reminder?")
        message = recognize_speech()
        set_reminder(time, message)
    elif "weather" in lemmatized_tokens:
        speak("Which city?")
        city = recognize_speech()
        get_weather(city)
    elif "turn on" in lemmatized_tokens or "turn off" in lemmatized_tokens:
        control_smart_home(command)
    else:
        answer_question(command)

# Main loop
def main():
    speak("Hello, how can I help you today?")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)
        speak("Do you need anything else?")

if __name__ == "__main__":
    main()
