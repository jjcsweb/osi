# funciones/db_manager.py

import sqlite3
import json

DB_NAME = 'curso-osi.db'


def get_db_connection():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Acceso tipo diccionario
    return conn


def initialize_all_dbs():
    """Crea TODAS las tablas necesarias: notas, paginas y contenido."""
    conn = get_db_connection()
    c = conn.cursor()

    # 1. Tabla NOTAS (Editor de Texto)
    c.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            guia_id TEXT NOT NULL,
            titulo TEXT NOT NULL,
            contenido TEXT,
            fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            usuario TEXT,
            PRIMARY KEY (guia_id, titulo)
        );
    """)

    # 2. Tabla PAGINAS (Constructor)
    c.execute("""
        CREATE TABLE IF NOT EXISTS paginas (
            titulo_pagina TEXT PRIMARY KEY,
            estructura_json TEXT,
            creado_por TEXT,
            fecha_mod TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 3. Tabla CONTENIDO (Unidades Didácticas)
    c.execute("""
        CREATE TABLE IF NOT EXISTS contenido (
            id_tema TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            texto_md TEXT,
            tipo_widget TEXT
        );
    """)

    conn.commit()
    conn.close()


# --- SECCIÓN 1: NOTAS (Editor de Texto) ---

def get_note_titles(guia_id: str) -> list:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT titulo FROM notas WHERE guia_id = ? ORDER BY fecha_modificacion DESC;", (guia_id,))
    # Extraemos el string de la fila
    titulos = [row['titulo'] for row in c.fetchall()]
    conn.close()
    return titulos


def get_note_content(guia_id: str, titulo: str) -> str:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT contenido FROM notas WHERE guia_id = ? AND titulo = ?", (guia_id, titulo))
    res = c.fetchone()
    conn.close()
    return res['contenido'] if res else ""


def save_note(guia_id, titulo, contenido, usuario):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
    INSERT OR REPLACE INTO notas (guia_id, titulo, contenido, fecha_modificacion, usuario) 
    VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?);
    """, (guia_id, titulo, contenido, usuario))
    conn.commit()
    conn.close()


# --- SECCIÓN 2: PÁGINAS (Constructor) ---

def guardar_pagina(titulo, estructura, usuario):
    conn = get_db_connection()
    c = conn.cursor()
    json_data = json.dumps(estructura)
    c.execute("""
        INSERT OR REPLACE INTO paginas (titulo_pagina, estructura_json, creado_por, fecha_mod)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """, (titulo, json_data, usuario))
    conn.commit()
    conn.close()


def cargar_pagina_por_titulo(titulo: str) -> list:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT estructura_json FROM paginas WHERE titulo_pagina = ?", (titulo,))
    data = c.fetchone()
    conn.close()
    return json.loads(data['estructura_json']) if data and data['estructura_json'] else []


def get_lista_paginas() -> list:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT titulo_pagina FROM paginas")
    lista = [row['titulo_pagina'] for row in c.fetchall()]
    conn.close()
    return lista


def eliminar_pagina_por_titulo(titulo: str):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM paginas WHERE titulo_pagina = ?", (titulo,))
    conn.commit()
    conn.close()


# --- SECCIÓN 3: UNIDADES DIDÁCTICAS (UI Manager) ---

def load_content(id_tema: str) -> dict:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM contenido WHERE id_tema = ?", (id_tema,))
    row = c.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def save_content(id_tema: str, titulo: str, texto_md: str, tipo_widget: str = 'default'):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO contenido (id_tema, titulo, texto_md, tipo_widget)
        VALUES (?, ?, ?, ?)
    """, (id_tema, titulo, texto_md, tipo_widget))
    conn.commit()
    conn.close()