# homepage.py
import streamlit as st
import sys, asyncio

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

st.set_page_config(
    page_title="AI Street",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- compact CSS (no pills) ----------
CARD_CSS = """
<style>
main .block-container { padding-top: 1.1rem; padding-bottom: .7rem; max-width: 1200px; }
h1, h2, h3 { margin-bottom: .45rem; }
hr { margin: .7rem 0 1rem 0; }
.aist-card {
  border: 1px solid rgba(0,0,0,0.06);
  padding: 16px 16px 12px 16px;
  border-radius: 14px;
  box-shadow: 0 1px 12px rgba(0,0,0,0.04);
  background: #ffffff;
}
ul.aist-bullets { margin:.25rem 0 .2rem 1.1rem; }
ul.aist-bullets li { margin:.12rem 0; }
.caption-tight { margin-top:.35rem; color:#64748b; font-size:.86rem; }
</style>
"""
st.markdown(CARD_CSS, unsafe_allow_html=True)

# ---------------- Landing Page ----------------
def landing():
    # Header row with quick Login/Logout
    hdr_l, hdr_r = st.columns([7, 2])
    with hdr_l:
        st.title("🌐 Welcome to AIStreet")
        st.subheader("Your AI Agents, All in One Place")
        st.write("Operational AI that plugs into BI workflows and removes repetitive toil. 🚀")
        st.success("If you are seeing this at www.aistreet.org, your integration works!")
    with hdr_r:
        user = st.session_state.get("user")
        st.write("")  # spacer
        st.write("")  # spacer
        if user:
            st.caption(f"Signed in as **{user}**")
            st.page_link("pages/90_Account/99_Logout.py", label="Logout", icon=":material/logout:")
        else:
            st.page_link("pages/90_Account/9_Login.py", label="Login", icon=":material/login:")

    st.markdown("---")

    # Access notice (no form here)
    access_l, access_r = st.columns([5, 4])
    with access_l:
        st.subheader("Access")
        if st.session_state.get("user"):
            st.success("You’re signed in. Use the sidebar or cards below to open products.")
        else:
            st.write("**Please sign in to access products.**")
            st.page_link("pages/90_Account/9_Login.py", label="Go to Login", icon=":material/login:")
    with access_r:
        m1, m2, m3 = st.columns(3)
        m1.metric("Agents", "3", "+2")
        m2.metric("Time Saved", "48%", "est.")
        m3.metric("Integrations", "5+", "new")

    st.markdown("---")

    # ---------- Product grid (two rows, three cards) ----------
    # Row 1
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="aist-card">', unsafe_allow_html=True)
        st.markdown("### 🔎 KPI Drift Hunter")
        st.write(
            "Continuously scans dashboards to **catch metric & widget drift** before stakeholders notice. "
            "Built for BI teams that need early warning and reproducible evidence."
        )
        st.markdown(
            """
            <ul class="aist-bullets">
              <li><b>Solves:</b> silent metric regressions, stale widgets, broken filters</li>
              <li><b>For:</b> Analytics Engineers, BI Developers, Product Ops</li>
              <li><b>Why AI:</b> heuristic + LLM checks surface non-obvious anomalies</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
        l1, l2, l3 = st.columns([1.1, 1.2, 1.3])
        with l1: st.page_link("kpidrifthunteragent_homepage.py", label="Overview", icon=":material/analytics:")
        with l2: st.page_link("pages/10_kpidrift_hunter/11_kpidrift_runthescan.py", label="Run Scan", icon=":material/play_circle:")
        with l3: st.page_link("pages/10_kpidrift_hunter/12_kpidrift_widgetextractor.py", label="Widget Extractor", icon=":material/crop:")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="aist-card">', unsafe_allow_html=True)
        st.markdown("### 🧾 ReceiptScanner")
        st.write(
            "Turn messy receipts into clean, structured rows ready for finance workflows. "
            "Handles varied formats with **high extraction accuracy**."
        )
        st.markdown(
            """
            <ul class="aist-bullets">
              <li><b>Solves:</b> manual entry, inconsistent fields, time-consuming QA</li>
              <li><b>For:</b> Finance Ops, Expense Tools, SMB Back-office</li>
              <li><b>Why AI:</b> robust OCR + schema-aware post-processing</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
        r1, r2, r3 = st.columns([1.05, 1.05, 1.0])
        with r1: st.page_link("receiptscanner_homepage.py", label="Overview", icon=":material/receipt_long:")
        with r2: st.page_link("pages/30_receiptscanner/31_uploadreceipt.py", label="Upload", icon=":material/upload_file:")
        with r3: st.page_link("pages/30_receiptscanner/32_extractreceipt.py", label="Extract", icon=":material/fact_check:")
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="aist-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ ProvisionAgent")
        st.write(
            "Spin up demo or test environments, seed data, and manage artifacts. "
            "Reduces setup time for **onboarding, POCs, or reproducible demos**."
        )
        st.markdown(
            """
            <ul class="aist-bullets">
              <li><b>Solves:</b> slow environment setup, inconsistent data, manual resets</li>
              <li><b>For:</b> Solution Engineers, Sales Eng, DevRel</li>
              <li><b>Why AI:</b> templates + agents automate common provisioning paths</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
        p1, p2 = st.columns([1, 1.1])
        with p1: st.page_link("provisionalagent_homepage.py", label="Overview", icon=":material/engineering:")
        with p2: st.page_link("pages/50_provisioning/51_provision.py", label="Provision", icon=":material/rocket_launch:")
        st.markdown("</div>", unsafe_allow_html=True)

    # Row 2 (compact admin + about/company)
    a1, a2, a3 = st.columns(3)
    with a1:
        st.markdown('<div class="aist-card">', unsafe_allow_html=True)
        st.markdown("### 🧩 Operations")
        st.write("Operate agents with simple consoles and reports. Designed to keep day-2 ops smooth.")
        st.markdown(
            """
            <ul class="aist-bullets">
              <li>Console: real-time controls & health</li>
              <li>Reports: usage, accuracy, latency trends</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
        a_l, a_r = st.columns(2)
        with a_l: st.page_link("pages/2_admin.py", label="Console", icon=":material/terminal:")
        with a_r: st.page_link("pages/3_Reports.py", label="Reports", icon=":material/insights:")
        st.markdown("</div>", unsafe_allow_html=True)

    with a2:
        st.markdown('<div class="aist-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Ideal Users")
        st.write("Teams that live in BI tools and need **reliable, low-touch** automation:")
        st.markdown(
            """
            <ul class="aist-bullets">
              <li>Analytics & BI teams maintaining dashboards at scale</li>
              <li>Finance/Ops teams processing receipts & spend</li>
              <li>SE/DevRel teams running repeatable demos</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="caption-tight">Need something custom? Reach out.</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with a3:
        st.markdown('<div class="aist-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 Next Steps")
        st.write("Sign in and open a product. Each page includes examples and a short guide.")
        if st.session_state.get("user"):
            st.page_link("kpidrifthunteragent_homepage.py", label="Open KPI Drift Hunter", icon=":material/analytics:")
        else:
            st.page_link("pages/90_Account/9_Login.py", label="Login to Continue", icon=":material/login:")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.caption("© AIStreet — Building practical AI that ships.")

# ---------------- Pages ----------------
#home = st.Page(landing, title="Landing Page", icon=":material/home:", default=True)
# ---------------- Pages ----------------
home = st.Page("pages/00_Home.py", title="Landing Page", icon=":material/home:", default=True)


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

# Admin
admin_console = st.Page("pages/2_admin.py",   title="Console",  icon=":material/terminal:")
admin_reports = st.Page("pages/3_Reports.py", title="Reports",  icon=":material/insights:")

# Account
login  = st.Page("pages/90_Account/9_Login.py",   title="Login",  icon=":material/login:")
logout = st.Page("pages/90_Account/99_Logout.py", title="Logout", icon=":material/logout:")

# ---------------- Navigation tree ----------------
nav = st.navigation(
    {
        "Home": [home],
        "KPI Drift Hunter Agent": [kdh_home, kdh_run, kdh_widget],
        "ReceiptScanner": [rs_home, rs_upload, rs_extract],
        "ProvisionAgent": [prov_home, provision],
        "Admin": [admin_console, admin_reports],
        "Account": [login, logout],
    },
    position="sidebar",
)

nav.run()
