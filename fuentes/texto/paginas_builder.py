# fuentes/texto/paginas_builder.py

import streamlit as st
import json
import base64
from io import BytesIO
# import sqlite3 # Descomentar si es necesario en tu entorno

# IMPORTACIONES DEL MÓDULO CENTRALIZADO
from funciones.db_manager import (
    initialize_all_dbs,
    guardar_pagina,
    cargar_pagina_por_titulo,
    get_lista_paginas,
    get_note_content,
    get_note_titles,
    eliminar_pagina_por_titulo,
)

AREAS_TRABAJO = {"MF0219": "Configurar Sistemas", "MF0220": "Redes Locales", "MF0221": "Configurar Aplicaciones",
                 "MF0222": "Aplicaciones MicroInf"}


# --- Funciones auxiliares ---

def get_texto_nota(guia_id, titulo_nota):
    texto_real = get_note_content(guia_id, titulo_nota)
    return texto_real if texto_real else f"⚠️ Nota '{titulo_nota}' no encontrada en {guia_id}"


# --- RENDERIZADOR (CANVAS) ---

def renderizar_bloque(bloque, is_editor=True):
    tipo = bloque.get("tipo")
    contenido = bloque.get("contenido", "")

    if tipo == "titulo":
        st.title(contenido)
    elif tipo == "subtitulo":
        st.subheader(contenido)
    elif tipo == "texto":
        st.markdown(contenido)
    elif tipo in ["info", "success", "warning", "error"]:
        getattr(st, tipo)(contenido)

    # Bloques Avanzados
    elif tipo == "nota_bd":
        guia = bloque.get("guia_id")
        titulo_n = bloque.get("titulo_nota")
        texto_real = get_texto_nota(guia, titulo_n)
        with st.expander(f"📄 Nota DB: {titulo_n} ({guia})", expanded=True):
            st.markdown(texto_real)

    elif tipo == "youtube":
        st.video(contenido)

    elif tipo == "imagen_url":
        st.image(contenido, use_column_width=True)

    elif tipo == "imagen_local":
        base64_img = bloque.get("base64_data")
        mime_type = bloque.get("mime_type", "image/png")
        if base64_img:
            st.markdown(
                f'<img src="data:{mime_type};base64,{base64_img}" style="max-width: 100%; height: auto; border-radius: 5px;">',
                unsafe_allow_html=True)
        else:
            st.error("Imagen local no encontrada.")

    elif tipo == "pdf_local":
        base64_pdf = bloque.get("base64_data")
        file_name = bloque.get("file_name", "documento.pdf")

        if is_editor:
            st.info(f"PDF cargado: **{file_name}** (Visible en modo lectura)")
        else:
            if base64_pdf:
                st.markdown(f"##### 📄 {file_name}")
                # Opción 1: Iframe
                html_code = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500"></iframe>'
                st.components.v1.html(html_code, height=500)
                # Opción 2: Botón de descarga
                st.download_button("⬇️ Descargar PDF", data=base64.b64decode(base64_pdf), file_name=file_name,
                                   mime="application/pdf")
            else:
                st.error("PDF no encontrado.")

    elif tipo == "dos_columnas":
        c1, c2 = st.columns([1, 2])
        with c1:
            if bloque.get("img_url"):
                st.image(bloque["img_url"])
            else:
                st.info("Sin Imagen")
        with c2:
            st.markdown(bloque.get("texto_columna", ""))

    if is_editor:
        st.caption(f"🔹 {tipo}")


# --- CALLBACKS ---

def load_page_callback():
    seleccion = st.session_state["page_selector_widget_key"]
    if seleccion == "-- Nueva Página --":
        st.session_state["current_page_blocks"] = []
        st.session_state["current_page_title"] = ""
    else:
        st.session_state["current_page_blocks"] = cargar_pagina_por_titulo(seleccion)
        st.session_state["current_page_title"] = seleccion

    st.session_state["last_selection"] = seleccion


def delete_page_callback():
    titulo = st.session_state["page_selector_widget_key"]
    if titulo and titulo != "-- Nueva Página --":
        eliminar_pagina_por_titulo(titulo)
        st.toast(f"Borrada: {titulo}")
        # Reset
        st.session_state["current_page_blocks"] = []
        st.session_state["current_page_title"] = ""
        st.session_state["last_selection"] = "-- Nueva Página --"
        st.rerun()


# --- FUNCIÓN DE VISTA LECTURA ---

def mostrar_pagina(titulo_pagina: str):
    #st.title(titulo_pagina)
    #st.markdown("---")
    bloques = cargar_pagina_por_titulo(titulo_pagina)
    if not bloques:
        st.warning("Página vacía o no encontrada.")
        return
    for bloque in bloques:
        with st.container():
            renderizar_bloque(bloque, is_editor=False)


# --- APP PRINCIPAL ---

