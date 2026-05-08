import streamlit as st
import pandas as pd

st.title("💰 Personal Budget Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.subheader("Add a New Expense")

# Input fields
date = st.date_input("Date")
item = st.text_input("Expense Item")
amount = st.text_input("Amount Spent (RM)")

# Submit button
if st.button("Add Expense"):
    try:
        amount = float(amount)

        if amount < 0:
            st.error("Amount cannot be negative!")
        else:
            st.session_state.expenses.append({
                "Date": date,
                "Expense Item": item,
                "Amount (RM)": amount
            })
            st.success(f"Expense '{item}' added successfully!")

    except:
        st.error("Amount must be a valid number!")

# Display table
if st.session_state.expenses:
    st.subheader("Expense Summary")

    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)

    total = df["Amount (RM)"].sum()
    st.write(f"### Total Expenses: RM {total:.2f}")