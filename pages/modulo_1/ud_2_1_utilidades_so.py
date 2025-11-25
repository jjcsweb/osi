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

def show_ud_2_1():
    """Muestra el contenido de la UD 2.1: Utilidades del Sistema Operativo."""

    st.subheader(":blue[UNIDAD DIDACTICA 2.1 -- ]" ":blue[ *Utilidades del Sistema Operativo*]")



    # =================================================================
    # 1. Características y funciones.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF2_UD1_T1"
    with st.expander("1. Características y funciones de las utilidades."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Características y funciones.",
            default_text="""
            Programas integrados en el SO que realizan tareas específicas de mantenimiento, configuración o diagnóstico.
            **Ejemplo:** *Calculadora, Bloc de Notas, Paint, Herramienta Recortes, Desfragmentador, Liberador de espacio.*
            """,
            default_widget='info'
        )

    # =================================================================
    # 2. Configuración del entorno de trabajo.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF2_UD1_T2"
    with st.expander("2. Configuración del entorno de trabajo."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Configuración del entorno.",
            default_text="""
            Personalización del **Escritorio**, **Menú de Inicio**, **Barra de Tareas**, **tema visual**, etc., para adaptar el SO al usuario.
            **Ejemplo:** *Cambio del fondo de pantalla, configuración del modo oscuro, o reordenación de iconos en la barra de tareas.*
            """,
            default_widget='default'
        )

    # =================================================================
    # 3. Administración y gestión de los sistemas de archivo.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF2_UD1_T3"
    with st.expander("3. Administración y gestión de los sistemas de archivo."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Gestión de archivos.",
            default_text="""
            Uso de herramientas como el **Explorador de Archivos** para crear, copiar, mover, renombrar y eliminar archivos y carpetas.
            **Ejemplo:** *Utilizar atajos de teclado (Ctrl+C, Ctrl+V) para mover documentos entre directorios del disco C: a un pendrive.*
            """,
            default_widget='default'
        )

    # =================================================================
    # 4. Gestión de usuarios y recursos.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF2_UD1_T4"
    with st.expander("4. Gestión de usuarios y recursos."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Gestión de usuarios.",
            default_text="""
            Creación de **cuentas de usuario**, asignación de **permisos** y gestión de **dispositivos** compartidos.
            **Ejemplo:** *Crear una cuenta de "Invitado" con permisos limitados o asignar un permiso de "Solo Lectura" a una carpeta compartida.*
            """,
            default_widget='success'
        )

    # =================================================================
    # 5. Gestión y edición de archivos.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF2_UD1_T5"
    with st.expander("5. Gestión y edición de archivos."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Edición de archivos.",
            default_text="""
            Utilidades básicas para abrir, editar y guardar diferentes tipos de archivos (texto, imagen, etc.).
            **Ejemplo:** *Usar el Bloc de Notas para crear un archivo `.bat` o Paint para recortar una imagen en formato `.png`.*
            """,
            default_widget='default'
        )
    st.divider()

if __name__ == '__main__':
    show_ud_2_1()