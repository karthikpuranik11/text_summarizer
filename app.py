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
  
def mp4_to_wav():
  video = VideoFileClip("video.mp4")
  video.audio.write_audiofile(wav, format='.wav')
  return wav  
    
st.title("Summarize Text")
video = st.file_uploader("Choose a file", type=['mp4'])
button = st.button("Summarize")

max = st.sidebar.slider('Select max', 50, 500, step=10, value=150)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=50)
with st.spinner("Generating Summary.."):
    if button and video:
        st.write(mp4_to_wav())
    
