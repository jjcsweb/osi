import streamlit as st
from streamlit_ace import st_ace
import streamlit.components.v1 as components
import json

# ==============================================================================
# 1. CONFIGURACIÓN INICIAL Y TRUCOS CSS
# ==============================================================================
st.set_page_config(layout="wide", page_title="OSI Editor Lab")

# Mapeo de opciones disponibles
LANG_OPTIONS = ["markdown", "html", "css", "json"]

# --- Lógica de Detección de Parámetros de URL (NUEVO) ---
query_params = st.query_params
# Leer el parámetro 'lang' de la URL. Si no existe, usa 'markdown' por defecto.
initial_lang_from_query = query_params.get("lang", [LANG_OPTIONS[0]])[0].lower()
# Fin de la detección de parámetros

# Inyección de CSS para hacer el uploader más compacto y estilos
st.markdown("""
<style>
    /* Hace el uploader de archivos más compacto */
    div[data-testid="stFileUploader"] section {
        padding: 1rem; 
        min-height: 50px;
    }
    div[data-testid="stFileUploader"] small {
        display: none;
    }
    .success-box { padding: 10px; background-color: #d4edda; color: #155724; border-radius: 5px; }
    .error-box { padding: 10px; background-color: #f8d7da; color: #721c24; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

st.subheader(f"- :blue[Editor LIVE: Markdown, HTML, CSS & JSON]")

# ==============================================================================
# 2. BARRA LATERAL (CONTROL Y GESTIÓN DE ESTADO)
# ==============================================================================
with st.sidebar:
    st.markdown(f"#### 📂 *Archivos*")

    with st.expander("⬆️ Cargar archivo", expanded=False):
        uploaded_file = st.file_uploader(
            "Arrastra aquí",
            type=["md", "html", "css", "json", "txt"],
            label_visibility="collapsed"
        )

    st.divider()
    st.markdown(f"## ⚙️ *Configuración*")

    # --- Lógica para determinar el Índice Inicial del SelectBox ---
    index_lenguaje = 0  # Por defecto es markdown

    # 1. Comprobar si un idioma fue forzado por la URL
    if initial_lang_from_query in LANG_OPTIONS:
        index_lenguaje = LANG_OPTIONS.index(initial_lang_from_query)
    # 2. Si hay archivo subido, anula la configuración de la URL y usa la del archivo
    elif uploaded_file:
        ext = uploaded_file.name.split(".")[-1].lower()
        if ext in LANG_OPTIONS:
            index_lenguaje = LANG_OPTIONS.index(ext)

    lenguaje = st.selectbox(
        "Lenguaje",
        options=LANG_OPTIONS,
        index=index_lenguaje
    )
    # Fin de la lógica del selector de lenguaje

    tema = st.selectbox(
        "Tema",
        options=["monokai", "github", "dracula", "tomorrow", "twilight"],
        index=0
    )

    font_size = st.slider("Fuente", 10, 24, 14)
    auto_update = st.toggle("Auto-render", value=True)


# --- Funciones de Utilidad ---
def prettify_json(content):
    """Formatea el string JSON con indentación y lo guarda en session_state."""
    try:
        data = json.loads(content)
        # Usamos st.session_state para forzar la actualización del editor
        st.session_state['prettified_content'] = json.dumps(data, indent=4)
    except json.JSONDecodeError:
        pass


# ==============================================================================
# 3. CONTENIDO POR DEFECTO (Ejemplos OSI)
# ==============================================================================
defaults = {
    "markdown": """## 🌐 Modelo OSI - Capa 3 (Red)
### Tabla de Protocolos
#### Subtítulo
Texto en **negrita** y *cursiva*.

- Elemento 1
- Elemento 2

[Enlace a Google](https://google.com)

| Protocolo | Puerto | Descripción |
|-----------|:------:|-------------|
| HTTP      | 80     | Web no segura |
| SSH       | 22     | Acceso remoto |
""",

    "html": """<div class="card">
        <h3>📡 Estado del Servidor: SRV-01</h3>
        <p>IP: 192.168.1.10</p>
        <p>Estado: <span class="status">● ONLINE</span></p>
    </div>
    <div style="text-align: center; padding: 20px;">
    <h1 style="color: #FF4B4B;">Hola HTML</h1>
    <p>Esto es un párrafo con estilo inline.</p>
    <button>Púlsame</button>
    <style>
        .card { border: 1px solid #ddd; padding: 20px; border-radius: 8px; font-family: sans-serif; max-width: 300px; }
        .status { color: green; font-weight: bold; }
    </style>""",

    "css": """/* Animación de luz de estado de servidor */
.server-light {
    width: 50px;
    height: 50px;
    background-color: #4CAF50;
    border-radius: 50%;
    box-shadow: 0 0 0 rgba(76, 175, 80, 0.4);
    animation: pulse 2s infinite;
    margin: 20px auto;
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.7); }
    70% { box-shadow: 0 0 0 20px rgba(76, 175, 80, 0); }
    100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }
}""",

    "json": """{"interface_config":{"name":"eth0","enabled":true,"ipv4":{"address":"192.168.1.50","netmask":"255.255.255.0"}},"firewall_rules":[{"port":80,"action":"allow"},{"port":22,"action":"deny"}]}"""
}

# --- Lógica de Contenido Inicial Final ---
# 1. Comprueba si el botón Prettify fue presionado
if 'prettified_content' in st.session_state:
    contenido_inicial = st.session_state.pop('prettified_content')
# 2. Si hay archivo subido, usa ese contenido
elif uploaded_file is not None:
    contenido_inicial = uploaded_file.getvalue().decode("utf-8")
# 3. Si no, usa el contenido por defecto del lenguaje seleccionado (incluido el forzado por URL)
else:
    # Si el lenguaje cambia (manual o por URL), cargamos el default correcto.
    if st.session_state.get('last_lang') != lenguaje:
        contenido_inicial = defaults[lenguaje]
        st.session_state['last_lang'] = lenguaje
    else:
        contenido_inicial = defaults[lenguaje]

# ==============================================================================
# 4. LAYOUT PRINCIPAL (EDITOR Y PREVIEW)
# ==============================================================================

col_editor, col_preview = st.columns([1, 1])

with col_editor:
    st.markdown(f"#### 🌎 código ({lenguaje})")

    contenido_actual = st_ace(
        value=contenido_inicial,
        language=lenguaje,
        theme=tema,
        font_size=font_size,
        height=550,
        auto_update=auto_update,
        key=f"ace_{lenguaje}"
    )

    # --- Control y Validación ---
    if lenguaje == "json":
        st.button(
            "✨ Formatear JSON (Prettify)",
            on_click=prettify_json,
            args=(contenido_actual,),
            use_container_width=True
        )

        try:
            json.loads(contenido_actual)
            st.markdown('<div class="success-box">✅ Sintaxis JSON Válida</div>', unsafe_allow_html=True)
        except json.JSONDecodeError as e:
            st.markdown(f'<div class="error-box">❌ Error de Sintaxis: Línea {e.lineno}<br>{e.msg}</div>',
                        unsafe_allow_html=True)

# --- Lógica de Descarga ---
if lenguaje == "markdown":
    mime = "text/markdown"; ext = "md"
elif lenguaje == "html":
    mime = "text/html"; ext = "html"
elif lenguaje == "json":
    mime = "application/json"; ext = "json"
else:
    mime = "text/css"; ext = "css"

with st.sidebar:
    st.divider()
    st.download_button(
        label=f"💾 Guardar Cambios (.{ext})",
        data=contenido_actual,
        file_name=f"lab_osi.{ext}",
        mime=mime,
        use_container_width=True
    )

with col_preview:
    st.markdown("#### 👁️ Vista Previa")

    with st.container(border=True):
        if lenguaje == "markdown":
            st.markdown(contenido_actual, unsafe_allow_html=True)

        elif lenguaje == "html":
            components.html(contenido_actual, height=550, scrolling=True)

        elif lenguaje == "json":
            try:
                parsed = json.loads(contenido_actual)
                st.json(parsed)
            except:
                st.info("Corrige el JSON para ver la estructura de datos.")

        elif lenguaje == "css":
            html_template = f"""
            <style>{contenido_actual}</style>
            <div class="container" style="text-align: center; padding: 20px;">
                <div class="server-light"></div>
                <h3>Efecto CSS</h3>
                <p>El color y el ritmo de la luz es controlado por tu código CSS.</p>
            </div>
            """
            components.html(html_template, height=550)
st.divider()