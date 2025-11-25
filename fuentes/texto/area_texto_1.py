import streamlit as st
import sqlite3

DB_FILE = "curso-osi.db"


# --- Funciones DB Internas ---

def get_titulos_notas(guia_id):
    """Recupera solo los títulos para el desplegable."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT titulo FROM notas WHERE guia_id = ? ORDER BY fecha_modificacion DESC", (guia_id,))
    titulos = [row[0] for row in cursor.fetchall()]
    conn.close()
    return titulos


def get_contenido_nota(guia_id, titulo):
    """Recupera el contenido de una nota específica."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT contenido FROM notas WHERE guia_id = ? AND titulo = ?", (guia_id, titulo))
    res = cursor.fetchone()
    conn.close()
    return res[0] if res else ""


def save_note(guia_id, titulo, contenido, usuario):
    """Guarda o actualiza."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE notas ADD COLUMN usuario TEXT")
    except:
        pass

    cursor.execute("""
    INSERT OR REPLACE INTO notas (guia_id, titulo, contenido, fecha_modificacion, usuario) 
    VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?);
    """, (guia_id, titulo, contenido, usuario))
    conn.commit()
    conn.close()


# --- CALLBACKS (Aquí está la magia para evitar el error) ---

def limpiar_campos_callback(title_key, content_key, selector_key):
    """Función que se ejecuta ANTES de recargar la página al pulsar Limpiar."""
    st.session_state[title_key] = ""
    st.session_state[content_key] = ""
    st.session_state[selector_key] = "-- Nueva Nota --"


def cargar_nota_callback(clave_unica, selector_key, title_key, content_key):
    """Función que se ejecuta cuando cambias el desplegable."""
    seleccion = st.session_state[selector_key]

    if seleccion and seleccion != "-- Nueva Nota --":
        contenido = get_contenido_nota(clave_unica, seleccion)
        st.session_state[title_key] = seleccion
        st.session_state[content_key] = contenido
    else:
        # Si selecciona "Nueva Nota", limpiamos
        st.session_state[title_key] = ""
        st.session_state[content_key] = ""


# --- Componente UI Principal ---

def mostrar_area_texto(clave_unica: str, titulo_area: str, usuario_actual: str):
    """
    Renderiza el editor con layout corregido y control de estado seguro.
    """

    # 1. Definición de Keys únicas
    title_key = f"title_{clave_unica}"
    content_key = f"content_{clave_unica}"
    selector_key = f"selector_{clave_unica}"

    # 2. Inicialización de Estado (Solo si no existen)
    if title_key not in st.session_state:
        st.session_state[title_key] = ""
    if content_key not in st.session_state:
        st.session_state[content_key] = ""
    if selector_key not in st.session_state:
        st.session_state[selector_key] = "-- Nueva Nota --"

    st.subheader(titulo_area)

    # 3. Layout Asimétrico (Editor Grande | Botonera Estrecha)
    col_editor, col_botonera = st.columns([5, 1], gap="medium")

    # --- COLUMNA IZQUIERDA: EDITOR ---
    with col_editor:

        # A. Selector (Dropdown) con Callback
        opciones = ["-- Nueva Nota --"] + get_titulos_notas(clave_unica)

        # OJO: Si la nota cargada ya no existe en la lista (ej. se borró), reseteamos el index
        index_seleccionado = 0
        if st.session_state[selector_key] in opciones:
            index_seleccionado = opciones.index(st.session_state[selector_key])

        st.selectbox(
            "📂 Cargar nota existente:",
            options=opciones,
            index=index_seleccionado,
            key=selector_key,
            on_change=cargar_nota_callback,  # <--- Callback aquí
            args=(clave_unica, selector_key, title_key, content_key),
            label_visibility="collapsed"
        )
        st.caption("☝️ Selecciona arriba para editar una nota existente.")

        # B. Inputs (Vinculados a Session State)
        st.text_input("Título:", key=title_key, placeholder="Pon un título único...")
        st.text_area("Contenido (Markdown):", key=content_key, height=350)

    # --- COLUMNA DERECHA: ACCIONES ---
    with col_botonera:

        # Botón Limpiar con Callback
        st.button(
            "🧹 Limpiar",
            key=f"btn_clean_{clave_unica}",
            use_container_width=True,
            on_click=limpiar_campos_callback,  # <--- Callback aquí
            args=(title_key, content_key, selector_key),
            type="secondary"
        )

        #st.markdown("<br><br><br>", unsafe_allow_html=True)  # Espacio visual

        # Botón Guardar (Este no necesita callback complejo, solo lógica post-click)
        btn_guardar = st.button("💾 Guardar", key=f"btn_save_{clave_unica}", type="secondary", use_container_width=True)

        st.markdown("---")

        # Logs debajo de la botonera
        log_container = st.empty()

        if btn_guardar:
            titulo = st.session_state[title_key]
            contenido = st.session_state[content_key]

            if not titulo:
                log_container.error("Falta Título")
            elif not contenido.strip():
                log_container.warning("Nota vacía")
            else:
                save_note(clave_unica, titulo, contenido, usuario_actual)
                log_container.success("Guardado ok")
                # Opcional: sleep(1) y st.rerun() si quieres que el selector se actualice al instante