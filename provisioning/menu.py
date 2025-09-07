import streamlit as st
from products.registry import PRODUCTS
from auth.supabase_auth import ensure_session, sign_in, sign_up, send_password_reset, sign_out

def _auth_panel():
    session = ensure_session()

    if session.get("user"):
        st.sidebar.success(f"Signed in: {session['user'].get('email','user')}")
        if st.sidebar.button("Sign out"):
            sign_out(); st.rerun()
        return True

    tabs = st.sidebar.tabs(["Sign in", "Sign up", "Forgot password"])
    # --- Sign in ---
    with tabs[0]:
        email = st.text_input("Email", key="login_email")
        pwd = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Sign in", key="login_btn"):
            ok, msg = sign_in(email, pwd)
            st.toast(msg, icon="✅" if ok else "❌")
            if ok: st.rerun()

    # --- Sign up ---
    with tabs[1]:
        e2 = st.text_input("Email", key="signup_email")
        p2 = st.text_input("Password", type="password", key="signup_pwd")
        if st.button("Create account", key="signup_btn"):
            ok, msg = sign_up(e2, p2)
            st.toast(msg, icon="✅" if ok else "❌")

    # --- Forgot ---
    with tabs[2]:
        e3 = st.text_input("Email", key="reset_email")
        if st.button("Send reset email", key="reset_btn"):
            ok, msg = send_password_reset(e3)
            st.toast(msg, icon="✅" if ok else "❌")

    return False

def render_sidebar():
    st.sidebar.title("AIStreet Portal")

    authed = _auth_panel()

    st.sidebar.markdown("---")
    product_slug = st.sidebar.radio(
        "Products",
        [p["slug"] for p in PRODUCTS],
        format_func=lambda s: next(p["label"] for p in PRODUCTS if p["slug"] == s),
    )

    pages = next(p["pages"] for p in PRODUCTS if p["slug"] == product_slug)
    page_key = st.sidebar.selectbox(
        "Section",
        [pg["key"] for pg in pages],
        format_func=lambda k: next(pg["label"] for pg in pages if pg["key"] == k),
    )

    is_admin = bool(st.session_state.get("is_admin", False))
    admin_choice = None
    st.sidebar.markdown("---")
    if is_admin:
        admin_choice = st.sidebar.selectbox("Admin", ["users"])

    return {"product": product_slug, "page": page_key, "admin": admin_choice, "authed": authed, "is_admin": is_admin}

def route(state):
    # Require login to use product pages (but landing can still show in app.py)
    if not state["authed"]:
        st.info("Please sign in to access products.")
        return

    # Admin
    if state["admin"]:
        if not state["is_admin"]:
            st.error("Admin access required."); return
        from admin.users import render as render_users
        if state["admin"] == "users": render_users(); return

    # Products
    if state["product"] == "provisioner":
        from products.provisioner import render as render_provisioner
        render_provisioner(); return

    if state["product"] == "receipt_scanner":
        if state["page"] == "upload":
            from products.receipt_scanner.pages.upload import render as rs_upload; rs_upload()
        elif state["page"] == "history":
            from products.receipt_scanner.pages.history import render as rs_hist; rs_hist()
        return

    if state["product"] == "kpi_drift_hunter":
        if state["page"] == "dashboards":
            from products.kpi_drift_hunter.pages.dashboards import render as kdh_dash; kdh_dash()
        elif state["page"] == "captures":
            from products.kpi_drift_hunter.pages.captures import render as kdh_cap; kdh_cap()
        return
