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

def show_ud_2_6():
    """Muestra el contenido de la UD 2.6: Gestión de Procesos y Recursos."""

    st.subheader(":blue[UNIDAD DIDACTICA 2.6 -- ]" ":blue[ *Gestión de Procesos y Recursos*]")



    # =================================================================
    # 1. Mensajes y avisos del sistema.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF2_UD6_T1"
    with st.expander("1. Mensajes y avisos del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Notificaciones.",
            default_text="""
            Notificaciones que informan al usuario sobre el estado del SO, errores, advertencias o eventos importantes.
            **Ejemplo:** *El aviso de "Batería baja" o la notificación de que hay nuevas actualizaciones disponibles para instalar.*
            """,
            default_widget='default'
        )

    # =================================================================
    # 2. Eventos del sistema.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF2_UD6_T2"
    with st.expander("2. Eventos del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Visor de Eventos.",
            default_text="""
            Registros de actividades importantes (errores, advertencias, información) que ocurren en el SO. Se visualizan en el **Visor de Eventos**.
            **Ejemplo:** *Un registro de "Error" que indica la hora exacta en que un servicio del sistema dejó de funcionar inesperadamente.*
            """,
            default_widget='info'
        )

    # =================================================================
    # 3. Rendimiento del sistema.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF2_UD6_T3"
    with st.expander("3. Rendimiento del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Monitorización.",
            default_text="""
            Monitorización del uso de recursos como CPU, RAM, disco y red para identificar cuellos de botella y optimizar el funcionamiento.
            **Ejemplo:** *Observar un uso de CPU del 100% al ejecutar una aplicación, indicando un problema de rendimiento.*
            """
        )

    # =================================================================
    # 4. Administrador de tareas.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF2_UD6_T4"
    with st.expander("4. Administrador de tareas."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Procesos en ejecución.",
            default_text="""
            Herramienta para ver los procesos en ejecución, su consumo de recursos, y finalizar tareas que no responden (matar procesos).
            **Ejemplo:** *Usar el Administrador de Tareas para finalizar una aplicación que se ha quedado "colgada" y no responde.*
            """,
            default_widget='success'
        )

    # =================================================================
    # 5. Editor del registro del sistema.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF2_UD6_T5"
    with st.expander("5. Editor del registro del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Registro (Registry).",
            default_text="""
            Herramienta avanzada para modificar la base de datos de configuración del sistema (Windows Registry). Debe usarse con extrema **precaución**.
            **Ejemplo:** *Modificar un valor D-WORD en la clave `HKEY_CURRENT_USER` para cambiar un ajuste oculto del sistema.*
            """,
            default_widget='error'
        )
    st.divider()

if __name__ == '__main__':
    show_ud_2_6()