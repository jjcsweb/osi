# fuentes/texto/area_texto.py

import streamlit as st
# 🚨 IMPORTACIONES DEL MÓDULO CENTRALIZADO
from funciones.db_manager import get_note_titles, get_note_content, save_note


# --- Funciones de Callback ---

def limpiar_campos_callback(clave_unica):
    """Limpia los campos del editor de texto y resetea el selector."""
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"
    selector_key = f"selector_{clave_unica}"  # Clave de estado
    widget_key = f"selector_widget_{clave_unica}"  # Clave del widget selectbox

    # Limpiar estado
    st.session_state[title_key] = ""
    st.session_state[content_key] = ""
    st.session_state[selector_key] = "-- Nueva Nota --"
    # Resetear el widget para que refleje el estado
    st.session_state[widget_key] = "-- Nueva Nota --"


def load_note_callback(clave_unica):
    """Carga el contenido de la nota seleccionada en los campos del editor."""
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"
    selector_key = f"selector_{clave_unica}"
    widget_key = f"selector_widget_{clave_unica}"

    # 🚨 Usamos el valor del widget, que es el que se actualiza primero
    titulo_seleccionado = st.session_state[widget_key]

    if titulo_seleccionado and titulo_seleccionado != "-- Nueva Nota --":
        # USANDO FUNCIÓN CENTRALIZADA
        contenido = get_note_content(clave_unica, titulo_seleccionado)

        st.session_state[title_key] = titulo_seleccionado
        st.session_state[content_key] = contenido
        st.session_state[selector_key] = titulo_seleccionado
    else:
        # Llama a limpiar si se selecciona "-- Nueva Nota --"
        limpiar_campos_callback(clave_unica)


def new_note_action(clave_unica):
    """Acción para limpiar y empezar una nueva nota."""
    limpiar_campos_callback(clave_unica)


# --- Componente UI Principal ---

def mostrar_area_texto(clave_unica: str, titulo_area: str, usuario_actual: str):
    """Muestra la interfaz del editor de notas con persistencia."""

    # 1. Definición de Keys únicas
    selector_key = f"selector_{clave_unica}"  # Clave de estado para persistir la selección
    widget_key = f"selector_widget_{clave_unica}"  # Clave única del widget selectbox
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"

    # 🚨 2. INICIALIZACIÓN DE ESTADO (MOVIDA AL PRINCIPIO PARA EVITAR KEYERROR) 🚨
    # Esto asegura que todas las claves existen antes de que cualquier widget las lea.
    if title_key not in st.session_state:
        st.session_state[title_key] = ""
    if content_key not in st.session_state:
        st.session_state[content_key] = ""
    if selector_key not in st.session_state:
        st.session_state[selector_key] = "-- Nueva Nota --"
    if widget_key not in st.session_state:
        st.session_state[widget_key] = "-- Nueva Nota --"

    st.subheader(titulo_area)

    # 3. Listado y Selector de Notas
    col_list, col_buttons = st.columns([1, 4])

    with col_list:
        st.markdown("##### Notas Guardadas")

        note_titles = get_note_titles(clave_unica)
        opciones = ["-- Nueva Nota --"] + note_titles

        # Usamos el estado persistido (selector_key) para calcular el índice inicial
        try:
            index_seleccionado = opciones.index(st.session_state[selector_key])
        except ValueError:
            index_seleccionado = 0  # Si la nota guardada ya no existe
            st.session_state[selector_key] = opciones[0]

        # Dropdown para cargar notas
        st.selectbox(
            "Cargar Nota:",
            options=opciones,
            key=widget_key,  # Usar la clave del widget
            index=index_seleccionado,
            label_visibility="collapsed",
            on_change=load_note_callback,
            args=(clave_unica,),  # Pasamos solo la clave única, el callback lee el estado
            help="Selecciona una nota para editarla o '-- Nueva Nota --' para crear una."
        )

    with col_buttons:
        if note_titles:
            st.markdown("##### Carga Rápida (Recientes)")
            cols = st.columns(3)
            for idx, titulo in enumerate(note_titles[:3]):
                with cols[idx]:
                    # Los botones de carga rápida usan un callback directo
                    st.button(
                        f"📝 {titulo}",
                        key=f"load_note_{clave_unica}_{idx}",
                        on_click=load_note_callback,
                        args=(clave_unica,),
                        use_container_width=True
                    )
                    # Forzamos la clave del widget a ser el título antes de llamar al callback
                    if st.session_state.get(f"load_note_{clave_unica}_{idx}", False):
                        st.session_state[widget_key] = titulo
        else:
            st.write("Pulsa sobre el nombre de una nota para **cargarla en el editor**.")
            st.markdown("---")

    st.divider()

    # 1. INPUT PARA EL TÍTULO DE LA NOTA y BOTÓN 'Nueva Nota'
    col_title, col_new = st.columns([4, 1])
    with col_title:
        st.text_input(
            "Nombre de la Nota (Título)",
            key=title_key,
            placeholder="Pon un título único...",
            help="Escribe el nombre con el que quieres guardar esta nota."
        )
    with col_new:
        st.button("➕ Nueva Nota", key=f"btn_new_{clave_unica}", on_click=new_note_action, args=(clave_unica,),
                  use_container_width=True)

    # 2. ÁREA DE TEXTO (CONTENIDO)
    st.text_area(
        "Pega tu texto (Markdown) aquí:",
        key=content_key,
        height=250,
        help="El contenido se edita aquí."
    )

    # 3. BOTONES DE ACCIÓN (Guardar y Limpiar)
    col_save, col_clean = st.columns([4, 1])

    with col_save:
        btn_guardar = st.button("💾 Guardar Nota", key=f"btn_save_{clave_unica}", type="primary",
                                use_container_width=True)

    with col_clean:
        st.button(
            "🧹 Limpiar",
            key=f"btn_clean_{clave_unica}",
            use_container_width=True,
            on_click=limpiar_campos_callback,
            args=(clave_unica,),
            type="secondary"
        )

    log_container = st.empty()
    st.markdown("---")

    if btn_guardar:
        titulo = st.session_state[title_key]
        contenido = st.session_state[content_key]

        if not titulo:
            log_container.error("❌ Falta Título")
        elif not contenido.strip():
            log_container.warning("⚠️ Nota vacía")
        else:
            save_note(clave_unica, titulo, contenido, usuario_actual)
            log_container.success("✅ Nota guardada correctamente.")

            # Sincronizar el estado de sesión y el valor del widget
            st.session_state[selector_key] = titulo
            st.session_state[widget_key] = titulo
            st.rerun()

    st.markdown("---")

    # Previsualización del Contenido
    if st.session_state[content_key]:
        st.subheader("Previsualización Markdown")
        st.markdown(st.session_state[content_key])
    else:
        st.info("Escribe o carga una nota para ver la previsualización.")