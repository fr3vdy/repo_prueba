import streamlit as st

st.title("Calculadora")

numero1 = st.number_input("Primer número", value=0.0)
numero2 = st.number_input("Segundo número", value=0.0)

operacion = st.radio(
    "Operación",
    ("Suma", "Resta", "Multiplicación", "División"),
    horizontal=True,
)

if operacion == "Suma":
    resultado = numero1 + numero2
elif operacion == "Resta":
    resultado = numero1 - numero2
elif operacion == "Multiplicación":
    resultado = numero1 * numero2
elif numero2 == 0:
    st.error("No se puede dividir entre cero")
    resultado = None
else:
    resultado = numero1 / numero2

if resultado is not None:
    st.write(f"Resultado: **{resultado}**")
