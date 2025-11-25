import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from funciones.mis_funciones import *

st.set_page_config(
    page_title="Home del curso",
    page_icon="👋",
    initial_sidebar_state="collapsed", # Key parameter here
    layout="wide", # Optional: can also set layout to "wide"

)
st.subheader("Temario del curso")
st.markdown("Todos los elementos ordenados por módulos, unidades formativas(UF), unidades didácticas(UD) y temas.")
div_blue()
with st.expander("Tema del curso"):
    leer_archivo("fuentes/curso_osi/acerca_curso.md")




with st.expander("Ficha del curso IFCT0209"):
    pdf_viewer("fuentes/curso_osi/IFCT0209_ficha.pdf", height=600)

div_blue()


# Elige un area para editar una nota
tab1, tab2, tab3, tab4 = st.tabs(["MF0219", "MF0220", "MF0221", "MF0222"])

with tab1:
    # Ruta a tu archivo Markdown
    ruta_archivo = "fuentes/curso_osi/MF0219_2: Instalación y configuración de sistemas operativos.md"

    # Lee el contenido del archivo
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Muestra el contenido en Streamlit
    st.markdown(contenido)
    st.divider()
with tab2:
    # Ruta a tu archivo Markdown
    ruta_archivo = "fuentes/curso_osi/MF0220_2: Implantación de los elementos de la red local.md"

    # Lee el contenido del archivo
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Muestra el contenido en Streamlit
    st.markdown(contenido)
    st.divider()
with tab3:
    # Ruta a tu archivo Markdown
    ruta_archivo = "fuentes/curso_osi/MF0221_2: Instalación y configuración de aplicaciones informáticas .md"

    # Lee el contenido del archivo
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Muestra el contenido en Streamlit
    st.markdown(contenido)
    st.divider()
with tab4:
    # Ruta a tu archivo Markdown
    ruta_archivo = "fuentes/curso_osi/MF0222_2: Aplicaciones microinformáticas.md"

    # Lee el contenido del archivo
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Muestra el contenido en Streamlit
    st.markdown(contenido)
    st.divider()






