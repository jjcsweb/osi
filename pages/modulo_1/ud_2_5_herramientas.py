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

def show_ud_2_5():
    """Muestra el contenido de la UD 2.5: Utilización de las herramientas del sistema."""

    st.subheader(":blue[UNIDAD DIDACTICA 2.5 -- ]" ":blue[ *Utilización de las Herramientas del Sistema*]")


    # =================================================================
    # 1. Desfragmentado de disco.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF2_UD5_T1"
    with st.expander("1. Desfragmentado de disco."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Desfragmentador.",
            default_text="""
            Herramienta que optimiza la ubicación de los fragmentos de archivos en **discos HDD** para mejorar la velocidad de acceso. No es necesario en discos SSD.
            **Ejemplo:** *Ejecutar la utilidad "Optimizar Unidades" en Windows para consolidar el espacio libre.*
            """,
            default_widget='info'
        )

    # =================================================================
    # 2. Copias de seguridad.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF2_UD5_T2"
    with st.expander("2. Copias de seguridad (Backup)."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Copias de seguridad.",
            default_text="""
            Proceso para crear duplicados de datos importantes para su recuperación en caso de pérdida o corrupción.
            **Ejemplo:** *Realizar una copia de seguridad en un disco externo o en un servicio en la nube (Cloud Backup).*
            """,
            default_widget='success'
        )

    # =================================================================
    # 3. Liberación de espacio.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF2_UD5_T3"
    with st.expander("3. Liberación de espacio."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Liberar espacio.",
            default_text="""
            Utilidad para eliminar archivos innecesarios (temporales, caché, papelera de reciclaje) y liberar espacio en el disco duro.
            **Ejemplo:** *Usar el "Liberador de espacio en disco" de Windows para borrar archivos de instalación antiguos de actualizaciones.*
            """
        )

    # =================================================================
    # 4. Programación de tareas.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF2_UD5_T4"
    with st.expander("4. Programación de tareas."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Programador de tareas.",
            default_text="""
            Permite automatizar la ejecución de programas o scripts en momentos específicos o en respuesta a ciertos eventos del sistema.
            **Ejemplo:** *Configurar el sistema para que se ejecute una limpieza de disco todos los domingos a las 3:00 a.m.*
            """
        )

    # =================================================================
    # 5. Restauración del sistema. (Confirmado como elemento en el archivo original)
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF2_UD5_T5"
    with st.expander("5. Restauración del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Restaurar el sistema.",
            default_text="""
            Funcionalidad para revertir el estado del sistema a un punto de restauración anterior, deshaciendo cambios recientes que causaron inestabilidad.
            **Ejemplo:** *Restaurar el sistema después de que la instalación de un controlador de vídeo haya provocado fallos al iniciar.*
            """,
            default_widget='warning'
        )
    st.divider()

if __name__ == '__main__':
    show_ud_2_5()