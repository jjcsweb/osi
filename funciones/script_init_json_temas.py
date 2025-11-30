# inicializar_temas.py
# Ejecuta este script una vez para generar los ficheros .json faltantes
"""Resumen de la Estrategia para Futuras Unidades
Cuando quieras atacar la UD3 (Gestión de Procesos), solo tendrás que:

Carpeta: Crear la carpeta física pages/modulo_1/gestion_procesos (o como se llame).

Mapeo: Ir a db_manager.py y añadir "UD3": "gestion_procesos".

Generar: Añadir los IDs (MF0219_UF1_UD3_T1, etc.) al script inicializar_temas.py y ejecutarlo.

UI: Crear el archivo ud_1_3_gestion_procesos.py copiando la estructura de los anteriores."""
from funciones.db_manager import guardar_pagina, initialize_all_dbs

# 1. Aseguramos que las tablas existan
initialize_all_dbs()

# 2. Definimos el contenido base para los temas nuevos
estructura_base = [
    {
        "tipo": "titulo",
        "contenido": "Título del Tema (Pendiente de Edición)"
    },
    {
        "tipo": "alerta",
        "variante": "info",
        "contenido": "Este tema ha sido generado automáticamente. Usa el botón 'Editar' para añadir contenido."
    }
]

# 3. LISTA DE TEMAS A GENERAR (Añade aquí los que necesites para UD2, UD3...)
temas_a_crear = [
    # UNIDAD 2: Funciones SO
    "MF0219_UF1_UD2_T1", # Conceptos básicos
    "MF0219_UF1_UD2_T2", # Funciones del SO
    # "MF0219_UF1_UD2_T3", # Si existiera...
]

print("🚀 Iniciando generación de temas...")

for tema_id in temas_a_crear:
    print(f"   > Generando: {tema_id}...", end=" ")
    try:
        # Esto guardará en DB y CREARÁ el archivo en pages/modulo_1/funciones_so/
        guardar_pagina(
            titulo=tema_id,
            estructura=estructura_base,
            usuario="Script_Inicializador"
        )
        print("✅ OK")
    except Exception as e:
        print(f"❌ ERROR: {e}")

print("\n✨ Proceso finalizado. Verifica la carpeta 'pages/modulo_1/funciones_so'.")