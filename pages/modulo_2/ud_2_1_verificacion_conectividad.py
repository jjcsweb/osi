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

def show_ud_2_1():
    st.subheader(":blue[UNIDAD DIDACTICA 2.1 -- ]" ":blue[ *Verificación y prueba de elementos de conectividad*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Herramientas de verificación y prueba."):
        _render_editable_block("1. Herramientas.", "MF0220_UF2_UD1_T1", "Comandos (ping, ipconfig, tracert) y testers físicos básicos.", 'info')

    # 2
    with st.expander("2. Procedimientos sistemáticos de verificación y prueba de elementos de conectividad de redes locales."):
        _render_editable_block("2. Procedimientos.", "MF0220_UF2_UD1_T2", "Verificación capa por capa: Física (cable), Enlace (link), Red (IP).", 'default')

    st.divider()

if __name__ == '__main__':
    show_ud_2_1()