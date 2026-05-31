import streamlit as st
import pandas as pd

from database.db import get_connection
from utils.categorizer import auto_category

st.set_page_config(
    page_title="CSV Import",
    layout="wide"
)

if "user" not in st.session_state:
    st.stop()

user = st.session_state.user

conn = get_connection()
cur = conn.cursor()

st.title("📂 Import CSV")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(
        uploaded_file
    )

    st.dataframe(df)

    if st.button("Import Data"):

        for _, row in df.iterrows():

            desc = str(
                row["Description"]
            )

            category = auto_category(
                desc
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
                    "Expense",
                    category,
                    float(
                        row["Amount"]
                    ),
                    desc,
                    str(
                        row["Date"]
                    )
                )
            )

        conn.commit()

        st.success(
            f"{len(df)} Transactions Imported"
        )