import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="Gestor de Archivos", layout="wide")

st.title("📁 Gestor de Archivos")
st.markdown("---")

# Crear carpeta de almacenamiento si no existe
UPLOAD_DIR = "/osi/uploads"
#Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
st.write("El valor de UPLOAD_DIR es: ", UPLOAD_DIR)
# Pestañas
tab1, tab2, tab3 = st.tabs(["📤 Cargar Archivos", "📥 Descargar Archivos", "📋 Ver Archivos"])

# TAB 1: CARGAR ARCHIVOS
with tab1:
    st.subheader("Carga tus archivos")
    
    uploaded_files = st.file_uploader(
        "Elige uno o varios archivos",
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} archivo(s) seleccionado(s)")
        
        if st.button("💾 Guardar archivos"):
            for uploaded_file in uploaded_files:
                file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"📄 Guardado: {uploaded_file.name}")
    else:
        st.info("ℹ️ Selecciona archivos para cargarlos")

# TAB 2: DESCARGAR ARCHIVOS
with tab2:
    st.subheader("Descarga tus archivos")
    
    files_in_dir = os.listdir(UPLOAD_DIR) if os.path.exists(UPLOAD_DIR) else []
    
    if files_in_dir:
        selected_file = st.selectbox("Elige un archivo para descargar:", files_in_dir)
        
        if selected_file:
            file_path = os.path.join(UPLOAD_DIR, selected_file)
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"⬇️ Descargar {selected_file}",
                    data=f.read(),
                    file_name=selected_file,
                    mime="application/octet-stream"
                )
    else:
        st.warning("⚠️ No hay archivos disponibles para descargar")

# TAB 3: VER ARCHIVOS
with tab3:
    st.subheader("Archivos almacenados")
    
    files_in_dir = os.listdir(UPLOAD_DIR) if os.path.exists(UPLOAD_DIR) else []
    
    if files_in_dir:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total de archivos", len(files_in_dir))
        
        with col2:
            total_size = sum(
                os.path.getsize(os.path.join(UPLOAD_DIR, f))
                for f in files_in_dir
            )
            st.metric("Tamaño total", f"{total_size / 1024:.2f} KB")
        
        with col3:
            if st.button("🗑️ Limpiar todos"):
                for f in files_in_dir:
                    os.remove(os.path.join(UPLOAD_DIR, f))
                st.success("✅ Archivos eliminados")
                st.rerun()
        
        st.markdown("#### Lista de archivos:")
        for file in files_in_dir:
            file_path = os.path.join(UPLOAD_DIR, file)
            size = os.path.getsize(file_path) / 1024
            st.text(f"📄 {file} ({size:.2f} KB)")
    else:
        st.info("ℹ️ No hay archivos almacenados")

st.markdown("---")




