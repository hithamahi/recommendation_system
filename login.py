import streamlit as st

# Dummy user credentials (Modify as needed)
USER_CREDENTIALS = {
    "admin": "password123",
    "user": "userpass"
}

def login():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid username or password")

# Initialize session state if not already set
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.write(f"Logged in as **{st.session_state['username']}**")  # Debugging line
    exec(open("app1.py").read())  # Ensure app1.py exists in the same directory
