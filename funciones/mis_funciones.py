import streamlit as st

# Lectura de archivos
def leer_markdown(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read()
def leer_archivo(ruta_archivo):
    with open(ruta_archivo, "r") as file:
        contenido = file.read()
        # Renderiza el contenido en la aplicación Streamlit
        st.markdown(contenido)

# Lineas con estilo
def div_green():
    st.markdown(
        "<hr style='border:1px solid #4CAF50; border-radius:1px;'>",
        unsafe_allow_html=True)
def div_blue():
    st.markdown(
        "<hr style='border:1px solid #3B66D4; border-radius:3px;'>",
        unsafe_allow_html=True)

# Titulo CSS en el top de la pagina
def estilo_titulo():
    st.markdown("""
            <style>
                   /* Remove blank space at top and bottom */ 
                   .block-container {
                       padding-top: 2.4rem;
                       padding-bottom: 0rem;

                    }

            </style>
            """, unsafe_allow_html=True)

    st.markdown("""
        <h7 style="text-align: left; color: rgb(61, 157, 243); font-family: 'Arial Black', Gadget, sans-serif; font-style: italic;"> Designed with Streamlit </h2>

        """, unsafe_allow_html=True)