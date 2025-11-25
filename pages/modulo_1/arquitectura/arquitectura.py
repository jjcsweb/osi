# pages/modulo_1/arquitectura/arquitectura.py

import streamlit as st
from funciones.mis_funciones import leer_markdown
# Importamos la función de renderizado del CMS y la lista de páginas
from fuentes.texto.paginas_builder import mostrar_pagina
from funciones.db_manager import get_lista_paginas


# --- MODIFICACIÓN CLAVE: AHORA ACEPTA UNA PÁGINA FIJA ---
def leccion_viewer(clave_unica, pagina_fija=None):
    """
    Visualizador de lecciones.
    - Si recibe 'pagina_fija': Carga esa página automáticamente (Modo Alumno/Final).
    - Si NO recibe 'pagina_fija': Muestra el selector para elegir (Modo Desarrollo/Exploración).
    """

    # 1. MODO AUTOMÁTICO (Lo que pediste para "pagina_model")
    if pagina_fija:
        # Verificamos si existe en la lista para evitar errores feos
        todas_las_paginas = get_lista_paginas()

        if pagina_fija in todas_las_paginas:
            # Renderizado directo sin selectores
            mostrar_pagina(pagina_fija)
        else:
            st.warning(
                f"⚠️ La página asignada a este tema ('{pagina_fija}') no se encuentra en la base de datos. Revisa el nombre en el Constructor.")
        return  # Salimos de la función aquí si es automático

    # 2. MODO MANUAL (Selector genérico - Se mantiene como fallback)
    lista_paginas = get_lista_paginas()
    with st.expander(f"📚 Selector Manual de Lecciones (Desarrollo)"):
        if not lista_paginas:
            st.warning("⚠️ No hay páginas construidas en la base de datos.")
            return

        # Clave dinámica para evitar conflictos
        key_selector = f"selector_leccion_vista_{clave_unica}"

        pagina_elegida = st.selectbox(
            "Elige una lección para visualizar:",
            options=lista_paginas,
            key=key_selector
        )

    if pagina_elegida:
        st.markdown("---")
        mostrar_pagina(pagina_elegida)
        st.caption(f"Visualizando: {pagina_elegida} | Contexto: {clave_unica}")


# --- (El resto de funciones auxiliares se mantienen igual) ---

def mod_dos_colum(file_md):
    contenido_markdown = leer_markdown(file_md)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""contenido_markdown, el que desees...""")
        with col2:
            st.write("Este es otro contenido.")
            st.image("fuentes/imagenes/hardware.png")


def titulo_tema(tema):
    if tema == "MF0219_UF1_UD1_T1":
        st.info(f"##### 1. Esquema funcional de un ordenador.- ")
    elif tema == "MF0219_UF1_UD1_T2":
        st.info(f"##### 2. La unidad central de proceso y sus elementos. ")
    elif tema == "MF0219_UF1_UD1_T3":
        st.info(f"##### 3. Buses de datos ")
    elif tema == "MF0219_UF1_UD1_T4":
        st.info(f"##### 4. Correspondencia entre los Subsistemas físicos y lógicos.")


# --- LÓGICA DE PESTAÑAS POR TEMA ---

def tabs_tema(tema):
    introduccion, desarrollo, ejercicios, practicas = st.tabs(
        [
            "Introducción",
            "Desarrollo",
            "Ejercicios",
            "Prácticas"
        ]
    )

    # ===================================================================
    # PESTAÑA "INTRODUCCION"
    # ===================================================================
    with introduccion:
        if tema == "MF0219_UF1_UD1_T1":
            titulo_tema(tema)
            contenido = leer_markdown("pages/modulo_1/arquitectura/esq_funcional.md")
            st.markdown(contenido)

        elif tema == "MF0219_UF1_UD1_T2":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)

        elif tema == "MF0219_UF1_UD1_T3":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)

        elif tema == "MF0219_UF1_UD1_T4":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        else:
            st.write("error")

    # =================================================================
    # PESTAÑA "DESARROLLO" (INTEGRACIÓN CMS AUTOMÁTICA)
    # =================================================================
    with desarrollo:

        if tema == "MF0219_UF1_UD1_T1":
            titulo_tema(tema)
            # 🚨 AQUÍ ESTÁ EL CAMBIO: Cargamos "pagina_model" automáticamente
            leccion_viewer(clave_unica=tema, pagina_fija="pagina_model")


        elif tema == "MF0219_UF1_UD1_T2":
            titulo_tema(tema)
            # Aquí podrías cargar otra página fija en el futuro, ej: "leccion_cpu"
            # Por ahora dejamos el contenido markdown antiguo o el viewer manual
            #contenido = leer_markdown("pages/pagina.md")
            #st.markdown(contenido)
            leccion_viewer(clave_unica=tema, pagina_fija="pagina_model")


        elif tema == "MF0219_UF1_UD1_T3":
            titulo_tema(tema)
            #contenido = leer_markdown("pages/pagina.md")
            #st.markdown(contenido)
            leccion_viewer(clave_unica=tema, pagina_fija="pagina_model")


        elif tema == "MF0219_UF1_UD1_T4":
            titulo_tema(tema)
            #contenido = leer_markdown("pages/pagina.md")
            #st.markdown(contenido)
            leccion_viewer(clave_unica=tema, pagina_fija="pagina_model")

        else:
            st.write("error")

    # =================================================================
    # PESTAÑA "EJERCICIOS"
    # =================================================================
    with ejercicios:
        if tema == "MF0219_UF1_UD1_T1":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        # ... (resto de lógica repetitiva sin cambios) ...
        elif tema == "MF0219_UF1_UD1_T2":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        elif tema == "MF0219_UF1_UD1_T3":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        elif tema == "MF0219_UF1_UD1_T4":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        else:
            st.write("error")

    # =================================================================
    # PESTAÑA "PRÁCTICAS"
    # =================================================================
    with practicas:
        if tema == "MF0219_UF1_UD1_T1":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        # ... (resto de lógica repetitiva sin cambios) ...
        elif tema == "MF0219_UF1_UD1_T2":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        elif tema == "MF0219_UF1_UD1_T3":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        elif tema == "MF0219_UF1_UD1_T4":
            titulo_tema(tema)
            contenido = leer_markdown("pages/pagina.md")
            st.markdown(contenido)
        else:
            st.write("error")