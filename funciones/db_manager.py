import sqlite3
import json
import os
import re
from typing import List, Dict, Any

DB_NAME = 'curso-osi.db'

# 💡 Directorio para guardar notas creadas DESDE la App
BASE_NOTES_DIR = os.path.join("pages", "_user_notes")
os.makedirs(BASE_NOTES_DIR, exist_ok=True)

# NUEVO: Directorio para páginas no asignadas (fallback)
FALLBACK_PAGES_DIR = "pages_modelos_no_asignados"
os.makedirs(FALLBACK_PAGES_DIR, exist_ok=True)

# Directorios raíz para escaneo (Ajustado para incluir el nuevo)
ROOT_SCAN_DIRS = ["pages", FALLBACK_PAGES_DIR]


def get_db_connection():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # CRÍTICO: Acceso por nombre de columna
    return conn


def initialize_all_dbs():
    """Crea TODAS las tablas necesarias."""
    conn = get_db_connection()
    c = conn.cursor()

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

    c.execute("""
        CREATE TABLE IF NOT EXISTS paginas (
            titulo_pagina TEXT PRIMARY KEY,
            estructura_json TEXT,
            creado_por TEXT,
            fecha_mod TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

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


# =================================================================
# --- SECCIÓN 1: NOTAS (Editor de Texto) ---
# =================================================================

def _get_note_path_and_filename(guia_id: str, titulo: str) -> str:
    """Calcula la ruta de guardado para notas nuevas."""
    safe_title = "".join(c for c in titulo if c.isalnum() or c in (' ', '_', '-')).rstrip()
    safe_title = safe_title.replace(' ', '_')
    target_dir = os.path.join(BASE_NOTES_DIR, guia_id)
    file_name = f"{safe_title}.md"
    os.makedirs(target_dir, exist_ok=True)
    return os.path.join(target_dir, file_name)


def save_note(guia_id: str, titulo: str, contenido: str, usuario: str):
    conn = get_db_connection()
    c = conn.cursor()

    # 1. DB
    c.execute("""
    INSERT OR REPLACE INTO notas (guia_id, titulo, contenido, fecha_modificacion, usuario) 
    VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?);
    """, (guia_id, titulo, contenido, usuario))

    # 2. Disco
    full_path = _get_note_path_and_filename(guia_id, titulo)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(contenido)

    conn.commit()
    conn.close()


def get_note_titles(guia_id: str) -> List[str]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT titulo FROM notas WHERE guia_id = ? ORDER BY fecha_modificacion DESC", (guia_id,))
    titulos = [row['titulo'] for row in c.fetchall()]
    conn.close()
    return titulos


def get_note_content(guia_id: str, titulo: str) -> str:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT contenido FROM notas WHERE guia_id = ? AND titulo = ?", (guia_id, titulo))
    res = c.fetchone()
    conn.close()
    return str(res['contenido']) if res and res['contenido'] is not None else ""


def delete_note(guia_id: str, titulo: str):
    conn = get_db_connection()
    c = conn.cursor()
    # 1. Borrar de DB
    c.execute("DELETE FROM notas WHERE guia_id = ? AND titulo = ?", (guia_id, titulo))

    # 2. Borrar de Disco (Intentamos borrar en la ruta predecible)
    try:
        full_path = _get_note_path_and_filename(guia_id, titulo)
        if os.path.exists(full_path):
            os.remove(full_path)
    except Exception as e:
        print(f"🚨 Error borrando MD: {e}")

    conn.commit()
    conn.close()


# =================================================================
# --- SECCIÓN 2: PÁGINAS (Constructor) ---
# =================================================================

def _get_path_from_id(id_tema: str) -> str:
    """
    Ruta inteligente basada en el ID (MF0219_UF1_UD2...).
    Determina si va a una carpeta específica o al fallback.
    """
    parts = id_tema.split('_')

    # Si tiene estructura estándar (ej: MF0219_UF1_UD1_T1)
    if len(parts) >= 3 and parts[0].startswith("MF"):
        mf_id = parts[0]
        ud_id = parts[2]

        # Mapeo de Módulos
        base_mod = "modulo_1" if mf_id == "MF0219" else "modulo_2"

        # Mapeo de Unidades
        mapa_unidades = {
            "UD1": "arquitectura",
            "UD2": "funciones_so",
            "UD3": "gestion_procesos",
        }

        carpeta_unidad = mapa_unidades.get(ud_id, "otros")
        return os.path.join("pages", base_mod, carpeta_unidad)

    # Fallback para páginas sin ID estándar (ej: pagina_model, MI_PAGINA)
    # 💥 CORRECCIÓN AQUÍ: Usamos el directorio de modelos no asignados
    return FALLBACK_PAGES_DIR


def _save_json_file(titulo_pagina: str, json_data: str):
    """Guarda el JSON en disco lanzando error si falla."""
    target_dir = _get_path_from_id(titulo_pagina)
    os.makedirs(target_dir, exist_ok=True)

    full_path = os.path.join(target_dir, f"{titulo_pagina}.json")

    print(f"[DB_MANAGER] Guardando JSON en: {full_path}")

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(json_data)


def guardar_pagina(titulo: str, estructura: List[Dict[str, Any]], usuario: str):
    conn = get_db_connection()
    c = conn.cursor()
    json_data = json.dumps(estructura, indent=4)

    # 1. Guardar en DB
    c.execute("""
        INSERT OR REPLACE INTO paginas (titulo_pagina, estructura_json, creado_por, fecha_mod)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """, (titulo, json_data, usuario))

    # 2. Guardar en Disco
    _save_json_file(titulo, json_data)

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

    # 1. Borrar de DB
    c.execute("DELETE FROM paginas WHERE titulo_pagina = ?", (titulo,))

    # 2. Borrar de Disco
    try:
        # Reconstruir la ruta donde DEBERÍA estar el archivo
        target_dir = _get_path_from_id(titulo)
        full_path = os.path.join(target_dir, f"{titulo}.json")

        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"[DB_MANAGER] 🗑️ JSON de página eliminado: {full_path}")
        else:
            print(f"[DB_MANAGER] ⚠️ JSON no encontrado en la ruta esperada: {full_path}")

    except Exception as e:
        print(f"🚨 Error borrando JSON del disco: {e}")

    conn.commit()
    conn.close()


# =================================================================
# --- SECCIÓN 3: CONTENIDO ---
# =================================================================

def load_content(id_tema: str) -> dict:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM contenido WHERE id_tema = ?", (id_tema,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None


def save_content(id_tema: str, titulo: str, texto_md: str, tipo_widget: str):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
    INSERT OR REPLACE INTO contenido (id_tema, titulo, texto_md, tipo_widget) 
    VALUES (?, ?, ?, ?);
    """, (id_tema, titulo, texto_md, tipo_widget))
    conn.commit()
    conn.close()


