# Modulo: acerca_de.py
# Propósito: Gestionar una única nota persistente (ej: la descripción de la página).
# Una vez creada, solo muestra el área de texto para edición rápida.

import streamlit as st
import sqlite3
import os

DB_FILE = "totumrevolotum.db"  # Archivo de base de datos SQLite

# --- Constantes para Streamlit Session State ---
# Estas claves ahora son estáticas para enfocarse en una ÚNICA nota (About)
TITLE_KEY = "acerca_de_title"
CONTENT_KEY = "acerca_de_content"
IS_CONFIGURED_KEY = "acerca_de_is_configured"
LAST_SAVE_CONTENT = "acerca_de_last_save"  # Para evitar re-guardar si no hay cambios
DEFAULT_TITLE = "Nueva Nota Sin Nombre"  # Nueva constante para mejorar legibilidad


# --- Funciones de Base de Datos (DB) ---

def inicializar_db():
    """Crea la tabla 'notas' si no existe."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Usamos (guia_id, titulo) como clave principal compuesta
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        guia_id TEXT NOT NULL,
        titulo TEXT NOT NULL,
        contenido TEXT,
        fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (guia_id, titulo)
    );
    """)
    conn.commit()
    conn.close()


def get_note(guia_id: str):
    """Obtiene el título y el contenido de la primera nota para la guia_id dada."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Para la lógica de "Acerca de", asumimos que solo habrá una nota por guia_id
    cursor.execute("SELECT titulo, contenido FROM notas WHERE guia_id = ? LIMIT 1;", (guia_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado  # Retorna (titulo, contenido) o None


def save_note(guia_id: str, titulo: str, contenido: str):
    """Guarda o actualiza una nota. También actualiza la fecha de modificación."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR REPLACE INTO notas (guia_id, titulo, contenido, fecha_modificacion) 
    VALUES (?, ?, ?, CURRENT_TIMESTAMP);
    """, (guia_id, titulo, contenido))
    conn.commit()
    conn.close()
    # Al guardar, actualizamos el estado de la última versión guardada
    st.session_state[LAST_SAVE_CONTENT] = contenido


# --- Streamlit Callbacks y Funciones de Acción ---

def check_and_save_content(guia_id: str):
    """
    Función de callback para guardar el contenido automáticamente al cambiar (simulando Ctrl+Enter).
    Esto se ejecuta automáticamente cuando el widget de text_area cambia de valor.
    """
    # Usamos .get() para evitar un KeyError si el estado no se inicializó por alguna razón
    titulo = st.session_state.get(TITLE_KEY)
    contenido_nuevo = st.session_state.get(CONTENT_KEY, "").strip()
    contenido_anterior = st.session_state.get(LAST_SAVE_CONTENT, "")

    # Solo guardamos si hay un título y el contenido ha cambiado
    if titulo and titulo != DEFAULT_TITLE and contenido_nuevo and contenido_nuevo != contenido_anterior:
        save_note(guia_id, titulo, contenido_nuevo)
        st.toast(f"✅ Contenido actualizado (Clave: {guia_id})")
    elif not titulo or titulo == DEFAULT_TITLE:
        # Mostramos la advertencia SOLAMENTE si estamos configurados, pero el título se perdió
        if st.session_state.get(IS_CONFIGURED_KEY, False):
            st.warning("⚠️ Título no asignado, no se puede guardar automáticamente. Reinicia para recargar.")


def initial_setup_save_action(guia_id: str):
    """Acción para guardar la nota por primera vez (durante la configuración inicial)."""
    titulo = st.session_state.get(TITLE_KEY, "").strip()
    contenido = st.session_state.get(CONTENT_KEY, "")

    if not titulo or titulo == DEFAULT_TITLE:
        st.error("❌ Por favor, asigna un nombre único a la nota antes de guardar.")
        return

    if not contenido.strip():
        st.warning("⚠️ La nota está vacía. Se guardará con contenido vacío.")

    save_note(guia_id, titulo, contenido)
    st.success(f"✅ Nota '{titulo}' guardada con éxito. Activando modo 'Solo Edición'.")
    st.session_state[IS_CONFIGURED_KEY] = True

    # Rerunnear para cargar el modo de edición simplificado
    st.rerun()


# --- Función Principal del Módulo ---

def mostrar_acerca_de(clave_unica: str, titulo_area: str):
    """
    Renderiza el gestor de la nota 'Acerca de...' en modo de configuración o solo edición.

    :param clave_unica: La guia_id en la DB (ej: "Notas_Home").
    :param titulo_area: El título principal del área (ej: "Acerca de esta pagina").
    """

    inicializar_db()

    # 1. Inicialización de Session State: Garantizar que las claves existan SIEMPRE.
    if IS_CONFIGURED_KEY not in st.session_state:
        st.session_state[IS_CONFIGURED_KEY] = False

    if TITLE_KEY not in st.session_state or st.session_state[TITLE_KEY] is None:
        st.session_state[TITLE_KEY] = DEFAULT_TITLE

    if CONTENT_KEY not in st.session_state:
        st.session_state[CONTENT_KEY] = f"Escribe el contenido de {titulo_area} aquí..."

    if LAST_SAVE_CONTENT not in st.session_state:
        st.session_state[LAST_SAVE_CONTENT] = ""

    # 2. Carga/Recarga de la Nota: Si la nota está en la DB, sobrescribe los valores por defecto.
    # Esta lógica se ejecuta en cada run para garantizar que el estado refleje la DB.
    nota_cargada = get_note(clave_unica)

    if nota_cargada:
        titulo_db, contenido_db = nota_cargada

        # Sobrescribe el estado de Streamlit con los valores de la DB
        st.session_state[TITLE_KEY] = titulo_db
        st.session_state[LAST_SAVE_CONTENT] = contenido_db

        # Solo actualiza el CONTENT_KEY si está en el estado por defecto o no está configurado
        # Esto previene sobrescribir el texto que el usuario está escribiendo justo ahora.
        if st.session_state[CONTENT_KEY] == f"Escribe el contenido de {titulo_area} aquí..." or not st.session_state[
            IS_CONFIGURED_KEY]:
            st.session_state[CONTENT_KEY] = contenido_db

        # Si encontramos la nota, siempre la marcamos como configurada.
        st.session_state[IS_CONFIGURED_KEY] = True

    # 3. Renderizado del Componente

    # El título del área de texto lo usaremos como encabezado de la sección de la DB
    st.markdown(f"**Gestor de Notas:** Clave DB: `{clave_unica}`")

    is_configured = st.session_state[IS_CONFIGURED_KEY]

    # --- Modo de Configuración Inicial (Mostrar título y botón de guardar) ---
    if not is_configured:
        st.info(
            f"Configuración Inicial de '{titulo_area}': Define el título y el contenido. Luego pulsa 'Guardar y Bloquear'.")

        # INPUT PARA EL TÍTULO DE LA NOTA (solo visible en configuración)
        st.text_input(
            "Nombre Único de esta Nota (Título)",
            key=TITLE_KEY,
            help="Este nombre se usará para guardar en la DB.",
        )

        # ÁREA DE TEXTO (editable)
        st.text_area(
            f"Pega tu texto (Markdown) aquí: (Propósito de {titulo_area})",
            key=CONTENT_KEY,
            height=300,
            on_change=None,  # Desactivamos el auto-guardado en la configuración
            help="Introduce el contenido principal de la nota."
        )

        # BOTÓN DE GUARDAR (solo visible en configuración)
        st.markdown("Pulsa este botón para guardar el contenido y pasar al modo de edición rápida.")
        if st.button("💾 Guardar y Bloquear Nota", key=f"btn_setup_save_{clave_unica}"):
            initial_setup_save_action(clave_unica)

    # --- Modo de Solo Edición (Oculta título y guarda con on_change) ---
    else:
        # **CAMBIO AQUÍ: Usamos titulo_area como encabezado principal.**
        st.markdown(f"### {titulo_area}")
        st.markdown(
            f"*(Título Guardado en DB: `{st.session_state[TITLE_KEY]}`)*")  # Mantenemos la referencia al título DB
        st.markdown("---")  # Separador visual

        # ÁREA DE TEXTO (editable con guardado automático al cambiar)
        st.text_area(
            "Pega tu texto (Markdown) aquí:",
            key=CONTENT_KEY,
            height=300,
            # Guardado automático al perder el foco (o simulación de Ctrl+Enter)
            on_change=check_and_save_content,
            args=(clave_unica,),
            help="Edita el contenido aquí. Se guarda automáticamente al pulsar Ctrl+Enter o al perder el foco."
        )
        st.caption(
            "✨ Guardado automático activado. Los cambios se registran con **Ctrl+Enter** o al perder el foco del campo.")

    # 4. Eliminada la Vista previa del contenido.