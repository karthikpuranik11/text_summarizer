import numpy as np
import pandas as pd
import streamlit as st 
import joblib
import os
from moviepy.editor import *
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import transformers
from transformers import pipeline
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize
import re

from PIL import Image

def welcome():
    return "Welcome All"

def get_large_audio_transcription(path):  
    r = sr.Recognizer()
    sound = AudioSegment.from_wav(path)  
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence=500,
    )
    folder_name = ""
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                whole_text += text
    return whole_text
    
st.title("Summarize Text")
video = st.file_uploader("Choose a file", type=['mp4'])
button = st.button("Summarize")

max = st.sidebar.slider('Select max', 50, 500, step=10, value=150)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=50)
with st.spinner("Generating Summary.."):
    if button and video:
        v = VideoFileClip("video.mp4")
        v.audio.write_audiofile("movie.wav")
        whole_text=get_large_audio_transcription("movie.wav")
        st.write(whole_text)
        #st.video(video, format="video/mp4", start_time=0)
   
        
    
