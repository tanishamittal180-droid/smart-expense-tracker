import streamlit as st
import pandas as pd

from database.db import get_connection

st.set_page_config(
    page_title="Budgets",
    layout="wide"
)

if "user" not in st.session_state:
    st.stop()

user = st.session_state.user

conn = get_connection()
cur = conn.cursor()

st.title("🎯 Budget Management")

category = st.selectbox(
    "Category",
    [
        "Food",
        "Rent",
        "Travel",
        "Shopping",
        "Bills",
        "Education",
        "Entertainment",
        "Healthcare"
    ]
)

budget = st.number_input(
    "Budget Amount",
    min_value=0.0
)

if st.button("Save Budget"):

    cur.execute(
        """
        INSERT INTO budgets
        (
        user_id,
        category,
        budget
        )
        VALUES
        (?,?,?)
        """,
        (
            user["id"],
            category,
            budget
        )
    )

    conn.commit()

    st.success(
        "Budget Saved"
    )

budgets = pd.read_sql_query(
    """
    SELECT * FROM budgets
    WHERE user_id=?
    """,
    conn,
    params=(user["id"],)
)

st.subheader("Saved Budgets")

st.dataframe(
    budgets,
    use_container_width=True
)