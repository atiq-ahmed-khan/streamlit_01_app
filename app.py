import streamlit as st
import numpy as np
import pandas as pd
from gtts import gTTS 
import os
import speech_recognition as sr

# Title of the app
st.title("My First Streamlit Application")

# Display text
st.write("Hello, welcome to the Streamlit app!")

# Text input
user_input = st.text_input("Enter some text:")
if user_input:  
    st.write(f"You entered: {user_input}")

# Slider to select the number of points
num_points = st.slider("Select the number of points to display:", 10, 200, 50)

# Generate random chart data based on the selected number of points
chart_data = pd.DataFrame(
    np.random.randn(num_points, 2), 
    columns=["X", "Y"]
)

# Display the line chart
st.line_chart(chart_data)

#Text to Speech 
st.title("Text-to-Speech App 🎤")

text = st.text_input("Enter text to convert into speech:")

if st.button("Speak"):
    if text:
        tts = gTTS(text=text, lang="en")  # Convert text to speech
        tts.save("speech.mp3")  # Save audio file
        st.audio("speech.mp3", format="audio/mp3")  # Play audio in Streamlit
    else:
        st.warning("Please enter some text!")

#Speech to text
st.title("Speech-to-Text App 🎙️")

recognizer = sr.Recognizer()

if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.info("Listening... Speak Now!")
        audio = recognizer.listen(source)  # Record user's voice
        
        try:
            text = recognizer.recognize_google(audio)  # Convert to text
            st.success(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio!")
        except sr.RequestError:
            st.error("Could not request results, check your internet connection!")

