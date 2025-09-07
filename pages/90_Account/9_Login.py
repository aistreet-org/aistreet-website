import streamlit as st

st.set_page_config(page_title="Login", layout="wide")

st.title("🔐 Login")
with st.form("login_form", clear_on_submit=False):
    email = st.text_input("Email", placeholder="you@example.com")
    pwd = st.text_input("Password", placeholder="••••••••", type="password")
    do_login = st.form_submit_button("Sign In")

if do_login:
    if email and pwd:
        st.session_state.user = email  # TODO: swap with real auth (Supabase)
        st.success("Signed in. Use the sidebar to open a product.")
        st.page_link("pages/00_Home.py", label="Go to Landing", icon=":material/home:")

        st.balloons()
    else:
        st.error("Enter your email and password to continue.")
