import streamlit as st
import pandas as pd

from database.db import get_connection
from utils.categorizer import auto_category

st.set_page_config(
    page_title="Transactions",
    layout="wide"
)

if "user" not in st.session_state:
    st.stop()

user = st.session_state.user

conn = get_connection()
cur = conn.cursor()

st.title("💸 Transactions")

with st.form("transaction_form"):

    transaction_type = st.selectbox(
        "Type",
        ["Income", "Expense"]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Description"
    )

    date = st.date_input(
        "Date"
    )

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
            "Healthcare",
            "Other"
        ]
    )

    submit = st.form_submit_button(
        "Add Transaction"
    )

if submit:

    if description:

        suggested = auto_category(
            description
        )

        cur.execute(
            """
            INSERT INTO transactions
            (
            user_id,
            type,
            category,
            amount,
            description,
            date
            )
            VALUES
            (?,?,?,?,?,?)
            """,
            (
                user["id"],
                transaction_type,
                suggested,
                amount,
                description,
                str(date)
            )
        )

        conn.commit()

        st.success(
            "Transaction Added"
        )

st.divider()

df = pd.read_sql_query(
    """
    SELECT * FROM transactions
    WHERE user_id=?
    ORDER BY id DESC
    """,
    conn,
    params=(user["id"],)
)

st.subheader("Transaction History")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True
    )

    delete_id = st.number_input(
        "Enter Transaction ID To Delete",
        min_value=0
    )

    if st.button("Delete Transaction"):

        cur.execute(
            """
            DELETE FROM transactions
            WHERE id=?
            """,
            (delete_id,)
        )

        conn.commit()

        st.success(
            "Transaction Deleted"
        )

        st.rerun()