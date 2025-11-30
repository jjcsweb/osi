# funciones/db_manager.py

import sqlite3
import json
import os
from typing import List, Dict, Any

DB_NAME = 'curso-osi.db'


def get_db_connection():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
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

def get_note_titles(guia_id: str) -> List[str]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT titulo FROM notas WHERE guia_id = ? ORDER BY fecha_modificacion DESC;", (guia_id,))
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

# funciones/db_manager.py (Fragmento a actualizar)

def _get_path_from_id(id_tema: str) -> str:
    """
    Convierte el ID del tema (MF0219_UF1_UDX_TX) en su ruta de directorio real.
    """

    # --- CONFIGURACIÓN DE LA ESTRUCTURA DIDÁCTICA ---
    MAPEO_MODULOS = {
        "MF0219": "modulo_1",
        "MF0220": "modulo_2"  # Ejemplo futuro
    }

    # AQUÍ AGREGAS LAS NUEVAS UNIDADES A MEDIDA QUE CRECES
    MAPEO_UNIDADES = {
        "UD1": "arquitectura",
        "UD2": "funciones_so",  # <--- NECESARIO PARA QUE FUNCIONE AHORA
        "UD3": "gestion_procesos",  # Ejemplo futuro (según tu árbol de directorios)
        "UD4": "gestion_memoria",
        "UD5": "sistemas_archivos"
    }
    # -----------------------------------------------

    try:
        parts = id_tema.split('_')
        if len(parts) < 4:
            raise ValueError("ID no estándar")

        mf_id = parts[0]  # MF0219
        ud_id = parts[2]  # UD1, UD2...

        modulo_dir = MAPEO_MODULOS.get(mf_id)
        unidad_dir = MAPEO_UNIDADES.get(ud_id)

        if modulo_dir and unidad_dir:
            # Construye: pages/modulo_1/funciones_so
            return os.path.join('pages', modulo_dir, unidad_dir)

    except (IndexError, ValueError):
        pass

    return 'pages_modelos_no_asignados'


def _save_json_file(titulo_pagina: str, json_data: str):
    """
    Guarda la estructura JSON en un archivo físico con la ruta y nomenclatura didáctica.
    """

    target_dir = _get_path_from_id(titulo_pagina)
    file_name = f"{titulo_pagina}.json"

    os.makedirs(target_dir, exist_ok=True)

    full_path = os.path.join(target_dir, file_name)

    try:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(json_data)
        print(f"✅ Archivo JSON guardado en: {full_path}")
    except Exception as e:
        print(f"🚨 Error al guardar archivo JSON {full_path}: {e}")


def guardar_pagina(titulo: str, estructura: Dict[str, Any], usuario: str):
    """
    Guarda la estructura de la página en la DB y en un archivo JSON físico.
    """
    conn = get_db_connection()
    c = conn.cursor()
    # 1. Serializar la estructura a string JSON (indent=4 para legibilidad en el archivo)
    json_data = json.dumps(estructura, indent=4)

    # 2. Guardar en la base de datos
    c.execute("""
        INSERT OR REPLACE INTO paginas (titulo_pagina, estructura_json, creado_por, fecha_mod)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """, (titulo, json_data, usuario))

    # 3. Guardar en el archivo físico (NUEVO PASO)
    _save_json_file(titulo, json_data)

    conn.commit()
    conn.close()


def cargar_pagina_por_titulo(titulo: str) -> List[Dict[str, Any]]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT estructura_json FROM paginas WHERE titulo_pagina = ?", (titulo,))
    data = c.fetchone()
    conn.close()
    return json.loads(data['estructura_json']) if data and data['estructura_json'] else []


def get_lista_paginas() -> List[str]:
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


# --- SECCIÓN 4: SISTEMA DE SINCRONIZACIÓN (DISCO -> DB) ---

def _import_json_to_db_only(titulo: str, json_data: str, usuario: str = "System_Sync"):
    """
    Inserta el JSON directamente en la BD sin volver a generar el archivo físico.
    Se usa para la sincronización de arranque.
    """
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO paginas (titulo_pagina, estructura_json, creado_por, fecha_mod)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """, (titulo, json_data, usuario))
    conn.commit()
    conn.close()


def sync_disk_to_db(verbose=False):
    """
    Recorre la carpeta 'pages/', busca todos los archivos .json que cumplan
    con la nomenclatura (MF...) y actualiza la base de datos.
    Devuelve un reporte de lo sucedido.
    """
    root_dir = "pages"
    count_updated = 0
    errors = []

    # Recorremos recursivamente todas las carpetas dentro de 'pages'
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".json"):
                # Asumimos que el nombre del archivo (sin extensión) es el ID/Título
                titulo = filename.replace(".json", "")

                # Opcional: Filtrar para que solo procese temas reales (MF...)
                if not titulo.startswith("MF"):
                    continue

                full_path = os.path.join(dirpath, filename)

                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content_str = f.read()

                        # Validamos que sea JSON válido antes de insertar
                        json.loads(content_str)

                        # Insertamos solo en DB
                        _import_json_to_db_only(titulo, content_str)
                        count_updated += 1
                        if verbose:
                            print(f"🔄 Sincronizado: {titulo}")

                except Exception as e:
                    error_msg = f"Error en {filename}: {str(e)}"
                    errors.append(error_msg)
                    print(f"❌ {error_msg}")

    return count_updated, errors