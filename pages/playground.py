# pages/vista_leccion.py (Ejemplo de cómo usar la función)

import streamlit as st
# Importa la función de renderizado y la función que lista las páginas
from fuentes.texto.paginas_builder import mostrar_pagina
from funciones.db_manager import get_lista_paginas  # Para poblar el selector

st.set_page_config(layout="wide", page_title="Visor de Lecciones")


# --- LÓGICA DE VISUALIZACIÓN ---

def leccion_viewer():
    st.header("📚 Visor de Contenido del Curso")
    st.markdown("---")

    # 1. Obtener la lista de todas las páginas que has guardado en el constructor
    lista_paginas = get_lista_paginas()

    if not lista_paginas:
        st.warning("⚠️ No hay páginas construidas en la base de datos. ¡Ve al 'Constructor de Páginas'!")
        return

    # 2. Selector para que el usuario elija qué página ver
    pagina_elegida = st.selectbox(
        "Selecciona la Lección a Visualizar:",
        options=lista_paginas,
        key="selector_leccion_vista"
    )

    st.markdown("---")

    # 3. Llamar a la función de renderizado para mostrar el contenido de la página
    if pagina_elegida:
        # Aquí se usa la función que carga el JSON y renderiza los bloques
        mostrar_pagina(pagina_elegida)

    st.markdown("---")
    st.caption(f"Lección Actual: {pagina_elegida}")


# Ejecutar la función principal de esta página
leccion_viewer()