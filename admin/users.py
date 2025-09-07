# admin/users.py
import streamlit as st
from supabase import create_client

def render():
    st.header("👤 Admin — Users & Roles")

    # Require Supabase secrets to be set
    if "SUPABASE_URL" not in st.secrets or "SUPABASE_ANON_KEY" not in st.secrets:
        st.error("Supabase secrets not found. Please configure SUPABASE_URL and SUPABASE_ANON_KEY.")
        return

    client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_ANON_KEY"])

    try:
        # ⚠️ auth.users is only accessible with service role key.
        # In production, replace ANON_KEY with SERVICE_ROLE_KEY for admin-only functions.
        res = client.table("profiles").select("user_id, display_name, avatar_url, created_at").execute()

        st.subheader("Registered Users")
        if not res.data:
            st.info("No users found.")
        else:
            for row in res.data:
                st.write(f"- **{row.get('display_name') or row['user_id']}** "
                         f"(joined {row['created_at']})")
    except Exception as e:
        st.error(f"Unable to fetch users: {e}")
        st.info(
            "Note: To read full `auth.users`, you need to call Supabase Admin APIs "
            "with the Service Role key (never expose this key client-side)."
        )
