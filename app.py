import streamlit as st

st.title("Conversor de temperatura")
celsius = st.number_input("Grados celsius")

farenheit = celsius * 9 / 5 + 32

st.write(f"{celsius} C son {farenheit} F")