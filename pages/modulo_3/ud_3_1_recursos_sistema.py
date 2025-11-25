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

def show_ud_3_1():
    st.subheader(":blue[UNIDAD DIDACTICA 1 -- ]" ":blue[ *Recursos y componentes de un sistema informático*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Herramientas del sistema operativo para la obtención de información."):
        _render_editable_block("1. Herramientas info.", "MF0221_UD1_T1", "Uso de 'Información del sistema' (msinfo32), dxdiag y comandos como 'systeminfo' para auditar el equipo.", 'default')

    # 2
    with st.expander("2. Recursos Hardware."):
        _render_editable_block("2. Recursos HW.", "MF0221_UD1_T2", "Gestión de Conflictos, Recursos compartidos, DMA (Acceso directo a memoria), Canales IRQ (Interrupciones), Direcciones de E/S y Memoria.", 'info')

    # 3
    with st.expander("3. El administrador de dispositivos."):
        _render_editable_block("3. Admin dispositivos.", "MF0221_UD1_T3", "Herramienta gráfica para ver el estado del hardware, identificar componentes con errores (signo de exclamación) y actualizar drivers.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    st.divider()

if __name__ == '__main__':
    show_ud_3_1()