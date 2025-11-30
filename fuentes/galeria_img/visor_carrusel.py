# fuentes/galeria_img/visor_carrusel.py

import streamlit as st
from PIL import Image
import io
import requests


# --- Funciones de Navegación ---

def _next_image(key_suffix):
    """Avanza el índice específico del slider."""
    session_key_index = f'current_index_{key_suffix}'
    session_key_list = f'slider_image_list_{key_suffix}'

    if st.session_state[session_key_index] < len(st.session_state[session_key_list]) - 1:
        st.session_state[session_key_index] += 1


def _prev_image(key_suffix):
    """Retrocede el índice específico del slider."""
    session_key_index = f'current_index_{key_suffix}'

    if st.session_state[session_key_index] > 0:
        st.session_state[session_key_index] -= 1


# --- Widget Principal: El Slider ---

def image_slider(urls_list, slider_id, title_text=None):
    """
    Renderiza un slider de imágenes compacto y modular.

    Args:
        urls_list (list): Lista de strings de URLs de imágenes.
        slider_id (str): Identificador único para el estado de sesión (ej: 'arquitectura_carrusel').
        title_text (str, optional): Título opcional para el carrusel.
    """

    # 1. Inicialización de Estado de Sesión con ID único
    session_key_index = f'current_index_{slider_id}'
    session_key_list = f'slider_image_list_{slider_id}'

    if session_key_index not in st.session_state:
        st.session_state[session_key_index] = 0

    st.session_state[session_key_list] = urls_list

    if not st.session_state[session_key_list]:
        st.info("No hay URLs válidas para mostrar en este carrusel.")
        return

    current_idx = st.session_state[session_key_index]
    total_images = len(st.session_state[session_key_list])
    current_url = st.session_state[session_key_list][current_idx]

    if title_text:
        st.subheader(title_text)

    # Diseño de tres columnas para la navegación y la imagen (1, 3, 1)
    col_prev, col_image, col_next = st.columns([1, 3, 1])

    # 2. Obtener Imagen y Metadatos
    metadata_caption = ""

    try:
        # Descargar la imagen
        response = requests.get(current_url, timeout=5)
        response.raise_for_status()

        # Cargar con PIL para metadatos
        image_data = io.BytesIO(response.content)
        image_pil = Image.open(image_data)

        # Solución de compatibilidad: Usar PIL .thumbnail() para reducir la altura máxima a 350px
        MAX_COMPACT_HEIGHT = 350
        image_pil.thumbnail((9999, MAX_COMPACT_HEIGHT))

        # Extracción y Formateo de Metadatos
        width, height = image_pil.size
        format_str = image_pil.format
        mode_str = image_pil.mode
        image_data.seek(0)
        size_bytes = len(image_data.read())
        size_str = f"{size_bytes / 1024:.2f} KB" if size_bytes > 1024 else f"{size_bytes} B"

        # Metadatos simplificados
        metadata_caption = (
            f"URL: {current_url}\n"
            f"🖼️ Formato: {format_str} | Dimensiones: {width}x{height} px | Tamaño: {size_str}"
        )

    except Exception as e:
        col_image.error(f"Error al cargar imagen para la URL: {current_url}")
        return

    # 3. Visualización de la Imagen Actual (columna central)
    with col_image:
        st.markdown(
            f"<h5 style='text-align: center;'>{current_idx + 1} / {total_images}</h5>",
            unsafe_allow_html=True
        )
        st.image(
            image_pil,
            caption=metadata_caption,
            use_container_width=True,
            width=400,

            )

    # 4. Botones de Navegación (Centrados)
    with col_prev:
        c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
        with c2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.button(
                "❮ Anterior",
                # FIX: Corrección de on_on_click a on_click
                on_click=_prev_image,
                args=(slider_id,),
                disabled=(current_idx == 0),
                use_container_width=True,
                key=f'prev_btn_{slider_id}'
            )

    with col_next:
        c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
        with c2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.button(
                "Siguiente ❯",
                on_click=_next_image,
                args=(slider_id,),
                disabled=(current_idx == total_images - 1),
                use_container_width=True,
                key=f'next_btn_{slider_id}'
            )


# --- Sistema de Selección de Archivo en Sidebar ---

def select_url_file_sidebar(key_id):
    """
    Crea la interfaz de selección de archivo en el st.sidebar y devuelve las URLs.
    """
    with st.sidebar:
        st.markdown(f"### ⚙️:blue[Carrusel]")

        #st.markdown("📁 Archivo de URLs")
        with st.expander("⬆️ Archivos URLs", expanded=False):
            uploaded_file = st.file_uploader(
                "Sube un archivo .txt con URLs",
                type=['txt'],
                key=f'file_uploader_sidebar_{key_id}',
                help="Sube tu archivo de configuración de URLs (una URL por línea)."
        )

        urls_list = []
        file_name = "Ninguno"
        st.divider()

        if uploaded_file is not None:
            try:
                file_content = uploaded_file.getvalue().decode("utf-8")
                urls_list = [line.strip() for line in file_content.split('\n') if line.strip()]
                file_name = uploaded_file.name
                st.success(f"Archivo **{file_name}** cargado.")
            except Exception as e:
                st.error(f"Error al leer el archivo subido: {e}")

        return urls_list, file_name