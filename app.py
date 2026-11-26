import streamlit as st

st.title("Calculadora")

numero1 = st.number_input("Primer número", value=0.0)
numero2 = st.number_input("Segundo número", value=0.0)

operacion = st.radio(
    "Operación",
    ("Suma", "Resta", "Multiplicación", "División", "Residuo", "Potencia"),
    horizontal=True,
)

if operacion == "Suma":
    resultado = numero1 + numero2
elif operacion == "Resta":
    resultado = numero1 - numero2
elif operacion == "Multiplicación":
    resultado = numero1 * numero2

elif operacion == "División":
    if numero2 == 0:
        st.error("No se puede dividir entre cero")
        resultado = None
    else:
        resultado = numero1 / numero2

elif operacion == "Residuo":
    if numero2 == 0:
        st.error("No se puede calcular el residuo entre cero")
        resultado = None
    else:
        resultado = numero1 % numero2

elif operacion == "Potencia":
    if numero1 == 0 and numero2 < 0:
        st.error("No se puede elevar cero a un exponente negativo")
        resultado = None
    elif numero1 < 0 and not numero2.is_integer():
        st.error("El exponente debe ser entero cuando la base es negativa")
        resultado = None
    else:
        resultado = numero1 ** numero2

