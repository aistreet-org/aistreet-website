import streamlit as st
import sys, asyncio

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

st.set_page_config(page_title="AI Street",
                   page_icon="🧠",
                   layout="wide",
                   initial_sidebar_state="expanded")

# ---------------- Landing Page ----------------
def landing():
    st.title("🌐 Welcome to AIStreet")
    st.subheader("Your AI Agents, All in One Place")
    st.write("This is a placeholder site deployed with Streamlit. 🚀")
    st.success("If you are seeing this at www.aistreet.org, your integration works!")
    st.markdown("---")
    st.subheader("Access")
    st.write("**Please sign in to access products**")

    user = st.session_state.get("user")
    if user:
        c1, c2 = st.columns([1, 3])
        with c1:
            st.success(f"Signed in as **{user}**")
        with c2:
            if st.button("Logout", use_container_width=True):
                st.session_state.user = None
                st.rerun()
    else:
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="you@example.com")
            pwd = st.text_input("Password", placeholder="••••••••", type="password")
            do_login = st.form_submit_button("Sign In")
        if do_login:
            if email and pwd:
                st.session_state.user = email  # TODO: replace with Supabase auth
                st.rerun()
            else:
                st.error("Enter your email and password to continue.")

# ---------------- Pages ----------------
home = st.Page(landing, title="Landing Page", icon=":material/home:", default=True)

# ProvisionAgent group
prov_home = st.Page("provisionalagent_homepage.py", title="ProvisionAgent", icon=":material/engineering:")
provision = st.Page("pages/50_provisioning/51_provision.py", title="Provision", icon=":material/rocket_launch:")

# KPI Drift Hunter Agent group
kdh_home = st.Page("kpidrifthunteragent_homepage.py", title="KPI Drift Hunter", icon=":material/analytics:")
kdh_run  = st.Page("pages/10_kpidrift_hunter/11_kpidrift_runthescan.py", title="Run the Scan", icon=":material/play_circle:")
kdh_widget = st.Page("pages/10_kpidrift_hunter/12_kpidrift_widgetextractor.py", title="Widget Extractor", icon=":material/crop:")

# Receipt Scanner group
rs_home   = st.Page("receiptscanner_homepage.py", title="ReceiptScanner", icon=":material/receipt_long:")
rs_upload = st.Page("pages/30_receiptscanner/31_uploadreceipt.py", title="Upload Receipt", icon=":material/upload_file:")
rs_extract= st.Page("pages/30_receiptscanner/32_extractreceipt.py", title="Extract", icon=":material/fact_check:")

# Admin children
admin_console = st.Page("pages/2_admin.py",   title="Console",  icon=":material/terminal:")
admin_reports = st.Page("pages/3_Reports.py", title="Reports",  icon=":material/insights:")
# (Add artifacts if you have it; otherwise leave it out)

# Account
login  = st.Page("pages/90_Account/9_Login.py",   title="Login",  icon=":material/login:")
logout = st.Page("pages/90_Account/99_Logout.py", title="Logout", icon=":material/logout:")

# ---------------- Navigation tree ----------------
nav = st.navigation(
    {
        "Home": [home],
        "ProvisionAgent": [prov_home, provision],
        "KPI Drift Hunter Agent": [kdh_home, kdh_run, kdh_widget],
        "ReceiptScanner": [rs_home, rs_upload, rs_extract],
        "Admin": [admin_console, admin_reports],
        "Account": [login, logout],
    },
    position="sidebar",
)

nav.run()
