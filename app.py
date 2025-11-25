import streamlit as st
from funciones.db_manager import initialize_all_dbs
from funciones.mis_funciones import estilo_titulo

st.set_page_config(
    page_title="Curso OSI",
    page_icon="👋",
    initial_sidebar_state="collapsed", # Key parameter here
    layout="wide", # Optional: can also set layout to "wide"
)

estilo_titulo()
initialize_all_dbs()

st.logo("fuentes/curso_osi/logo_sidebar.png", size="large")
st.subheader(f" 📥 *CURSO DE OPERADOR DE SISTEMAS INFORMÁTICOS*")

def run_app():

    pages = {

    " 🗁  DIRECTORIO RAIZ ": [
        st.Page("presentacion.py", title="Presentación", icon="🙋"),
        st.Page("home.py", title="Home", icon="💼"),
        st.Page("ayuda.py", title="Ayuda", icon="🛟"),

    ],

    " 🗁  MÓDULOS CURSO ": [
        st.Page("pages/modulo_1/modulo_1.py", title="Módulo 1", icon="🖥️"),
        st.Page("pages/modulo_2/modulo_2.py", title="Módulo 2", icon="🔗"),
        st.Page("pages/modulo_3/modulo_3.py", title="Módulo 3", icon="🛠️"),
        st.Page("pages/modulo_4/modulo_4.py", title="Módulo 4", icon="👥"),
    ],

    "🗁  HERRAMIENTAS ": [

        st.Page("pages/playground.py", title="Patio de juegos", icon="🚧"),
        st.Page("pages/galeria_img.py", title="Galeria de imagenes", icon="📷"),
        st.Page("pages/constructor.py", title="Constructor Páginas", icon="👷"),
        st.Page("pages/visor_lecciones.py", title="Visor Páginas", icon="👀"),
        st.Page("pages/notas.py", title="Notas", icon="📒"),
        st.Page("pages/editor_codigo.py", title="Editor Codigo", icon="📝"),
        st.Page("fuentes/html/captura_html.py", title="Copiar URL", icon="🌐"),

    ],

        "🗁  TOOLS ": [

        #st.Page("pages/playground.py", title="Editor MD", icon="📝"),

        ],
    }

    pg = st.navigation(pages)
    pg.run()

if __name__ == '__main__':
    run_app() # Ejecutas la función que contiene pg.run()


