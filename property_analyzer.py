import streamlit as st

st.set_page_config(page_title="Property Analyzer", layout="centered")

st.title("🏘️ Real Estate Property Analyzer")

# --- Inputs ---
st.header("📋 Property Details")
purchase_price = st.number_input("Purchase Price ($)", value=300000, step=1000)
monthly_rent = st.number_input("Monthly Rent ($)", value=2500, step=100)
monthly_expenses = st.number_input("Monthly Operating Expenses ($)", value=600, step=50)
down_payment_pct = st.slider("Down Payment (%)", min_value=0.0, max_value=100.0, value=20.0)
interest_rate = st.number_input("Interest Rate (%)", value=6.5, step=0.1)
loan_term = st.number_input("Loan Term (Years)", value=30, step=1)

# --- Calculations ---
loan_amount = purchase_price * (1 - down_payment_pct / 100)
down_payment = purchase_price * (down_payment_pct / 100)
monthly_mortgage_payment = (
    loan_amount * (interest_rate / 100 / 12) /
    (1 - (1 + interest_rate / 100 / 12) ** (-loan_term * 12))
)

monthly_cash_flow = monthly_rent - monthly_expenses - monthly_mortgage_payment
annual_cash_flow = monthly_cash_flow * 12
cap_rate = (monthly_rent - monthly_expenses) * 12 / purchase_price * 100
cash_on_cash_return = (annual_cash_flow / down_payment) * 100 if down_payment else 0

# --- Output ---
st.header("📈 Investment Metrics")
st.metric("Cap Rate", f"{cap_rate:.2f} %")
st.metric("Cash-on-Cash Return", f"{cash_on_cash_return:.2f} %")
st.metric("Annual Cash Flow", f"${annual_cash_flow:,.0f}")
st.metric("Monthly Mortgage", f"${monthly_mortgage_payment:,.0f}")

if cash_on_cash_return < 5:
    st.warning("⚠️ This deal might not generate strong returns. Review your inputs.")
elif cash_on_cash_return > 10:
    st.success("✅ Strong potential return! Worth looking into.")

