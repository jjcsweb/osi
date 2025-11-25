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

def show_ud_2_2():
    """Muestra el contenido de la UD 2.2: Organización del disco y sistema de archivos."""

    st.subheader(":blue[UNIDAD DIDACTICA 2.2 -- ]" ":blue[ *Organización del disco y sistema de archivos*]")


    # =================================================================
    # 1. El sistema de archivos.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF2_UD2_T1"
    with st.expander("1. El sistema de archivos."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. El sistema de archivos.",
            default_text="""
            Estructura lógica que organiza la información en los dispositivos de almacenamiento. Define cómo se almacenan, nombran y acceden los archivos.
            **Ejemplo:** *NTFS* (Windows) vs *ext4* (Linux) y su gestión de permisos y tamaños máximos de archivo.
            """,
            default_widget='info'
        )

    # =================================================================
    # 2. Unidades lógicas de almacenamiento.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF2_UD2_T2"
    with st.expander("2. Unidades lógicas de almacenamiento."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Unidades lógicas.",
            default_text="""
            Representaciones de las particiones de un disco físico. Permiten al SO tratar el espacio de almacenamiento como unidades separadas.
            **Ejemplo:** *La unidad C: en Windows para el sistema operativo, o la carpeta /home en Linux para los archivos de usuario.*
            """
        )

    # =================================================================
    # 3. Estructuración de los datos.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF2_UD2_T3"
    with st.expander("3. Estructuración de los datos."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Jerarquía de directorios.",
            default_text="""
            Jerarquía de directorios (carpetas) y archivos para organizar la información de forma lógica y accesible. (Modelo de árbol invertido).
            **Ejemplo:** *Tener una carpeta principal "Proyectos" y dentro de ella, subcarpetas "2024", "2025", etc.*
            """
        )

    # =================================================================
    # 4. Tipos de ficheros.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF2_UD2_T4"
    with st.expander("4. Tipos de ficheros."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Ficheros y extensiones.",
            default_text="""
            Archivos clasificados por su contenido y propósito. Identificados por su extensión.
            **Ejemplo:** *`.exe` para archivos ejecutables, `.pdf` para documentos portables, `.jpg` para imágenes.*
            """,
            default_widget='warning'
        )

    # =================================================================
    # 5. Carpetas y archivos del sistema.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF2_UD2_T5"
    with st.expander("5. Carpetas y archivos del sistema."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Ficheros esenciales.",
            default_text="""
            Directorios y ficheros esenciales para el funcionamiento del SO, a menudo ocultos o protegidos para evitar modificaciones accidentales.
            **Ejemplo:** *`C:\Windows\System32` en Windows o `/bin` y `/etc` en Linux.*
            """
        )

    # =================================================================
    # 6. Estructura y configuración del explorador de archivos.
    # =================================================================
    TEMA_ID_T6 = "MF0219_UF2_UD2_T6"
    with st.expander("6. Estructura y configuración del explorador de archivos."):
        _render_editable_block(
            id_base=TEMA_ID_T6,
            topic_title="6. Explorador de archivos.",
            default_text="""
            Herramienta gráfica para navegar, gestionar y visualizar la estructura de archivos y carpetas del sistema.
            **Ejemplo:** *Configurar el Explorador para mostrar las extensiones de archivo o los archivos ocultos.*
            """
        )

    # =================================================================
    # 7. Operaciones con archivos.
    # =================================================================
    TEMA_ID_T7 = "MF0219_UF2_UD2_T7"
    with st.expander("7. Operaciones con archivos."):
        _render_editable_block(
            id_base=TEMA_ID_T7,
            topic_title="7. Operaciones básicas.",
            default_text="""
            Acciones básicas: **Crear**, **Copiar**, **Mover**, **Renombrar**, **Eliminar**, **Buscar** y **Modificar** propiedades de archivos y carpetas.
            **Ejemplo:** *Comprimir varios archivos en un `.zip` antes de enviarlos por correo electrónico.*
            """
        )

    # =================================================================
    # 8. Búsqueda de archivos.
    # =================================================================
    TEMA_ID_T8 = "MF0219_UF2_UD2_T8"
    with st.expander("8. Búsqueda de archivos."):
        _render_editable_block(
            id_base=TEMA_ID_T8,
            topic_title="8. Búsqueda avanzada.",
            default_text="""
            Funcionalidad para localizar ficheros por nombre, tipo, fecha de modificación o contenido, utilizando filtros y patrones.
            **Ejemplo:** *Usar la búsqueda avanzada para encontrar todos los archivos `.doc` modificados en la última semana.*
            """,
            default_widget='success'
        )
    st.divider()

if __name__ == '__main__':
    show_ud_2_2()