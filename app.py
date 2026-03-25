import streamlit as st

st.set_page_config(page_title="Trackora", layout="centered")

st.title("🎵 Trackora")

menu = st.selectbox("Select Option", ["Login", "Signup"])

# ---------------- LOGIN ----------------
if menu == "Login":
    st.write(" ")
    
    with st.container():
        st.subheader("Login")


    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Loggin in")


# ---------------- SIGNUP ----------------
if menu == "Signup":
    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age")
    region = st.text_input("Region")
    genre = st.text_input("Genre")
    instruments = st.text_input("Instruments")
    experience = st.text_input("Experience")
    teacher = st.text_input("Teacher (optional)")
    is_public = st.checkbox("Public Account")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        st.success("Account created!")