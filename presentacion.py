import streamlit as st
import streamlit.components.v1 as components
from streamlit import container

from funciones.mis_funciones import leer_markdown

acerca_de, notebookLM, making_off = st.tabs(
    [
        "Acerca de",
        "NotebooLM",
        "Como se hizo",
    ]
)
with acerca_de:
    st.subheader(f":grey[Como se estructura el curso]")
    contenido = leer_markdown(("fuentes/curso_osi/acerca_curso.md"))
    st.markdown(contenido)
    st.divider()

with notebookLM:
    st.subheader(f":grey[Presentación realizada con NotebookLM]")
    st.divider()
    st.info("Se presenta el curso en formatos de video y texto, de forma amena y divertida. ")


    col1, col2 = st.columns(2)
    with col1:
        with st.container(key=1):
            st.markdown(f"### :grey[Video editado con IA]")
            st.video("fuentes/curso_osi/presentacion/Manual_del_Profesional_de_TI.mp4", width=500)
    with col2:
        with st.container(key=2):
            st.markdown(f"### :grey[Podcast(IA) sobre el curso ]", )

            st.markdown("""
                Entretenido podcast con voz y tonos naturales que comenta los contenidos del programa educativo.
            
                Escuchado con sentido del humor, y con la naturalidad de su voz, asomará una sonrisa.
                Puedes modificar la velocidad de reproducción.                
                """)


            st.audio("fuentes/curso_osi/presentacion/Manual_del_Profesional_de_TI.mp4")



    st.markdown(
        """
            El video y el podcast mostrados han sido editados con IA, a partir de una ficha del curso, y cuatro archivo cheet_cheet con el contenido del "temario" del curso.

        """
    )
    st.divider()
    st.info("""
        ***Toda la estructura ha sido creada a partir de estos archivos:***
        
            0.IFCT0209_ficha.pdf
            1.MF0219_2: Instalación y configuración de sistemas operativos.md
            2.MF0220_2: Implantación de los elementos de la red local.md
            3.MF0221_2: Instalación y configuración de aplicaciones informáticas .md
            4.MF0222_2: Aplicaciones microinformáticas.md
        """)
    st.divider()


    #st.image("fuentes/curso_osi/presentacion/NotebookLM Mind Map.png")

with making_off:
    st.subheader(f":grey[💬Chats con Gemini para el montaje de la web]")

    st.info(
        """
            Los siguientes archivos html (con scrolling) nos muestran el proceso para la creacion de esta pagina web. Escrita en python (código) a traves del entorno web de streamlit y usando un "asistente" de la IA gemini para el montaje de backend y el frontend. 🚫 No se incluyen todos los chats por seguridad.
            
            Me sirve para recordar como realizar los ***"prompts"*** adecuados para obtener el objetivo buscado. Mi gem de gemini se llama curso OSI. Aconsejable trabajar con los ultimos modelos de LLM cuando el numero de archivos en su base de conocimientos aumenta. En mi caso gemini 2.5 Pro.
            
        """
    )
    st.divider()

    st.subheader(f":grey[⏳Ordenados por orden cronológico.]  ")
    with st.expander("Chats con gemini AI - Volumen 1"):

        arch_html = "fuentes/curso_osi/como_se_hizo/estructura_modular_curso_1.html"
        with open(arch_html, 'r') as file:
            html_data = file.read()
        st.components.v1.html(html_data, height=800, scrolling=True)
        st.divider()

    with st.expander("Chats con gemini AI - Volumen 2"):
        arch_html = "fuentes/curso_osi/como_se_hizo/estructura_modular_curso_2.html"
        with open(arch_html, 'r') as file:
            html_data = file.read()
        st.components.v1.html(html_data, height=800, scrolling=True)
        st.divider()
    st.divider()


