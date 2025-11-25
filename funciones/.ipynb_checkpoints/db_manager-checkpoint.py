import sqlite3

# Nombre de la base de datos central
DB_NAME = 'curso_osi.db'


def get_db_connection():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas como si fueran diccionarios
    return conn


def initialize_db():
    """Crea la tabla 'contenido' si no existe."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS contenido (
            id_tema TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            texto_md TEXT,
            tipo_widget TEXT  -- Ej: 'info', 'success', 'warning', 'columna_img', 'default'
        )
    """)
    conn.commit()
    conn.close()


def load_content(id_tema: str) -> dict or None:
    """Carga el contenido de un tema por su ID único."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM contenido WHERE id_tema = ?", (id_tema,))
    row = c.fetchone()
    conn.close()

    if row:
        # Devuelve el resultado como un diccionario
        return dict(row)
    return None


def save_content(id_tema: str, titulo: str, texto_md: str, tipo_widget: str = 'default'):
    """Inserta o actualiza el contenido de un tema."""
    conn = get_db_connection()
    c = conn.cursor()

    # Usa un UPSERT (INSERT OR REPLACE) para crear o actualizar el registro
    c.execute("""
        INSERT OR REPLACE INTO contenido (id_tema, titulo, texto_md, tipo_widget)
        VALUES (?, ?, ?, ?)
    """, (id_tema, titulo, texto_md, tipo_widget))

    conn.commit()
    conn.close()

# 💡 Importante: Llamar a initialize_db() una vez al inicio de la aplicación (por ejemplo, en app.py)
# initialize_db() # Lo haremos en app.py para asegurar que se crea la DB al arrancar.