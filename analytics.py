import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_connection

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

if "user" not in st.session_state:
    st.stop()

user = st.session_state.user

conn = get_connection()

df = pd.read_sql_query(
    """
    SELECT * FROM transactions
    WHERE user_id=?
    """,
    conn,
    params=(user["id"],)
)

st.title("📈 Analytics")

if df.empty:

    st.warning(
        "No Data Available"
    )

    st.stop()

expense_df = df[
    df["type"] == "Expense"
]

if not expense_df.empty:

    st.subheader(
        "Category Wise Spending"
    )

    pie = px.pie(
        expense_df,
        names="category",
        values="amount"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

monthly = df.groupby(
    "date"
)["amount"].sum().reset_index()

st.subheader(
    "Transaction Trend"
)

line = px.line(
    monthly,
    x="date",
    y="amount",
    markers=True
)

st.plotly_chart(
    line,
    use_container_width=True
)