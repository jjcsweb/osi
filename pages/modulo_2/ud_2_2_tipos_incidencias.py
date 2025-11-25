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

def show_ud_2_2():
    st.subheader(":blue[UNIDAD DIDACTICA 2.2 -- ]" ":blue[ *Tipos de incidencias que se pueden producir en una red*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Incidencias a nivel de conectividad del enlace."):
        _render_editable_block("1. Incidencias enlace.", "MF0220_UF2_UD2_T1", "Cables rotos, conectores mal crimpados, atenuación excesiva, ruido.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 2
    with st.expander("2. Incidencias a nivel de red."):
        _render_editable_block("2. Incidencias red.", "MF0220_UF2_UD2_T2", "IPs duplicadas, máscara incorrecta, puerta de enlace inalcanzable, DNS fallido.", 'warning')

    st.divider()

if __name__ == '__main__':
    show_ud_2_2()