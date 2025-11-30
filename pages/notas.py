import streamlit as st
import pandas as pd
import sqlite3
from funciones.db_manager import initialize_all_dbs, sync_disk_to_db, get_note_titles, get_note_content, delete_note
from fuentes.texto.area_texto import mostrar_area_texto

st.set_page_config(page_title="Gestor Notas", layout="wide")

AREAS_TRABAJO = {
    "Configurar Sistemas": "MF0219",
    "Redes Locales": "MF0220",
    "Configurar Aplicaciones": "MF0221",
    "Aplicaciones MicroInf": "MF0222",
    "Prácticas": "PRACTICAS",
    "Ayuda": "AYUDA"
}


def notas_page():
    # --- Sidebar ---

    st.sidebar.markdown(f"#### ⬇️:blue[Notas de:]")
    area_sel = st.sidebar.selectbox("Módulo:", list(AREAS_TRABAJO.keys()), key="main_area_sel")
    clave_db = AREAS_TRABAJO[area_sel]
    usuario = "admin@curso-osi.com"

    # --- Pestañas ---
    tab1, tab2 = st.tabs(["1. Estado", f"2. Gestor ({clave_db})"])

    # TAB 1: Estado
    with tab1:
        st.markdown(f"## :grey[Estado del Sistema]")
        st.info(f"Módulo Activo: {area_sel} ({clave_db})")
        if 'sync_msg' in st.session_state:
            st.success(st.session_state['sync_msg'])
        if st.button("🔄 Sincronizar Disco -> DB"):
            initialize_all_dbs()
            p, n, c, e = sync_disk_to_db(verbose=False)
            msg = f"✅ Sincronizado: {p} Páginas, {n} Notas, {c} Contenidos."
            if e: msg += f" ❌ {len(e)} Errores."
            st.session_state['sync_msg'] = msg
            st.rerun()

    # TAB 2: Gestor y Borrado (SIMPLIFICADO)
    with tab2:
        colA, colB = st.columns([1, 2])

        # Recuperamos títulos
        titulos = get_note_titles(clave_db)

        with colA:
            st.subheader("🔎 Seleccionar Nota")
            # SOLUCIÓN SENCILLA: Un selectbox normal en lugar de tabla
            if titulos:
                nota_a_borrar = st.selectbox(
                    "Elige una nota para ver o borrar:",
                    options=["-- Seleccionar --"] + titulos,
                    key="sel_borrado"
                )
            else:
                st.info("No hay notas guardadas.")
                nota_a_borrar = "-- Seleccionar --"


        with colB:
            st.subheader("⚙️ Acciones")
            if nota_a_borrar and nota_a_borrar != "-- Seleccionar --":
                # Recuperamos contenido para confirmar que es la correcta
                contenido = get_note_content(clave_db, nota_a_borrar)

                with st.expander("👁️ Vista Previa", expanded=True):
                    st.markdown(contenido[:300] + "..." if len(contenido) > 300 else contenido)

                # BOTÓN DE BORRADO
                st.write("")
                if st.button("🗑️ ELIMINAR ESTA NOTA", type="primary"):
                    delete_note(clave_db, nota_a_borrar)
                    st.success(f"Nota '{nota_a_borrar}' eliminada.")
                    st.rerun()
            else:
                st.caption("Selecciona una nota a la izquierda para habilitar el borrado.")

        st.divider()
        st.subheader("📝 Crear / Editar Nota")
        # El editor sigue funcionando igual
        mostrar_area_texto(clave_db, "-- Nueva Nota --", usuario)
        st.divider()




if __name__ == "__main__":
    notas_page()