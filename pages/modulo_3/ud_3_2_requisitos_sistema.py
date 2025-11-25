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

def show_ud_3_2():
    st.subheader(":blue[UNIDAD DIDACTICA 2 -- ]" ":blue[ *Requisitos del sistema exigidos por las aplicaciones*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Fuentes de obtención."):
        _render_editable_block("1. Fuentes.", "MF0221_UD2_T1", "Consulta de la caja del producto, manuales oficiales, web del desarrollador y archivos 'ReadMe'.", 'default')

    # 2
    with st.expander("2. Requisitos de componentes hardware."):
        _render_editable_block("2. Requisitos HW.", "MF0221_UD2_T2", "Especificaciones mínimas y recomendadas: Tipo de CPU, cantidad de RAM, espacio en disco y tarjeta gráfica.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 3
    with st.expander("3. Requisitos de sistema operativo."):
        _render_editable_block("3. Requisitos SO.", "MF0221_UD2_T3", "Compatibilidad con la versión del SO (ej. Win 10/11), arquitectura (32/64 bits) y frameworks necesarios (.NET, Java).", 'info')

    # 4
    with st.expander("4. Otros requisitos."):
        _render_editable_block("4. Otros requisitos.", "MF0221_UD2_T4", "Conexión a Internet, periféricos específicos, cuentas de usuario con privilegios de administrador.", 'default')

    st.divider()

if __name__ == '__main__':
    show_ud_3_2()