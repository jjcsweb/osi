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

def show_ud_4_1_4():
    st.subheader(":blue[UNIDAD DIDACTICA 4 -- ]" ":blue[ *Obtención de certificados de firma electrónica*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Conceptos sobre seguridad en las comunicaciones."):
        _render_editable_block("1. Conceptos.", "MF0222_UF1_UD4_T1", "Confidencialidad, Integridad, Autenticación y No Repudio.", 'default')

    # 2
    with st.expander("2. Certificados electrónicos."):
        _render_editable_block("2. Certificados.", "MF0222_UF1_UD4_T2", "Documento digital que vincula una identidad a una clave pública. Estándar X.509.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 3
    with st.expander("3. Firma electrónica."):
        _render_editable_block("3. Firma.", "MF0222_UF1_UD4_T3", "Conjunto de datos electrónicos que acompañan a una información para identificar al firmante.", 'info')

    # 4
    with st.expander("4. Prestador de servicios de certificación."):
        _render_editable_block("4. PSC / CA.", "MF0222_UF1_UD4_T4", "Autoridad de Certificación (CA). Entidad de confianza que emite y revoca certificados (ej. FNMT).", 'default')

    # 5
    with st.expander("5. Obtención de un certificado por una persona física."):
        _render_editable_block("5. Obtención.", "MF0222_UF1_UD4_T5", "Proceso: Solicitud vía navegador, Acreditación de identidad presencial y Descarga/Instalación.", 'warning')

    # 6
    with st.expander("6. El certificado y el correo electrónico."):
        _render_editable_block("6. Uso en correo.", "MF0222_UF1_UD4_T6", "Configuración del certificado en el cliente de correo para firmar digitalmente los mensajes salientes.", 'success')

    st.divider()

if __name__ == '__main__':
    show_ud_4_1_4()