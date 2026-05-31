import streamlit as st

from database.db import create_tables
from utils.auth import register_user
from utils.auth import login_user

create_tables()

st.set_page_config(
    page_title="Smart Expense Tracker",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

if "user" not in st.session_state:
    st.session_state.user = None


st.title("💰 Smart Expense Tracker")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Login",
        "Register"
    ]
)

# REGISTER

if menu == "Register":

    st.subheader("Create Account")

    name = st.text_input("Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        success = register_user(
            name,
            email,
            password
        )

        if success:
            st.success(
                "Account Created Successfully"
            )

        else:
            st.error(
                "User Already Exists"
            )

# LOGIN

if menu == "Login":

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.user = user

            st.success(
                "Login Successful"
            )

            st.switch_page(
                "pages/dashboard.py"
            )

        else:

            st.error(
                "Invalid Credentials"
            )
            st.sidebar.page_link(
    "pages/dashboard.py",
    label="Dashboard"
)

st.sidebar.page_link(
    "pages/transactions.py",
    label="Transactions"
)

st.sidebar.page_link(
    "pages/budgets.py",
    label="Budgets"
)

st.sidebar.page_link(
    "pages/analytics.py",
    label="Analytics"
)

st.sidebar.page_link(
    "pages/import_csv.py",
    label="Import CSV"
)