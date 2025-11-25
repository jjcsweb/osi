import streamlit as st
from PIL import Image
import io
import requests
import base64

# --- 1. Inicialización del Estado de Sesión ---

if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0
if 'image_list' not in st.session_state:
    st.session_state['image_list'] = []
# Clave para el widget de área de texto, usada para su valor por defecto
if 'urls_text_area' not in st.session_state:
    st.session_state[
        'urls_text_area'] = "https://picsum.photos/800/600?image=10\nhttps://picsum.photos/800/600?image=20\nhttps://picsum.photos/800/600?image=30"
# Clave para el widget de área de texto, usada para forzar su actualización
if 'urls_text_area_key' not in st.session_state:
    st.session_state['urls_text_area_key'] = 0

st.markdown(f"#### 🖼️ Visor de Galería de Imágenes Avanzado (v3)")
st.caption("Carga URLs (directamente o por archivo), navega y visualiza metadatos.")


# --- 2. Funciones de Navegación y Carga ---

def next_image():
    """Avanza al siguiente índice, si es posible."""
    if st.session_state['current_index'] < len(st.session_state['image_list']) - 1:
        st.session_state['current_index'] += 1


def prev_image():
    """Retrocede al índice anterior, si es posible."""
    if st.session_state['current_index'] > 0:
        st.session_state['current_index'] -= 1


def load_images_from_urls(urls_text):
    """Procesa el texto de las URLs, las valida y las guarda en el estado de sesión."""

    urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
    st.session_state['image_list'] = []
    st.session_state['current_index'] = 0

    if not urls:
        st.error("🚨 No se ha introducido ninguna URL.")
        return

    status_placeholder = st.empty()
    status_placeholder.info(f"🔎 Validando y cargando {len(urls)} URLs...")

    valid_urls_count = 0

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            content_type = response.headers.get('Content-Type', '')
            if 'image' not in content_type:
                raise IOError("El Content-Type no parece ser una imagen.")

            st.session_state['image_list'].append(url)
            valid_urls_count += 1

        except (requests.exceptions.RequestException, IOError) as e:
            # URL descartada
            pass

    if st.session_state['image_list']:
        status_placeholder.success(f"✅ Se cargaron {valid_urls_count} de {len(urls)} URLs exitosamente.")
    else:
        status_placeholder.error("🚨 No se pudo cargar ninguna imagen de las URLs proporcionadas.")


def load_urls_from_file():
    """Carga URLs desde un archivo subido o vacía el estado si el archivo es eliminado."""

    uploaded_file = st.session_state.get('url_uploader')

    if uploaded_file is not None:
        try:
            # Caso 1: Archivo subido. Cargar contenido en el área de texto.
            file_content = uploaded_file.getvalue().decode("utf-8")

            st.session_state['urls_text_area'] = file_content
            st.session_state['urls_text_area_key'] += 1  # Forzar re-renderización

            st.success("Archivo de URLs cargado con éxito en el área de texto. Haz clic en 'Cargar Galería'.")
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")

    else:
        # Caso 2: Archivo eliminado (None). Limpiar el visualizador y el área de texto.

        # Limpiar la galería para que desaparezca
        st.session_state['image_list'] = []
        st.session_state['current_index'] = 0

        # Limpiar el área de texto y forzar re-renderización
        st.session_state['urls_text_area'] = ""
        st.session_state['urls_text_area_key'] += 1

        st.info("Archivo de URLs eliminado. El visualizador y el área de texto se han vaciado.")


# --- 3. Interfaz de Usuario: Carga y Guardado ---

with st.expander("🔗 Cargar URLs, Archivos y Opciones de Guardado", expanded=True):
    col_input, col_load_file, col_download = st.columns([2, 1, 1])

    # Columna Izquierda: Área de Texto
    with col_input:
        urls_input = st.text_area(
            "Introduce una URL por línea:",
            value=st.session_state['urls_text_area'],
            height=150,
            key=f'urls_text_area_{st.session_state["urls_text_area_key"]}'  # Clave dinámica
        )

    # Columna Central: Carga de Archivo
    with col_load_file:
        st.file_uploader(
            "Cargar archivo de URLs (.txt)",
            type=['txt'],
            on_change=load_urls_from_file,
            key='url_uploader'
        )

    # Columna Derecha: Botones de Carga y Guardado
    with col_download:
        st.markdown("<br>", unsafe_allow_html=True)

        # Botón 1: Cargar Galería
        st.button(
            "Cargar Galería 🚀",
            on_click=load_images_from_urls,
            args=(urls_input,),
            use_container_width=True
        )

        # Botón 2: Guardar
        urls_to_save = urls_input.encode('utf-8')
        st.download_button(
            label="💾 Guardar URLs",
            data=urls_to_save,
            file_name="galeria_urls.txt",
            mime="text/plain",
            help="Guarda todas las URLs del área de texto.",
            use_container_width=True
        )

st.markdown("---")

# --- 4. Galería de Visualización y Metadatos ---

if st.session_state['image_list']:

    current_idx = st.session_state['current_index']
    total_images = len(st.session_state['image_list'])
    current_url = st.session_state['image_list'][current_idx]

    # Diseño de tres columnas para la navegación y la imagen (1, 3, 1)
    col_prev, col_image, col_next = st.columns([1, 3, 1])

    # 4.1. Visualización de la Imagen Actual (en la columna central)
    with col_image:
        # Indicador arriba de la imagen
        st.markdown(
            f"<h4 style='text-align: center;'>{current_idx + 1} / {total_images}</h4>",
            unsafe_allow_html=True
        )
        try:
            # Obtenemos la imagen para mostrar y para metadatos
            response = requests.get(current_url, timeout=5)
            image_data = io.BytesIO(response.content)
            image_pil = Image.open(image_data)

            # Muestra la imagen
            st.image(
                image_pil,
                caption=f"URL: {current_url}",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error al mostrar la imagen o metadatos: {e}")

    # 4.2. Botones de Navegación (Centrados)
    with col_prev:
        c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
        with c2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.button(
                "❮ Anterior",
                on_click=prev_image,
                disabled=(current_idx == 0),
                use_container_width=True
            )

    with col_next:
        c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
        with c2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.button(
                "Siguiente ❯",
                on_click=next_image,
                disabled=(current_idx == total_images - 1),
                use_container_width=True
            )

    # 4.3. Metadatos de la Imagen
    if 'image_pil' in locals():
        st.markdown("---")

        metadata_cols = st.columns(4)

        metadata_cols[0].metric("Formato", image_pil.format)
        metadata_cols[1].metric("Dimensiones (Ancho x Alto)", f"{image_pil.width} x {image_pil.height} px")
        metadata_cols[2].metric("Modo de Color", image_pil.mode)

        # Calcular un tamaño estimado del archivo (no es exacto sin el archivo original)
        image_data.seek(0)
        size_kb = len(image_data.read()) / 1024
        metadata_cols[3].metric("Tamaño Estimado", f"{size_kb:.2f} KB")


else:
    st.info("⬆️ Introduce las URLs o carga un archivo y haz clic en 'Cargar Galería' para empezar.")