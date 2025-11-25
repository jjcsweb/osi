import streamlit as st
from funciones.ui_manager import show_editable_content
from arquitectura import arquitectura

# --- Función Auxiliar para la Maquetación del Bloque Editable ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content.
    CORRECCIÓN: Se ha cambiado 'width="auto"' a 'width="content"' para evitar el error de ancho de Streamlit.
    """

    # 1. Título opcional para el bloque
    if sub_heading:
        st.markdown(f"##### {sub_heading}")

    # 2. Lógica del botón de edición (Posición discreta)
    edit_key = f'edit_{id_base}'
    is_editing = st.session_state.get(edit_key, False)

    # Usamos las columnas para posicionar el botón.
    # El key 'btn_toggle_{id_base}' DEBE ser único en todo el script.
    col_btn, col_spacer = st.columns([1, 10])

    with col_btn:
        # CORRECCIÓN DE ANCHO FINAL: Cambiado de 'auto' a 'content' (válido)
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary", width="content"):
            st.session_state[edit_key] = not is_editing
            st.rerun()

    show_editable_content(
        id_tema=id_base,
        titulo=topic_title,
        default_text=default_text,
        default_widget=default_widget,
        default_image_url_fija=image_url_fija
    )


# -------------------------------------------------------------

def show_ud_1_2():
    """Muestra el contenido de la UD 1.2: Funciones del Sistema Operativo Informático."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.2 -- ]" ":blue[ *Funciones del Sistema Operativo Informático*]")

    # =================================================================
    # 1. Conceptos básicos.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD2_T1"
    with st.expander("1. Conceptos básicos. Concepto y arquitectura del SO."):
        RUTA_IMAGEN_BUSES = "fuentes/imagenes/logo.jpg"  # Ruta de imagen estática
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Conceptos básicos. Concepto y arquitectura del SO.",
            default_text="""
            El **Sistema Operativo (SO)** es el software fundamental que gestiona los recursos de *hardware* y proporciona una interfaz para los programas de aplicación. Actúa como intermediario entre el usuario y la máquina.

            Un SO se compone de: **Kernel** (núcleo), **Shell** (intérprete de comandos/interfaz) y **Utilidades** (programas de soporte).
            """,
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_BUSES  # Pasar la URL fija aquí

        )


    # =================================================================
    # 2. Funciones principales.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD2_T2"
    with st.expander("2. Funciones del SO. Gestión de recursos."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Funciones principales (Gestión)",
            sub_heading="📝 Funciones de Gestión",
            default_text="""
            El SO desempeña tareas críticas:
            * **Gestión de Procesos:** Controla la ejecución de programas, asignando tiempo de CPU a cada uno (multitarea).
            * **Gestión de Memoria Principal:** Decide qué procesos se cargan en la RAM y cuándo, optimizando el uso del espacio.
            * **Gestión del Sistema de Archivos:** Organiza el almacenamiento de datos en discos, proporcionando una estructura lógica (directorios, ficheros).
            * **Gestión de Entrada/Salida (E/S):** Comunica la CPU con los dispositivos periféricos a través de los *drivers*.
            """,
            default_widget='default'
        )


        _render_editable_block(
            id_base=f"{TEMA_ID_T2}_S1",
            topic_title="2. Funciones principales (Seguridad)",
            sub_heading="⚠️ Seguridad y Protección",
            default_text="El SO implementa mecanismos para proteger los recursos del sistema de accesos no autorizados. ¡Presta atención a esta función!",
            default_widget='error'
        )
    st.divider()


if __name__ == '__main__':
    show_ud_1_2()