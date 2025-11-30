# constructor.py

import streamlit as st
from fuentes.texto.paginas_builder import app_editor_paginas
from funciones.db_manager import initialize_all_dbs, sync_disk_to_db

st.set_page_config(layout="wide", page_title="Constructor")

# --- LÓGICA CRÍTICA: INICIALIZACIÓN DE ESTADO PARA MENSAJES ---
if 'sync_message' not in st.session_state:
    st.session_state['sync_message'] = None
if 'sync_type' not in st.session_state:
    st.session_state['sync_type'] = None
# -----------------------------------------------------------------

usuario = "admin@curso-osi.com"

# --- 1. VISUALIZAR EL RESULTADO DE LA SINCRONIZACIÓN (CUERPO PRINCIPAL) ---
# Si existe un mensaje en el estado de sesión, lo mostramos prominentemente
if st.session_state['sync_message']:
    if st.session_state['sync_type'] == 'success':
        st.success(st.session_state['sync_message'])
    elif st.session_state['sync_type'] == 'error':
        st.error(st.session_state['sync_message'])

    # NOTA: NO borramos el mensaje aquí. Se borrará o actualizará en el siguiente clic
    # para que sea visible hasta que el usuario sincronice de nuevo.

#st.markdown("---")
# ------------------------------------------------------------------------------------


# --- 2. BOTÓN DE SINCRONIZACIÓN (SIDEBAR) ---
st.sidebar.markdown("### 🛠️ Herramientas de Desarrollo")
if st.sidebar.button("🔄 Sincronizar Disco con DB"):

    # 💡 Limpiamos el estado al iniciar
    st.session_state['sync_message'] = "Iniciando sincronización..."
    st.session_state['sync_type'] = 'info'
    st.info("Iniciando sincronización...")  # Mensaje rápido en el main body

    # Prepara la DB y luego sincroniza
    initialize_all_dbs()
    # Deshabilitamos 'verbose' para no llenar la consola con logs si ya estamos mostrando el resumen en la UI.
    paginas, notas, contenido, errores = sync_disk_to_db(verbose=False)

    # 💡 Guardamos el resultado en st.session_state
    if errores:
        st.session_state[
            'sync_message'] = f"❌ Sincronización con errores. Páginas: {paginas}, Notas: {notas}, Contenido: {contenido}. Revisa la consola para los {len(errores)} errores."
        st.session_state['sync_type'] = 'error'
    else:
        st.session_state[
            'sync_message'] = f"✅ Sincronización completa. Páginas: {paginas}, Notas: {notas}, Contenido: {contenido}."
        st.session_state['sync_type'] = 'success'

    st.rerun()
# ------------------------------------------------------------------------------------

# 3. Ejecutar el Constructor
app_editor_paginas(usuario)