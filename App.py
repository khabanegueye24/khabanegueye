import streamlit as st


st.title("Calculatrice ")

st.write("---")

num1 = st.number_input("num1")
num2 = st.number_input("num2")

operation = st.radio("Choisissez une opération :", ("Addition", "Soustraction", "Multiplication", "Division"))

if st.button("Calculer"):
    if operation == "Addition":
        resultat = num1 + num2
    elif operation == "Soustraction":
        resultat = num1 - num2
    elif operation == "Multiplication":
        resultat = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.warning("Division par zéro impossible !")
            resultat = "Non défini"
        else:
            resultat = num1 / num2
    st.success(f"Résultat : {resultat}")

