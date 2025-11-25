import streamlit as st
from funciones.ui_manager import show_editable_content

# --- Función Auxiliar para la Maquetación del Bloque Editable ---
# PASO 1: Corrección de argumentos y lógica del botón
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""

    # 1. Título opcional para el bloque
    if sub_heading:
        st.markdown(f"##### {sub_heading}")

    # 2. Lógica del botón de edición (Posición discreta)
    edit_key = f'edit_{id_base}'
    is_editing = st.session_state.get(edit_key, False)

    # Usamos las columnas para posicionar el botón.
    col_btn, col_spacer = st.columns([1, 10])

    with col_btn:
        # CORRECCIÓN: Usamos 'width="content"' que es válido y ajustado al texto.
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary", width="content"):
            st.session_state[edit_key] = not is_editing
            st.rerun()

    # 3. Llamada a la función de guardado/renderizado
    # CORRECCIÓN: Pasamos 'default_image_url_fija' correctamente.
    show_editable_content(
        id_tema=id_base,
        titulo=topic_title,
        default_text=default_text,
        default_widget=default_widget,
        default_image_url_fija=image_url_fija
    )


# -------------------------------------------------------------

def show_ud_1_3():
    """Muestra el contenido de la UD 1.3: Elementos de un Sistema Operativo Informático."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.3 -- ]" ":blue[ *Elementos de un Sistema Operativo Informático*]")

    # PASO 3: Usamos una ruta existente para evitar errores
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # PASO 2: Eliminado el expander de nivel superior para mostrar los temas directamente

    # =================================================================
    # 1. Gestión de procesos.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD3_T1"
    with st.expander("1. Gestión de procesos."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Gestión de procesos.",
            default_text="Se encarga de crear, eliminar, suspender y reanudar procesos. El SO asigna tiempo de CPU a cada proceso (*Scheduling*).",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # =================================================================
    # 2. Gestión de memoria.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD3_T2"
    with st.expander("2. Gestión de memoria."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Gestión de memoria.",
            default_text="Asigna y libera bloques de memoria RAM a los procesos en ejecución para evitar conflictos y optimizar el uso del espacio.",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # =================================================================
    # 3. El sistema de Entrada y Salida (E/S).
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF1_UD3_T3"
    with st.expander("3. El sistema de Entrada y Salida (E/S)."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. El sistema de Entrada y Salida (E/S).",
            default_text="Facilita la comunicación entre la CPU/Memoria y los dispositivos externos (periféricos) a través de *drivers*.",
            default_widget='info'
        )

    # =================================================================
    # 4. Sistema de archivos.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF1_UD3_T4"
    with st.expander("4. Sistema de archivos."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Sistema de archivos.",
            default_text="Estructura lógica que organiza los datos en el disco (ej. directorios, ficheros, metadatos).",
            default_widget='success'
        )

    # =================================================================
    # 5. Sistema de protección.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF1_UD3_T5"
    with st.expander("5. Sistema de protección."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Sistema de protección.",
            default_text="Mecanismos que controlan el acceso a los recursos del sistema por parte de los usuarios y programas.",
            default_widget='warning'
        )

    # =================================================================
    # 6. Sistema de comunicaciones.
    # =================================================================
    TEMA_ID_T6 = "MF0219_UF1_UD3_T6"
    with st.expander("6. Sistema de comunicaciones."):
        _render_editable_block(
            id_base=TEMA_ID_T6,
            topic_title="6. Sistema de comunicaciones.",
            default_text="Gestiona la conexión y el intercambio de datos entre sistemas a través de interfaces de red.",
            default_widget='default'
        )

    # =================================================================
    # 7. Sistema de interpretación de órdenes.
    # =================================================================
    TEMA_ID_T7 = "MF0219_UF1_UD3_T7"
    with st.expander("7. Sistema de interpretación de órdenes."):
        _render_editable_block(
            id_base=TEMA_ID_T7,
            topic_title="7. Sistema de interpretación de órdenes.",
            default_text="Proporciona la interfaz (CLI o GUI) para que el usuario interactúe con el sistema operativo.",
            default_widget='info'
        )

    # =================================================================
    # 8. Programas del sistema.
    # =================================================================
    TEMA_ID_T8 = "MF0219_UF1_UD3_T8"
    with st.expander("8. Programas del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T8,
            topic_title="8. Programas del sistema.",
            default_text="Utilidades básicas incluidas con el SO (gestores de archivos, editores de texto, herramientas de monitorización).",
            default_widget='default'
        )

    st.divider()


if __name__ == '__main__':
    show_ud_1_3()