# auth/supabase_auth.py
import streamlit as st
from supabase import create_client

@st.cache_resource
def get_client():
    return create_client(st.secrets["SUPABASE__URL"], st.secrets["SUPABASE__ANON_KEY"])

def ensure_session():
    if "user" not in st.session_state:
        st.session_state["user"] = None
    return {"user": st.session_state["user"]}

def sign_up(email, password):
    try:
        res = get_client().auth.sign_up({"email": email, "password": password})
        # res.user will be unconfirmed if email confirmation is enabled
        return True, "Account created. Check your email to verify."
    except Exception as e:
        return False, f"Sign up error: {e}"

def sign_in(email, password):
    try:
        res = get_client().auth.sign_in_with_password({"email": email, "password": password})
        if not res or not res.user:
            return False, "Invalid credentials or email not verified."
        st.session_state["user"] = {"id": res.user.id, "email": res.user.email}
        return True, "Signed in."
    except Exception as e:
        return False, f"Auth error: {e}"

def send_password_reset(email):
    try:
        get_client().auth.reset_password_email(email)
        return True, "Password reset email sent."
    except Exception as e:
        return False, f"Reset error: {e}"

def sign_out():
    try:
        get_client().auth.sign_out()
    finally:
        st.session_state["user"] = None