def app_editor_paginas(usuario_actual):
    initialize_all_dbs()

    st.subheader("🏗️ Constructor de Páginas")

    # Inicializar Session State
    if "current_page_blocks" not in st.session_state: st.session_state["current_page_blocks"] = []
    if "current_page_title" not in st.session_state: st.session_state["current_page_title"] = ""
    if "last_selection" not in st.session_state: st.session_state["last_selection"] = "-- Nueva Página --"
    if "page_selector_widget_key" not in st.session_state: st.session_state[
        "page_selector_widget_key"] = "-- Nueva Página --"

    # --- BARRA DE GESTIÓN (Alineada abajo) ---
    # ✅ AÑADIDO: vertical_alignment="bottom" para alinear botones con inputs
    col_sel, col_name, col_save, col_del = st.columns([2, 2, 1, 1], vertical_alignment="bottom")

    lista_pags = ["-- Nueva Página --"] + get_lista_paginas()

    idx = 0
    if st.session_state["last_selection"] in lista_pags:
        idx = lista_pags.index(st.session_state["last_selection"])

    # 1. Selector
    col_sel.selectbox("Seleccionar Página", lista_pags, index=idx, key="page_selector_widget_key",
                      on_change=load_page_callback)

    # 2. Input Nombre
    st.session_state["current_page_title"] = col_name.text_input("Nombre ID:",
                                                                 value=st.session_state["current_page_title"],
                                                                 key="page_title_input_key")

    # 3. Guardar
    if col_save.button("💾 Guardar", use_container_width=True, type="primary"):
        titulo = st.session_state["page_title_input_key"]
        if titulo:
            guardar_pagina(titulo, st.session_state["current_page_blocks"], usuario_actual)
            st.success("Guardado")
            st.session_state["last_selection"] = titulo
            st.rerun()
        else:
            st.error("Falta nombre")

    # 4. Borrar
    pagina_seleccionada = st.session_state.get("page_selector_widget_key")
    if pagina_seleccionada and pagina_seleccionada != "-- Nueva Página --":
        col_del.button("🗑️ Borrar", type="secondary", use_container_width=True, on_click=delete_page_callback)

    st.divider()

    # --- BARRA DE AÑADIR BLOQUES (Alineada abajo) ---
    with st.container(border=True):
        st.markdown("**➕ Añadir Bloque**")

        # ✅ AÑADIDO: vertical_alignment="bottom" para alinear el botón 'Añadir' con los inputs
        c1, c2, c3 = st.columns([1, 2, 1], vertical_alignment="bottom")

        TIPOS = ["Texto Markdown", "Título", "Subtítulo", "Caja Info", "Caja Éxito", "Caja Alerta",
                 "Nota de BD", "Vídeo YouTube", "Imagen (URL)", "Imagen (Local)", "PDF (Local)", "Dos Columnas"]

        tipo_sel = c1.selectbox("Tipo", TIPOS)

        contenido = ""
        extra = {}

        # Renderizado condicional de inputs
        if tipo_sel == "Nota de BD":
            guia = c2.selectbox("Guía", list(AREAS_TRABAJO.keys()))
            notas = get_note_titles(guia)
            nota = c2.selectbox("Nota", notas if notas else ["Sin notas"])
            extra = {"guia_id": guia, "titulo_nota": nota}
        elif tipo_sel in ["Vídeo YouTube", "Imagen (URL)"]:
            contenido = c2.text_input("URL")
        elif tipo_sel == "Dos Columnas":
            extra["img_url"] = c2.text_input("URL Imagen (Izq)")
            extra["texto_columna"] = c2.text_area("Texto (Der)", height=100)
        elif tipo_sel in ["Imagen (Local)", "PDF (Local)"]:
            f_type = ['png', 'jpg', 'jpeg'] if "Imagen" in tipo_sel else ['pdf']
            uploaded = c2.file_uploader(f"Subir archivo ({tipo_sel})", type=f_type)
            if uploaded:
                bytes_data = uploaded.read()
                b64 = base64.b64encode(bytes_data).decode("utf-8")
                extra = {
                    "base64_data": b64,
                    "mime_type": uploaded.type,
                    "file_name": uploaded.name
                }
        else:
            contenido = c2.text_input("Contenido")

        # Botón Añadir (Alineado abajo gracias a vertical_alignment="bottom")
        if c3.button("Añadir", use_container_width=True):
            bloque = {}

            # Mapeo simple
            mapa_tipos = {
                "Texto Markdown": "texto", "Título": "titulo", "Subtítulo": "subtitulo",
                "Caja Info": "info", "Caja Éxito": "success", "Caja Alerta": "warning",
                "Nota de BD": "nota_bd", "Vídeo YouTube": "youtube", "Imagen (URL)": "imagen_url",
                "Imagen (Local)": "imagen_local", "PDF (Local)": "pdf_local",
                "Dos Columnas": "dos_columnas"
            }
            bloque["tipo"] = mapa_tipos.get(tipo_sel)
            bloque["contenido"] = contenido
            bloque.update(extra)

            # Validación
            es_valido = True
            if bloque["tipo"] == "nota_bd" and not extra.get("titulo_nota"): es_valido = False
            if bloque["tipo"] in ["imagen_local", "pdf_local"] and not extra.get("base64_data"): es_valido = False

            if es_valido:
                st.session_state["current_page_blocks"].append(bloque)
                st.rerun()
            else:
                st.error("Faltan datos para crear el bloque")

    # --- LIENZO ---
    st.write("### 🎨 Lienzo")
    bloques = st.session_state["current_page_blocks"]

    if not bloques:
        st.info("Página vacía")

    for i, b in enumerate(bloques):
        cont = st.container(border=True)
        with cont:
            # Alineamos también los botones de control dentro del bloque
            col_a, col_b = st.columns([6, 1], vertical_alignment="top")  # Top aquí suele verse mejor para controles
            with col_a:
                renderizar_bloque(b, True)
            with col_b:
                if i > 0:
                    if st.button("⬆️", key=f"up{i}"):
                        bloques[i], bloques[i - 1] = bloques[i - 1], bloques[i]
                        st.rerun()
                if i < len(bloques) - 1:
                    if st.button("⬇️", key=f"down{i}"):
                        bloques[i], bloques[i + 1] = bloques[i + 1], bloques[i]
                        st.rerun()
                if st.button("🗑️", key=f"del{i}", type="secondary"):
                    bloques.pop(i)
                    st.rerun()