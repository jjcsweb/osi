# funciones/db_manager.py

import sqlite3
import json
import os
from typing import List, Dict, Any

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

def get_note_titles(guia_id: str) -> List[str]:
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

def _get_path_from_id(id_tema: str) -> str:
    """
    Convierte el ID del tema (MF0219_UF1_UD1_T1) en su ruta de directorio didáctica.
    
    Para ID didácticas (e.g., MF0219_UF1_UD1_T1): Genera 'pages/modulo_1/arquitectura'
    Para otros títulos (e.g., pagina_model): Genera 'pages_modelos_no_asignados'
    """
    
    # Mapeo Didáctico: Define la estructura de tu proyecto
    MAPEO_MODULOS = {
        "MF0219": "modulo_1"
    }
    MAPEO_UNIDADES = {
        "UD1": "arquitectura",
        # Añade más unidades aquí (ej: "UD2": "sistemas_operativos")
    }

    try:
        parts = id_tema.split('_') 
        # Requerimos al menos 4 partes para ser una ID didáctica completa
        if len(parts) < 4:
            raise ValueError("ID no estándar")

        mf_id = parts[0]  # MF0219
        ud_id = parts[2]  # UD1

        modulo_dir = MAPEO_MODULOS.get(mf_id)
        unidad_dir = MAPEO_UNIDADES.get(ud_id)
        
        if modulo_dir and unidad_dir:
            # Ruta final: 'pages/modulo_1/arquitectura'
            return os.path.join('pages', modulo_dir, unidad_dir)

    except (IndexError, ValueError):
        # Para casos como "pagina_model", usamos una carpeta de respaldo
        pass # Continúa para devolver la ruta por defecto
    
    # Directorio de fallback para páginas modelo o no mapeadas
    return 'pages_modelos_no_asignados'


def _save_json_file(titulo_pagina: str, json_data: str):
    """
    Guarda la estructura JSON en un archivo físico con la ruta y nomenclatura didáctica.
    """
    
    # 1. Determinar el directorio de destino
    target_dir = _get_path_from_id(titulo_pagina) # target_dir ahora está en minúsculas
    
    # 2. Generar nombre de archivo (MF0219_UF1_UD1_T1.json)
    file_name = f"{titulo_pagina}.json"

    # 3. Crear el directorio si no existe
    # La variable target_dir es local, por lo que está correctamente en snake_case
    os.makedirs(target_dir, exist_ok=True) 
    
    # 4. Ruta completa
    full_path = os.path.join(target_dir, file_name)

    # 5. Escribir el contenido
    try:
        # Usamos el string JSON ya serializado
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(json_data)
        print(f"✅ Archivo JSON guardado en: {full_path}")
    except Exception as e:
        # Se puede añadir logging más robusto aquí
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
    
    
    
## 🚀 Próximos Pasos

Para verificar que esto funcione, asegúrate de:

1.  **Reemplazar** el contenido de tu `db_manager.py` con el código anterior.
    
2.  **Ejecutar** la inicialización de la base de datos (simulado en el turno anterior) para crear la `"pagina_model"`.
    
3.  **Ejecutar** `constructor.py` para abrir el constructor de páginas. Si guardas la página `"pagina_model"`, debería crearse la carpeta `pages_modelos_no_asignados` con el archivo `pagina_model.json`.
    
4.  Si creas y guardas una nueva página con el título **`MF0219_UF1_UD1_T1`**, el sistema creará automáticamente la ruta **`pages/modulo_1/arquitectura`** y guardará el archivo **`MF0219_UF1_UD1_T1.json`** dentro.




