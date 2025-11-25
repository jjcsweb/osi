# notas.py

import streamlit as st
import sqlite3
import pandas as pd
from streamlit.components.v1 import html

# Importamos el módulo rediseñado
from fuentes.texto.area_texto import mostrar_area_texto

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Curso OSI | Gestor de Notas", page_icon="📝", layout="wide")

DB_FILE = "curso-osi.db"

# Diccionario de Áreas
AREAS_TRABAJO = {
    "Configurar Sistemas": "MF0219",
    "Redes Locales": "MF0220",
    "Configurar Aplicaciones": "MF0221",
    "Aplicaciones MicroInf": "MF0222",
    "Prácticas": "PRACTICAS",
    "Ayuda": "AYUDA"
}


# --- GESTIÓN DE USUARIO (Simulación) ---
def get_current_user():
    if "user_email" not in st.session_state:
        st.session_state["user_email"] = "invitado@curso-osi.com"
    return st.session_state["user_email"]


# --- FUNCIONES DB BASICAS ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            guia_id TEXT NOT NULL,  
            titulo TEXT NOT NULL,
            contenido TEXT,
            fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            usuario TEXT,
            PRIMARY KEY (guia_id, titulo)
        )
    """)
    # Migración de columna usuario
    cursor.execute("PRAGMA table_info(notas)")
    cols = [c[1] for c in cursor.fetchall()]
    if "usuario" not in cols:
        cursor.execute("ALTER TABLE notas ADD COLUMN usuario TEXT")
    conn.commit()
    conn.close()


def get_notes_dataframe(guia_id):
    conn = sqlite3.connect(DB_FILE)
    # Ordenamos por fecha de modificación para ver lo último arriba
    df = pd.read_sql_query("SELECT * FROM notas WHERE guia_id = ? ORDER BY fecha_modificacion DESC", conn,
                           params=(guia_id,))
    conn.close()
    return df


def delete_note(guia_id, titulo):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notas WHERE guia_id = ? AND titulo = ?", (guia_id, titulo))
    conn.commit()
    conn.close()


# --- INTERFAZ ---
init_db()
usuario_activo = get_current_user()

st.markdown(f"### :grey[📚 Editores Notas-Curso]")
st.markdown(f"Usuario activo: `{usuario_activo}`")


tabs_modulos = st.tabs(list(AREAS_TRABAJO.keys()))

for i, (nombre_area, clave_db) in enumerate(AREAS_TRABAJO.items()):
    with tabs_modulos[i]:

        # --- SECCIÓN 1: VISUALIZACIÓN (Ahora dentro de un Expander) ---
        # "Notas en MFXXX y Visualizacion esten en un desplegable"
        label_expander = f"📂 Ver biblioteca de notas: {nombre_area} (Clic para desplegar)"

        with st.expander(label_expander, expanded=True):

            col_lista, col_visor = st.columns([1.5, 2.5], gap="large")

            # Columna Izquierda: Grid de Notas
            with col_lista:
                st.markdown(f"**Listado de {clave_db}**")
                df_notas = get_notes_dataframe(clave_db)

                nota_seleccionada = None

                if not df_notas.empty:
                    event = st.dataframe(
                        df_notas[["titulo", "fecha_modificacion", "usuario"]],
                        use_container_width=True,
                        hide_index=True,
                        selection_mode="single-row",
                        on_select="rerun",
                        key=f"grid_{clave_db}"
                    )
                    rows = event.selection.rows
                    if rows:
                        nota_seleccionada = df_notas.iloc[rows[0]]
                else:
                    st.info("No hay notas guardadas.")

            # Columna Derecha: Visor
            with col_visor:
                st.markdown("**Visor de Contenido**")
                container_visor = st.container(height=400, border=True)

                with container_visor:
                    if nota_seleccionada is not None:
                        st.write(f"### {nota_seleccionada['titulo']}")
                        st.caption(f"Por: {nota_seleccionada['usuario']} | {nota_seleccionada['fecha_modificacion']}")
                        st.markdown("---")

                        contenido = nota_seleccionada['contenido']
                        if nota_seleccionada['titulo'].startswith("HTML:"):
                            st.download_button("⬇️ Descargar HTML", data=contenido,
                                               file_name=f"{nota_seleccionada['titulo']}.html", mime="text/html")
                        else:
                            st.markdown(contenido)
                    else:
                        st.write("👈 Selecciona una nota de la lista.")

                if nota_seleccionada is not None:
                    if st.button("🗑️ Borrar Nota Seleccionada", key=f"del_{clave_db}"):
                        delete_note(clave_db, nota_seleccionada['titulo'])
                        st.rerun()

        #st.divider()

        # --- SECCIÓN 2: CREACIÓN (Tabs: Editor | Subir) ---
        st.markdown(f"### :grey[📚 Agrega o Edita Contenido]")

        tab_text, tab_html = st.tabs(["Editor de Texto", "Subir HTML"])

        with tab_text:
            # Llamamos al componente rediseñado
            mostrar_area_texto(clave_db, f":grey[*Notas*]", usuario_activo)
            st.divider()

        with tab_html:
            st.info("Sube archivos .html generados externamente.")
            upl = st.file_uploader("Archivo HTML", type=['html'], key=f"upl_{clave_db}")
            if upl and st.button("Guardar HTML", key=f"save_html_{clave_db}"):
                # Lógica simplificada de guardado HTML
                try:
                    conn = sqlite3.connect(DB_FILE)
                    c = conn.cursor()
                    c.execute("INSERT OR REPLACE INTO notas (guia_id, titulo, contenido, usuario) VALUES (?, ?, ?, ?)",
                              (clave_db, f"HTML: {upl.name}", upl.read().decode('utf-8'), usuario_activo))
                    conn.commit()
                    conn.close()
                    st.success("HTML Guardado")
                except Exception as e:
                    st.error(str(e))
            st.divider()