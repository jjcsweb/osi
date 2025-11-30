# pages/vista_leccion.py (Ejemplo de cómo usar la función)

import streamlit as st
st.title("hola de nuevo")
ask = st.imput("escribe algo")
if ask is not None:
  st.write('Escribistes: {ask}')
else:
  st.write("Escribe algo")
