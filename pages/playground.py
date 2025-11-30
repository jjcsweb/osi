# pages/vista_leccion.py (Ejemplo de cómo usar la función)

import streamlit as st
st.title("hola de nuevo")
ask = st.text_input("escribe algo")
if ask != '':
  st.write('Escribistes:', ask)
else:
  st.write("Escribe algo")

st.divider()
  
