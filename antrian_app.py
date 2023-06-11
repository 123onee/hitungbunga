import streamlit as st

def calculate_interest_rate(principal, future_value, num_periods):
    interest_rate = ((future_value / principal) ** (1 / num_periods) - 1) * 100
    return interest_rate

def main():
    st.title("Kalkulator Suku Bunga")

    st.subheader("Masukkan Informasi")
    principal = st.number_input("Jumlah Pokok (Principal):", min_value=0.0, value=1000.0, step=100.0)
    future_value = st.number_input("Nilai Masa Depan (Future Value):", min_value=0.0, value=1500.0, step=100.0)
    num_periods = st.number_input("Jumlah Periode:", min_value=1, value=5, step=1)

    if st.button("Hitung Suku Bunga"):
        interest_rate = calculate_interest_rate(principal, future_value, num_periods)
        st.write("Suku Bunga:", interest_rate, "%")

if __name__ == "__main__":
    main()