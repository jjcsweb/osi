import streamlit as st
from funciones.ui_manager import show_editable_content

def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None, image_url_fija=""):
    if sub_heading: st.markdown(f"##### {sub_heading}")
    edit_key = f'edit_{id_base}'; is_editing = st.session_state.get(edit_key, False)
    col_btn, _ = st.columns([1, 10])
    with col_btn:
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary", width="content"):
            st.session_state[edit_key] = not is_editing; st.rerun()
    show_editable_content(id_tema=id_base, titulo=topic_title, default_text=default_text, default_widget=default_widget, default_image_url_fija=image_url_fija)

def show_ud_3_4():
    st.subheader(":blue[UNIDAD DIDACTICA 4 -- ]" ":blue[ *Instalación de aplicaciones informáticas*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Componentes de una aplicación."):
        _render_editable_block("1. Componentes.", "MF0221_UD4_T1", "Ejecutables (.exe), librerías (.dll), archivos de configuración (.ini, .xml), y datos.", 'default')

    # 2
    with st.expander("2. Procedimientos de copia de seguridad."):
        _render_editable_block("2. Backup previo.", "MF0221_UD4_T2", "Importancia de realizar copias de seguridad o puntos de restauración antes de instalar software crítico.", 'warning')

    # 3
    with st.expander("3. Instalación y registro de aplicaciones."):
        _render_editable_block("3. Instalación.", "MF0221_UD4_T3", "Asistentes de instalación, rutas de destino, tipos de instalación (típica/personalizada) y activación de licencias.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 4
    with st.expander("4. Configuración de aplicaciones ofimáticas más comunes."):
        _render_editable_block("4. Configuración.", "MF0221_UD4_T4", "Ajustes post-instalación en suites como Office o LibreOffice: usuario, rutas de guardado, diccionarios.", 'default')

    # 5
    with st.expander("5. Procedimientos de prueba y verificación."):
        _render_editable_block("5. Verificación.", "MF0221_UD4_T5", "Ejecución de prueba (Smoke Test), verificación de funcionalidades básicas y comprobación de actualizaciones.", 'success')

    st.divider()

if __name__ == '__main__':
    show_ud_3_4()