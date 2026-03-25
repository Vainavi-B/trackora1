import streamlit as st
from supabase_client import supabase   #IMPORTANT

st.set_page_config(page_title="Trackora", layout="centered")

# ---------------- DASHBOARD ----------------
if "user" in st.session_state:
    st.title("🏠 Dashboard")
    st.write("Welcome!", st.session_state["user"].email)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Individual Streak", "5")

    with col2:
        st.metric("Group Streak", "10")

    if st.button("Logout"):
        del st.session_state["user"]
        st.rerun()

    st.stop()

# ---------------- MAIN UI ----------------
st.title("🎵 Trackora")

menu = st.selectbox("Select Option", ["Login", "Signup"])

# ---------------- LOGIN ----------------
if menu == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Please enter email and password")
        else:
            try:
                res = supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })

                if res.user:
                    st.session_state["user"] = res.user
                    st.success("Login successful!")
                    st.rerun()

            except Exception as e:
                st.error("Invalid email or password")


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
        if not email or not password:
            st.error("Email and password required")
        else:
            try:
                res = supabase.auth.sign_up({
                    "email": email,
                    "password": password
                })

                if res.user is None:
                    st.warning("Rate limit hit. Wait 2 mins and try again.")
                else:
                    user_id = res.user.id

                    supabase.table("users").insert({
                        "id": user_id,
                        "name": name,
                        "email": email,
                        "age": age,
                        "region": region,
                        "genre": genre,
                        "instruments": instruments,
                        "experience": experience,
                        "teacher": teacher,
                        "is_public": is_public
                    }).execute()

                    st.success("Account created successfully!")

            except Exception as e:
                st.error(f"Signup failed: {e}")