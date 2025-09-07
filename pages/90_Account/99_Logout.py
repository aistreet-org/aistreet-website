import streamlit as st

st.set_page_config(page_title="Logout", layout="wide")
st.title("👋 Logout")

if st.session_state.get("user"):
    st.info(f"Signed in as **{st.session_state.user}**")
    if st.button("Logout", use_container_width=True):
        st.session_state.user = None
        st.success("Logged out.")
        st.page_link("pages/00_Home.py", label="Go to Landing", icon=":material/home:")

else:
    st.write("You’re not signed in.")
    st.page_link("pages/90_Account/9_Login.py", label="Go to Login", icon=":material/login:")
