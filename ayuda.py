import streamlit as st


# --- CONFIGURACIÓN DE TEMA OSCURO "DARK WIKI" ---
def dark_wiki_css():
    st.markdown("""
    <style>
        /* 1. FONDO GLOBAL Y TEXTO BASE */
        .stApp {
            background-color: #0E1117; /* Gris muy oscuro (Github Dark style) */
            color: #C9D1D9; /* Gris perla muy claro para el texto */
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        /* 2. ENCABEZADOS (H1, H2, H3) - ALTO CONTRASTE */
        h1, h2, h3 {
            color: #58A6FF !important; /* Azul brillante estilo VS Code */
            font-weight: 700;
            border-bottom: 1px solid #30363d; /* Línea sutil debajo de los títulos */
            padding-bottom: 10px;
            margin-top: 20px;
        }

        /* Subheader específico (Ayuda del sitio) */
        div[data-testid="stMarkdownContainer"] h3 {
            color: #7EE787 !important; /* Verde neón suave para el título principal */
        }

        /* 3. ESTILO DE LAS PESTAÑAS (TABS) */
        /* Contenedor de pestañas */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
            border-bottom: 2px solid #30363d;
        }

        /* Pestaña INACTIVA */
        .stTabs [data-baseweb="tab"] {
            background-color: #161b22; /* Un poco más claro que el fondo */
            color: #8b949e; /* Texto gris apagado */
            border: 1px solid #30363d;
            border-bottom: none;
            border-radius: 6px 6px 0 0;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }

        /* Pestaña ACTIVA (Seleccionada) */
        .stTabs [aria-selected="true"] {
            background-color: #1f6feb !important; /* Azul intenso */
            color: #ffffff !important; /* Texto blanco brillante */
            border: 1px solid #1f6feb;
            font-weight: bold;
            box-shadow: 0px 0px 10px rgba(31, 111, 235, 0.4); /* Brillo sutil (Glow) */
        }

        /* Hover sobre pestañas */
        .stTabs [data-baseweb="tab"]:hover {
            color: #ffffff;
            background-color: #21262d;
        }

        /* 4. CONTENEDORES DE TEXTO Y MARKDOWN */
        /* Párrafos generales */
        p, li {
            font-size: 1.05rem;
            line-height: 1.7;
            color: #e6edf3; /* Casi blanco para lectura fácil */
        }

        /* Bloques de código (Code snippets dentro del markdown) */
        code {
            background-color: #2d333b !important; /* Fondo gris medio para código */
            color: #ff7b72 !important; /* Rojo suave para el texto del código */
            border-radius: 4px;
            padding: 2px 5px;
            font-family: 'Courier New', monospace;
        }

        /* Bloques de código grandes (```) */
        pre {
            background-color: #161b22 !important;
            border: 1px solid #30363d;
            border-radius: 8px;
        }

        /* Alertas (st.warning, st.info) adaptadas a oscuro */
        .stAlert {
            background-color: #161b22;
            color: #e6edf3;
            border: 1px solid #30363d;
        }

        /* Enlaces */
        a {
            color: #58a6ff !important;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }

    </style>
    """, unsafe_allow_html=True)


# Aplicar el tema oscuro
dark_wiki_css()

# --- LOGICA DE LA APP ---

st.subheader("📚 Ayuda del sitio")

ayuda_menu, cheet_sheet, buscar_web = st.tabs([
    "Ayuda Menú",
    "Cheat Sheet",
    "Buscar en Web",
])

with ayuda_menu:
    st.markdown("#### Navegación General")
    st.warning("Esta sección explica cómo usar el menú lateral y las opciones de usuario.")
    st.markdown("""
    * **Inicio:** Vuelve a la pantalla principal.
    * **Configuración:** Ajusta tus preferencias.
    * **Soporte:** Contacta con el administrador.
    """)

with cheet_sheet:
    st.info("Selecciona una tecnología para ver su referencia rápida.")

    markdown, html, css = st.tabs([
        "Markdown",
        "HTML",
        "CSS",
    ])


    # Helper function para leer archivos de forma segura
    def leer_archivo(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return f"⚠️ **Error:** No se encontró el archivo en la ruta: `{ruta}`"
        except Exception as e:
            return f"⚠️ **Error:** {str(e)}"


    with markdown:
        contenido = leer_archivo("fuentes/ayuda/cheet_cheet/ayuda_markdown.md")
        st.markdown(contenido)

    with html:
        contenido = leer_archivo("fuentes/ayuda/cheet_cheet/ayuda_html.md")
        st.markdown(contenido)

    with css:
        contenido = leer_archivo("fuentes/ayuda/cheet_cheet/ayuda_css.md")
        st.markdown(contenido)

with buscar_web:
    st.markdown("#### Búsqueda Integrada")
    st.text_input("Introduce tu búsqueda...", placeholder="Ej: Cómo centrar un div")
    st.caption("Los resultados se abrirán en una nueva pestaña.")
