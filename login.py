import streamlit as st
import time
# Initialize user credentials in session state if not already present
if "USER_CREDENTIALS" not in st.session_state:
    st.session_state["USER_CREDENTIALS"] = {
        "admin": "password123",
        "user": "userpass"
    }

def login():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state["USER_CREDENTIALS"] and st.session_state["USER_CREDENTIALS"][username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}! Redirecting...")
            st.rerun()  # Rerun the app to load the logged-in state
        else:
            st.error("Invalid username or password")

def register():
    st.title("Register New User")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if new_username in st.session_state["USER_CREDENTIALS"]:
            st.error("Username already exists!")
        elif new_password != confirm_password:
            st.error("Passwords do not match!")
        elif new_username and new_password:
            # Register the new user (stored in session state)
            st.session_state["USER_CREDENTIALS"][new_username] = new_password
            st.success(f"User {new_username} successfully registered! Please login.")
            time.sleep(2)
            st.session_state["authenticated"] = False
            st.session_state["username"] = ""
            st.experimental_rerun()  # Reset to login page after registration
        else:
            st.error("Please provide both username and password.")

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login_or_register = st.radio("Choose an option", ["Login", "Register"])

    if login_or_register == "Login":
        login()
    elif login_or_register == "Register":
        register()
else:
    st.write(f"Logged in as **{st.session_state['username']}**")  # Show logged-in user
    exec(open("app1.py").read())  # Ensure app1.py exists in the same directory
