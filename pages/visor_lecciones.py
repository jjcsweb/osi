import streamlit as st
# Importa la función de renderizado
from fuentes.texto.paginas_builder import mostrar_pagina
# Importa la función que lista las páginas guardadas
from funciones.db_manager import get_lista_paginas

# Configuración básica de la página
st.set_page_config(layout="wide", page_title="Visor de Lecciones")

st.subheader(f"📚 :blue[Visor de Contenido del Curso]")
#st.markdown("---")

# 1. Obtener la lista de todas las páginas construidas
lista_paginas = get_lista_paginas()

if not lista_paginas:
    st.warning("⚠️ No hay páginas construidas en la base de datos. Ve al 'Constructor de Páginas'.")
else:
    # 2. Selector para que el usuario elija qué página ver
    pagina_elegida = st.selectbox(
        "Selecciona la Lección a Visualizar:",
        options=lista_paginas,
        index=0 # Selecciona la primera por defecto
    )

    #st.markdown("---")

    # 3. Llamar a la función de renderizado para mostrar el contenido
    if pagina_elegida:
        # La función mostrar_pagina llama a cargar_pagina_por_titulo
        # y luego usa renderizar_bloque para cada elemento, incluyendo el PDF.
        mostrar_pagina(pagina_elegida)