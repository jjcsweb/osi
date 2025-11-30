import streamlit as st
from funciones.db_manager import get_note_titles, get_note_content, save_note

NEW_NOTE_TITLE = "-- Nueva Nota --"


def limpiar_campos_callback(clave_unica):
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"
    widget_key = f"selector_widget_{clave_unica}"
    st.session_state[title_key] = ""
    st.session_state[content_key] = ""
    st.session_state[widget_key] = NEW_NOTE_TITLE


def load_note_callback(clave_unica):
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"
    widget_key = f"selector_widget_{clave_unica}"

    titulo_seleccionado = st.session_state[widget_key]
    if titulo_seleccionado and titulo_seleccionado != NEW_NOTE_TITLE:
        contenido = get_note_content(clave_unica, titulo_seleccionado)
        st.session_state[title_key] = titulo_seleccionado
        st.session_state[content_key] = contenido
    else:
        limpiar_campos_callback(clave_unica)


def mostrar_area_texto(clave_unica, titulo_defecto, usuario_actual):
    widget_key = f"selector_widget_{clave_unica}"
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"

    # 1. Inicialización PROTEGIDA (Evita StreamlitAPIException)
    if widget_key not in st.session_state:
        st.session_state[widget_key] = NEW_NOTE_TITLE
    if title_key not in st.session_state:
        st.session_state[title_key] = ""
    if content_key not in st.session_state:
        st.session_state[content_key] = ""

    # 2. Selector
    titulos = get_note_titles(clave_unica)
    opciones = [NEW_NOTE_TITLE] + titulos

    st.selectbox(
        "📂 Seleccionar Nota:",
        options=opciones,
        key=widget_key,
        on_change=load_note_callback,
        args=(clave_unica,)
    )

    # 3. Campos de Edición
    st.text_input("📝 Título", key=title_key)
    st.text_area("✍️ Contenido", key=content_key, height=300)

    # 4. Guardado
    col1, col2 = st.columns([4, 1])
    with col1:
        if st.button("💾 Guardar Nota", key=f"btn_save_{clave_unica}", type="primary", use_container_width=True):
            tit = st.session_state[title_key]
            cont = st.session_state[content_key]

            if not tit or tit == NEW_NOTE_TITLE:
                st.error("Título inválido")
            else:
                save_note(clave_unica, tit, cont, usuario_actual)
                st.success("Guardado.")
                # Fuerza actualización visual del selector
                st.session_state[widget_key] = tit
                st.rerun()

    with col2:
        st.button("🧹", key=f"btn_cln_{clave_unica}", on_click=limpiar_campos_callback, args=(clave_unica,))