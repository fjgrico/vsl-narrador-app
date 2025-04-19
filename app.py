import streamlit as st

st.set_page_config(page_title="VSL Narrador", layout="centered")

st.title("🎙️ Generador de Guiones VSL con Narración")

st.write("Esta es una versión funcional y mínima de la app para pruebas.")

if st.button("Generar texto de prueba"):
    st.success("✅ Este es tu guion generado: 'Hola, soy tu guion VSL automático.'")
