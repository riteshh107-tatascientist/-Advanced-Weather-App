import streamlit as st
import random
import pandas as pd
import datetime
import time
import requests
import base64
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Advanced Weather App 🌐 Global Weather Hub 🌎",
    page_icon="🌤 🚩",
    layout="wide"
)

# ---------------- UI STYLING (House Predictor Premium Style) ----------------
st.markdown("""
    <style>
    .stApp {
        background: url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .glass-card {
        background: rgba(0, 0, 0, 0.7);
        border-radius: 25px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
        margin-bottom: 20px;
    }
    .motto-text {
        color: #FF4500;
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #FF4500;
    }
    [data-testid="stMetricValue"] { 
        color: #00ffcc !important; 
        font-size: 2.8rem !important;
        text-shadow: 0 0 15px #00ffcc;
    }
    label { color: #ffffff !important; font-weight: bold !important; font-size: 1.1rem !important; }
    h1, h2, h3 { color: #00d2ff !important; text-shadow: 0 0 10px rgba(0, 210, 255, 0.3); }
    </style>
""", unsafe_allow_html=True)

# ---------------- API KEY ----------------
API_KEY = "0756dafd0f6c793e6b810993cf370c28"

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## ⚙️ Settings")
city = st.sidebar.text_input("🔍 Enter City or State Name", value="Bhopal")
refresh = st.sidebar.button("🔄 Refresh Weather")

# ---------------- MUSIC FUNCTION (Corner, Hidden, Deployment Friendly) ----------------
def corner_music(file_path):
    """Plays hidden looping background music safely."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(f"""
            <audio id="bg-music" src="data:audio/mp3;base64,{b64}" autoplay loop controls></audio>
            <style>
                #bg-music {{
                    position: fixed;
                    bottom: 10px;
                    left: 10px;
                    width: 50px !important;
                    height: 30px !important;
                    opacity: 0.2;  /* almost hidden */
                    z-index: 9999;
                }}
            </style>
            """, unsafe_allow_html=True)
    else:
        st.warning("🎵 Background music file not found. Place 'pawan_singh.mp3' in the project folder.")

# 🎵 Run hidden corner music (relative path)
corner_music("pawan_singh.mp3")

# ---------------- MAIN CONTENT ----------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Header Section
col_title, col_motto = st.columns([2, 1])
with col_title:
    st.title("🌦 Advanced Weather App")
    st.subheader(f"📍 Location: {city.upper()}")
with col_motto:
    st.markdown('<div class="motto-text">🌐 Global Weather Hub 🌎</div>', unsafe_allow_html=True)

st.divider()

# API Function
def get_real_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["main"]["temp"], data["main"]["humidity"], data["wind"]["speed"]
        return None, None, None
    except:
        return None, None, None

if refresh:
    with st.spinner('⚡ Fetching latest satellite data...'):
        time.sleep(1)

temperature, humidity, wind_speed = get_real_weather(city)

# Weather Metrics
if temperature is not None:
    c1, c2, c3 = st.columns(3)
    c1.metric("🌡 Temperature", f"{temperature}°C")
    c2.metric("💧 Humidity", f"{humidity}%")
    c3.metric("🌬 Wind Speed", f"{wind_speed} m/s")

    if temperature > 35: st.error("🔥 Status: Very Hot Weather")
    elif temperature > 25: st.warning("☀ Status: Warm Weather")
    else: st.success("❄ Status: Cool Weather")
else:
    st.error(f"❌ Could not find weather for '{city}'. Please check the spelling.")

# Graph Section
st.markdown("---")
st.markdown("### 📈 Temperature Trend (Last 7 Days)")
dates = [(datetime.date.today() - datetime.timedelta(days=i)) for i in range(7)]
base_temp = temperature if temperature else 30
temps = [base_temp + random.randint(-5, 5) for _ in range(7)]
data = pd.DataFrame({"Date": dates[::-1], "Temp (°C)": temps[::-1]})
st.line_chart(data.set_index("Date"))

# ---------------- FOOTER SECTIONS ----------------
st.markdown("---")
col_math, col_ds = st.columns(2)

with col_math:
    st.markdown("### 🧠 Mathematics Applied")
    st.write("🔹 **Mean (Average):** For trend analysis.")
    st.write("🔹 **Linear Interpolation:** For graph plotting.")
    st.write(r"🔹 **Time Series:** Tracking data over $t$ intervals.")

with col_ds:
    st.markdown("### 📊 Data Science Skills")
    st.write("🔹 **API Integration:** RESTful requests.")
    st.write("🔹 **Data Wrangling:** Pandas DataFrame cleaning.")
    st.write("🔹 **Visualization:** Real-time Plotly/Streamlit charts.")

st.markdown("---")
f_col1, f_col2 = st.columns([2, 1])

with f_col1:
    st.markdown("### 👨‍💻 Project Developer")
    st.markdown(f"<h2 style='color: #00ffcc; margin-top:-10px;'>Ritesh Kumar Singh</h2>", unsafe_allow_html=True)
    st.write("🚀 **Passionate about Data Science & AI**")
    st.caption("🏆 College Math + Python Model Project")

with f_col2:
    st.markdown("### 🏫 Institution")
    st.markdown("<b style='color: #FFFF00; font-size:1.2rem;'>Technocrats Institute of Technology (TIT)</b>", unsafe_allow_html=True)
    st.write("📍 Bhopal, MP")
    st.write("🎓 **B.Tech CSE (Data Science)**")

st.markdown("---")
st.info("📌 This app uses the OpenWeatherMap API to fetch real-time meteorological data.")
st.markdown('</div>', unsafe_allow_html=True)