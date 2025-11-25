import streamlit as st
from fuentes.texto.paginas_builder import app_editor_paginas
#from funciones.db_manager import initialize_all_dbs

st.set_page_config(layout="wide", page_title="Constructor")

# Simulación de usuario (o traer de autenticación real)
usuario = "admin@curso-osi.com"
#initialize_all_dbs()
app_editor_paginas(usuario)