import streamlit as st
import pandas as pd
from database.db import get_connection

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

if "user" not in st.session_state:
    st.error("Please Login First")
    st.stop()

user = st.session_state.user

conn = get_connection()

df = pd.read_sql_query(
    """
    SELECT * FROM transactions
    WHERE user_id=?
    ORDER BY id DESC
    """,
    conn,
    params=(user["id"],)
)

st.image(
    "assets/banner.jpg",
    use_container_width=True
)

st.title("📊 Dashboard")

income = 0
expense = 0

if not df.empty:

    income = df[
        df["type"] == "Income"
    ]["amount"].sum()

    expense = df[
        df["type"] == "Expense"
    ]["amount"].sum()

balance = income - expense

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Income",
        f"₹ {income:,.2f}"
    )

with col2:
    st.metric(
        "💸 Expense",
        f"₹ {expense:,.2f}"
    )

with col3:
    st.metric(
        "🏦 Balance",
        f"₹ {balance:,.2f}"
    )

st.subheader("Recent Transactions")

if df.empty:
    st.info("No Transactions Found")
else:
    st.dataframe(
        df[
            [
                "date",
                "type",
                "category",
                "amount",
                "description"
            ]
        ],
        use_container_width=True
    )