# Script de Inicialización (NO en db_manager.py, es un script aparte)
from funciones.db_manager import initialize_all_dbs, guardar_pagina
import  streamlit as st


# 1. Inicializar Tablas
initialize_all_dbs()

# 2. Definir la estructura del modelo simple
estructura_modelo = [
    {
        "tipo": "titulo",
        "contenido": "Contenido Principal del Tema"
    },
    {
        "tipo": "markdown",
        "contenido": "Este contenido es el corazón de la lección. Reemplaza este texto con el desarrollo completo del tema didáctico.\n\nAquí puedes usar **Markdown** para formato avanzado."
    },
    {
        "tipo": "alerta",
        "variante": "success",
        "contenido": "Modelo de página creado con éxito. Ahora puedes editarlo desde el Constructor."
    }
]

# 3. Guardar la página en la DB (titulo debe ser "pagina_model" para que arquitectura.py la use)


st.write("Script de un solo uso. Vacia base de datos")

check = st.text_input("Borrar base de datos ? si/no")
if check == "si":
    guardar_pagina(
        titulo="pagina_model",
        estructura=estructura_modelo,
        usuario="Sistema_Ingeniero"
    )
    st.success("Base de datos inicializada y 'pagina_model' creada.")
else:
    st.warning("No se ha realizado ninguna funcion")

