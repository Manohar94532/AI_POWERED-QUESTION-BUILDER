from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
from dotenv import load_dotenv
import streamlit as st
import streamlit_chat as stc
import google.generativeai as genai
import PyPDF2
import docx
import os
import platform
import random
# Changed mysql.connector to pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from bson.objectid import ObjectId  # Import ObjectId for MongoDB's _id
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import googletrans
import numpy as np
import io
import datetime
from datetime import datetime, timedelta
from fpdf import FPDF
import csv
import tempfile
from pptx import Presentation
from streamlit_option_menu import option_menu
from pptx.util import Inches
import plotly.express as px
from streamlit_lottie import st_lottie  # Import the Lottie function
import requests  # To fetch the Lottie animation
import googletrans
# from google_trans_new import google_translator
# Using deep-translator as it's more reliable
from deep_translator import GoogleTranslator


translated = GoogleTranslator(source='auto', target='en').translate('Bonjour')
print(translated)


# Initialize translator (from google_trans_new, if used elsewhere)
# translator = google_translator()


st.set_page_config(layout="wide")
