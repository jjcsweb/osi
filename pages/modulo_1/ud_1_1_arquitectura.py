import streamlit as st
from funciones.ui_manager import show_editable_content
from arquitectura import arquitectura
from fuentes.galeria_img.select_file import seleccion_urls
from funciones.mis_funciones import leer_markdown

NOTA_CHAT = leer_markdown("pages/nota_chat.md")


# --- Función Auxiliar para la Maquetación del Bloque Editable ---
# MODIFICADO: Añadido image_url_fija para la imagen estática
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""

    # 1. Título opcional para el bloque
    if sub_heading:
        st.markdown(f"##### {sub_heading}")

    # 2. Lógica del botón de edición (Posición discreta)
    edit_key = f'edit_{id_base}'
    # Importante: Streamlit verifica la existencia de la clave en session_state
    is_editing = st.session_state.get(edit_key, False)

    # Usamos las columnas para posicionar el botón.
    # El key 'btn_toggle_{id_base}' DEBE ser único en todo el script.
    col_btn, col_spacer = st.columns([2, 10])  # Ajustado el tamaño de la columna del botón para que no colisione.

    with col_btn:
        # Aquí es donde Streamlit encontró la clave duplicada.
        # Si se llama a la función dos veces con el mismo id_base, falla.
        if st.button("✏️" if not is_editing else "👁️", key=f'btn_toggle_{id_base}', type="secondary", width="stretch"):
            st.session_state[edit_key] = not is_editing
            st.rerun()

    # 3. Contenido editable
    show_editable_content(
        id_tema=id_base,
        titulo=topic_title,
        default_text=default_text,
        default_widget=default_widget,
        default_image_url_fija=image_url_fija  # Pasamos la URL estática
    )


# -------------------------------------------------------------
# ... (Función show_ud_1_1)
# ---------------------------------------------------------------
def show_ud_1_1():
    st.subheader(":blue[UNIDAD DIDACTICA 1.1 -- ]" + ":blue[ *Arquitecturas de un Sistema Microinformático*]")

    # Mostrar el carrusel de imagenes, llamando a un ficheros con URLs
    with st.expander(f":green[Mostrar el *CARRUSEL DE IMAGENES*]"):
        seleccion_urls()  # Aquí se llama al driver que gestiona el sidebar y muestra el carrusel


    # =================================================================
    # 1. Esquema funcional de un ordenador.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD1_T1"
    RUTA_IMAGEN_BUSES = "fuentes/imagenes/logo.jpg"  # Ruta de imagen estática

    with st.expander("1. Esquema funcional de un ordenador."):

        with st.popover("💬 Chat de Notas"):
            st.markdown("⬇️ Pulsa abajo para editar. Añade o consulta notas.")
            _render_editable_block(
                id_base=TEMA_ID_T1,
                topic_title="2. La unidad central de proceso y sus elementos.",
                default_text= NOTA_CHAT,
                default_widget='info',
                image_url_fija=RUTA_IMAGEN_BUSES  # Pasar la URL fija aquí
            )
        arquitectura.tabs_tema(TEMA_ID_T1)
        # Bloques de BD. Entradas de usuarios (estudiantes)



    # =================================================================
    # 2. La unidad central de proceso y sus elementos.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD1_T2"
    RUTA_IMAGEN_BUSES = "fuentes/imagenes/logo.jpg"  # Ruta de imagen estática

    with st.expander("2. La unidad central de proceso y sus elementos."):

        with st.popover("💬 Chat de Notas"):
            st.markdown("⬇️ Pulsa abajo para editar. Añade o consulta notas.")
            _render_editable_block(
                id_base=TEMA_ID_T2,
                topic_title="2. La unidad central de proceso y sus elementos.",
                default_text= NOTA_CHAT,
                default_widget='info',
                image_url_fija=RUTA_IMAGEN_BUSES  # Pasar la URL fija aquí

            )
        arquitectura.tabs_tema(TEMA_ID_T2)

    # =================================================================
    # 3. Buses.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF1_UD1_T3"
    RUTA_IMAGEN_BUSES = "fuentes/imagenes/logo.jpg"  # Ruta de imagen estática
    with st.expander("3. Buses."):

       with st.popover("💬 Chat de Notas"):
           st.markdown("⬇️ Pulsa abajo para editar. Añade o consulta notas.")
           _render_editable_block(
               id_base=TEMA_ID_T3,
               topic_title="3. Buses.",
               default_text=NOTA_CHAT,
               default_widget='info',
               image_url_fija=RUTA_IMAGEN_BUSES  # Pasar la URL fija aquí
           )
       arquitectura.tabs_tema(TEMA_ID_T3)

    # =================================================================
    # 4. Correspondencia entre los Subsistemas físicos y lógicos.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF1_UD1_T4"
    RUTA_IMAGEN_BUSES = "fuentes/imagenes/logo.jpg"  # Ruta de imagen estática

    with st.expander("4. Correspondencia entre los Subsistemas físicos y lógicos."):

        with st.popover("💬 Chat de Notas"):
            st.markdown("⬇️ Pulsa abajo para editar. Añade o consulta notas.")
            _render_editable_block(
                id_base=TEMA_ID_T4,
                topic_title="4. Correspondencia entre los Subsistemas físicos y lógicos.",
                default_text=NOTA_CHAT,
                default_widget='info',
                image_url_fija = RUTA_IMAGEN_BUSES # Pasar la URL fija aquí

            )
        arquitectura.tabs_tema(TEMA_ID_T4)
    st.divider()

if __name__ == '__main__':
    show_ud_1_1()