# =================================================================
# --- SECCIÓN 4: SINCRONIZACIÓN (Maestro) ---
# =================================================================

def _import_json_to_db_only(titulo: str, json_data: str):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO paginas (titulo_pagina, estructura_json) VALUES (?, ?)", (titulo, json_data))
    conn.commit()
    conn.close()


def _import_content_json_to_db_only(data: dict):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
    INSERT OR REPLACE INTO contenido (id_tema, titulo, texto_md, tipo_widget) 
    VALUES (?, ?, ?, ?);
    """, (data.get('id_tema'), data.get('titulo', ''), data.get('texto_md', ''), data.get('tipo_widget', 'default')))
    conn.commit()
    conn.close()


def _import_note_md_to_db_only(guia_id: str, titulo: str, contenido: str):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO notas (guia_id, titulo, contenido) VALUES (?, ?, ?)",
              (guia_id, titulo, contenido))
    conn.commit()
    conn.close()


def _infer_guia_id_from_path(file_path: str) -> str:
    match = re.search(r'(MF\d{4})', file_path, re.IGNORECASE)
    if match: return match.group(1).upper()
    if 'practicas' in file_path.lower(): return "PRACTICAS"
    if 'ayuda' in file_path.lower(): return "AYUDA"
    return os.path.basename(os.path.dirname(file_path)).upper()


def sync_disk_to_db(verbose: bool = True) -> tuple:
    """Escanea los directorios de páginas recursivamente buscando .json y .md"""
    count_paginas, count_notas, count_contenido = 0, 0, 0
    errors = []

    # 💥 CORRECCIÓN AQUÍ: Iteramos sobre los dos directorios raíz
    for root_dir in ROOT_SCAN_DIRS:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    # 1. JSON (Páginas/Contenido)
                    if filename.endswith(".json"):
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content_str = f.read()
                            data = json.loads(content_str)

                        if 'id_tema' in data:  # Es contenido
                            _import_content_json_to_db_only(data)
                            count_contenido += 1
                        else:  # Es página
                            titulo = filename.replace(".json", "")
                            _import_json_to_db_only(titulo, content_str)
                            count_paginas += 1

                    # 2. MARKDOWN (Notas)
                    elif filename.endswith(".md"):
                        if filename.lower() in ["readme.md", "pagina.md", "nota_chat.md"]: continue

                        titulo = filename.replace(".md", "")
                        guia_id = _infer_guia_id_from_path(full_path)

                        with open(full_path, 'r', encoding='utf-8') as f:
                            md_content = f.read()
                            _import_note_md_to_db_only(guia_id, titulo, md_content)
                            count_notas += 1

                except Exception as e:
                    errors.append(f"{filename}: {str(e)}")
                    if verbose: print(f"❌ Error sync {filename}: {e}")

    return count_paginas, count_notas, count_contenido, errors