# fuentes/galeria_img/select_file.py

import streamlit as st
# Importación relativa dentro del paquete galeria_img
from .visor_carrusel import image_slider, select_url_file_sidebar


def seleccion_urls():
    """
    Gestiona la carga de URLs desde el sidebar y muestra el carrusel.
    """
    # 1. Selección del archivo de URLs (Llamada al sidebar)
    urls_to_load, selected_file_name = select_url_file_sidebar(key_id="carrusel")

    if urls_to_load:
        # 2. Llamada al Módulo (Widget) - Solo si hay contenido
        #st.markdown("---")
        image_slider(
            urls_to_load,
            slider_id="carrusel_arquitectura_ud1_1",
            #title_text=f":grey archivo con URLs: {selected_file_name}",


        )
    else:
        # Mensaje en la página principal (contenedora)
        st.info("Utiliza la barra lateral izquierda (⬅️) para subir el archivo de URLs y activar el carrusel.")