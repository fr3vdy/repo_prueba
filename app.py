import streamlit as st

st.title("Calculadora")

numero1 = st.number_input("Primer número", value=0.0)
numero2 = st.number_input("Segundo número", value=0.0)

operacion = st.radio("Operación", ("Suma", "Resta"), horizontal=True)

if operacion == "Suma":
    resultado = numero1 + numero2
else:
    resultado = numero1 - numero2

st.write(f"Resultado: **{resultado}**")
