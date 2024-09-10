import streamlit as st
import speech_recognition as sr
from datetime import datetime
from googletrans import Translator
import pytz

# Initialize translator
translator = Translator()

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to check if it's after 6 PM IST
def is_after_six_pm():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).time()
    six_pm = current_time.replace(hour=18, minute=0, second=0, microsecond=0)
    return current_time >= six_pm

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
            return None

# Streamlit GUI
st.title("English to Hindi Audio Translation")

if is_after_six_pm():
    st.write("Please press the button and start speaking in English.")
    if st.button("Start Listening"):
        english_text = recognize_speech()
        if english_text:
            hindi_translation = translator.translate(english_text, dest='hi').text
            st.write(f"Translation in Hindi: {hindi_translation}")
else:
    st.write("This translation service is available only after 6 PM IST.")
