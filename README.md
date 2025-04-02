📉 Social Media Detox Tracker

🚀 Introduction

The Social Media Detox Tracker is a simple web application built using Streamlit. It helps users monitor their screen time, set detox goals, and earn rewards for reducing social media usage.

🎯 Features

User Login System (Basic authentication with username & password)

Track Screen Time (Displays daily screen time for platforms like Instagram, Facebook, Twitter, YouTube, and TikTok)

Set Detox Goals (Users can input their goals for reducing screen time)

Reward System (Users earn points for achieving goals)

Interactive Charts (Visual representation of screen time data using bar charts)
🛠️ Installation & Setup

1️⃣ Install Dependencies

Ensure you have Python 3.x installed. Then, install Streamlit using:

pip install streamlit

2️⃣ Run the Application

Execute the following command in the terminal:

streamlit run app.py

This will open the application in your web browser at http://localhost:8501.

📝 Code Overview

The main functionalities of the app include:

🔐 User Authentication

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

Users input their credentials, and a simple check verifies login.

📊 Display Screen Time

screen_time = {
    "Instagram": 90,
    "Facebook": 60,
    "Twitter": 45,
    "YouTube": 120,
    "TikTok": 80
}
st.bar_chart(screen_time)

A bar chart displays the screen time usage for different platforms.

🎯 Goal Setting

goal = st.text_input("Enter your goal (e.g., Less than 1 hour on Instagram)")
if st.button("Save Goal"):
    st.success(f"Goal saved: {goal}")

Users can input and save their personal detox goals.

🏆 Rewards System

st.subheader("🏆 Rewards Earned")
st.write("Total Points: **250** 🎉")

The app displays a reward system that encourages users to reduce screen time.

Code file- https://drive.google.com/file/d/1Y7jrbgZJHT1AE3HXh98nX2c5LxxIJ6AS/view?usp=sharing
Screenshot
![Screenshot 2025-04-01 195750](https://github.com/user-attachments/assets/069a9ab1-5f6c-4646-abfc-565774face7a)
