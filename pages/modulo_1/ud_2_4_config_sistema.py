import streamlit as st
from funciones.ui_manager import show_editable_content

# --- Función Auxiliar para la Maquetación del Bloque Editable ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""
    with st.container():
        if sub_heading:
            st.markdown(f"##### {sub_heading}")
        edit_key = f'edit_{id_base}'
        is_editing = st.session_state.get(edit_key, False)
        col_btn, col_spacer = st.columns([1, 10])
        with col_btn:
            if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}'):
                st.session_state[edit_key] = not is_editing
                st.rerun()
        show_editable_content(
            id_tema=id_base,
            titulo=topic_title,
            default_text=default_text,
            default_widget=default_widget
        )
# -------------------------------------------------------------

def show_ud_2_4():
    """Muestra el contenido de la UD 2.4: Configuración del sistema informático."""

    st.subheader(":blue[UNIDAD DIDACTICA 2.4 -- ]" ":blue[ *Configuración del sistema informático*]")



    # =================================================================
    # 1. Configuración del entorno de trabajo.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF2_UD4_T1"
    with st.expander("1. Configuración del entorno de trabajo."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Entorno de trabajo.",
            default_text="""
            Personalización de la interfaz de usuario, accesos directos, y la apariencia general del SO.
            **Ejemplo:** *Cambiar la resolución de pantalla, el puntero del ratón o la combinación de colores.*
            """,
            default_widget='default'
        )

    # =================================================================
    # 2. Administrador de impresión.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF2_UD4_T2"
    with st.expander("2. Administrador de impresión."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Cola de impresión.",
            default_text="""
            Herramienta para gestionar las impresoras conectadas, sus colas de impresión, los documentos en espera y los controladores.
            **Ejemplo:** *Pausar o cancelar un documento que se ha enviado erróneamente a la impresora.*
            """,
            default_widget='info'
        )

    # =================================================================
    # 3. Administrador de dispositivos.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF2_UD4_T3"
    with st.expander("3. Administrador de dispositivos."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Drivers y Hardware.",
            default_text="""
            Utilidad para ver y gestionar el hardware conectado al sistema, actualizar controladores y diagnosticar problemas (ej. *drivers* faltantes o con conflicto).
            **Ejemplo:** *Identificar un dispositivo con un signo de exclamación amarillo que indica un problema de controlador.*
            """
        )

    # =================================================================
    # 4. Protección del sistema.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF2_UD4_T4"
    with st.expander("4. Protección del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Puntos de Restauración.",
            default_text="""
            Configuración de **Puntos de Restauración** que permiten al SO volver a un estado anterior en caso de fallos o problemas.
            **Ejemplo:** *Crear un punto de restauración antes de instalar un software desconocido o un controlador nuevo.*
            """,
            default_widget='success'
        )

    # =================================================================
    # 5. Configuración avanzada del sistema.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF2_UD4_T5"
    with st.expander("5. Configuración avanzada del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Ajustes avanzados.",
            default_text="""
            Ajustes del **rendimiento**, **memoria virtual**, **perfiles de usuario**, variables de entorno y opciones de arranque.
            **Ejemplo:** *Ajustar el tamaño de la Memoria Virtual (Archivo de Paginación) para optimizar el rendimiento en sistemas con poca RAM.*
            """
        )
    st.divider()

if __name__ == '__main__':
    show_ud_2_4()