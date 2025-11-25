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

def show_ud_2_4():
    st.subheader(":blue[UNIDAD DIDACTICA 2.4 -- ]" ":blue[ *Comprobación de cables de par trenzado y coaxial*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Categorías de herramientas de comprobación de cableado."):
        _render_editable_block("1. Categorías herramientas.", "MF0220_UF2_UD4_T1", "Verificación (continuidad), Calificación (ancho de banda) y Certificación (cumplimiento norma).", 'info')

    # 2
    with st.expander("2. Analizadores o comprobadores de cable."):
        _render_editable_block("2. Analizadores.", "MF0220_UF2_UD4_T2", "Pruebas de mapa de cableado, longitud, atenuación, NEXT (diafonía) y ruido.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    st.divider()

if __name__ == '__main__':
    show_ud_2_4()