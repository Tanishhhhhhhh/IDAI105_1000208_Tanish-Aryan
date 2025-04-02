import streamlit as st

# App Title
st.set_page_config(page_title="Social Media Detox Tracker", layout="wide")

# Sidebar for User Authentication
st.sidebar.title("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

if login_button:
    if username == "admin" and password == "1234":  # Simple check
        st.session_state["logged_in"] = True
        st.sidebar.success("Login successful!")
    else:
        st.sidebar.error("Invalid credentials.")

# Main Page Content
st.title("📉 Social Media Detox Tracker")
st.write("Track your screen time and improve digital well-being!")

# Fake Data for Screen Time
screen_time = {
    "Instagram": 90,
    "Facebook": 60,
    "Twitter": 45,
    "YouTube": 120,
    "TikTok": 80
}

st.subheader("📊 Today's Screen Time")
st.bar_chart(screen_time)

# Goals Section
st.subheader("🎯 Set Detox Goals")
goal = st.text_input("Enter your goal (e.g., Less than 1 hour on Instagram)")
if st.button("Save Goal"):
    st.success(f"Goal saved: {goal}")

# Rewards Section
st.subheader("🏆 Rewards Earned")
st.write("Total Points: **250** 🎉")

st.write("Keep reducing screen time to earn more points!")

# Logout Button
if st.sidebar.button("Logout"):
    st.session_state["logged_in"] = False
    st.sidebar.success("Logged out successfully!")
