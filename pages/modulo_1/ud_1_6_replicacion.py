import streamlit as st
from funciones.ui_manager import show_editable_content


# --- Función Auxiliar para la Maquetación del Bloque Editable ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""

    if sub_heading:
        st.markdown(f"##### {sub_heading}")

    edit_key = f'edit_{id_base}'
    is_editing = st.session_state.get(edit_key, False)

    col_btn, col_spacer = st.columns([1, 10])

    with col_btn:
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary",
                     width="content"):
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

def show_ud_1_6():
    """Muestra el contenido de la UD 1.6: Replicación física de particiones y discos duros."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.6 -- ]" ":blue[ *Replicación física de particiones y discos duros*]")

    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # =================================================================
    # 1. Programas de copia de seguridad.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD6_T1"
    with st.expander("1. Programas de copia de seguridad."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Programas de copia de seguridad.",
            default_text="Herramientas diseñadas para duplicar datos y permitir su restauración. Ejemplos: Cobian Backup, Veeam, herramientas nativas del SO. Diferencian entre copia completa, incremental y diferencial.",
            default_widget='default'
        )

    # =================================================================
    # 2. Clonación.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD6_T2"
    with st.expander("2. Clonación."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Clonación.",
            default_text="Proceso de copia exacta (bit a bit o a nivel de archivo) de un disco o partición a otro. Permite replicar un sistema operativo completo con todas sus configuraciones y programas.",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # =================================================================
    # 3. Funcionalidad y objetivos del proceso de replicación.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF1_UD6_T3"
    with st.expander("3. Funcionalidad y objetivos del proceso de replicación."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Objetivos de la replicación.",
            default_text="Los objetivos principales son: despliegue rápido de equipos (aulas, empresas), estandarización de configuraciones (maquetas) y recuperación rápida ante desastres.",
            default_widget='info'
        )

    # =================================================================
    # 4. Seguridad y prevención en el proceso de replicación.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF1_UD6_T4"
    with st.expander("4. Seguridad y prevención en el proceso de replicación."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Seguridad en la replicación.",
            default_text="Al clonar, se copian identificadores únicos (SIDs). Es vital usar herramientas como Sysprep (en Windows) para generalizar la imagen y evitar conflictos de seguridad en la red.",
            default_widget='warning'
        )

    # =================================================================
    # 5. Particiones de discos.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF1_UD6_T5"
    with st.expander("5. Particiones de discos."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Particiones de discos.",
            default_text="Gestión de la estructura del disco (tablas MBR vs GPT). La replicación puede implicar redimensionar particiones si el disco destino tiene un tamaño diferente al origen.",
            default_widget='default'
        )

    # =================================================================
    # 6. Herramientas de creación e implantación de imágenes.
    # =================================================================
    TEMA_ID_T6 = "MF0219_UF1_UD6_T6"
    with st.expander("6. Herramientas de creación e implantación de imágenes y réplicas de sistemas."):
        _render_editable_block(
            id_base=TEMA_ID_T6,
            topic_title="6. Herramientas de imágenes.",
            default_text="Software especializado para crear y desplegar imágenes: Clonezilla (Software Libre), Norton Ghost (Legacy), Acronis True Image, Microsoft Deployment Toolkit (MDT).",
            default_widget='success'
        )

    st.divider()


if __name__ == '__main__':
    show_ud_1_6()