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

def show_ud_1_4():
    st.subheader(":blue[UNIDAD DIDACTICA 1.4 -- ]" ":blue[ *Instalación y configuración de los nodos de la red de área local*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. El armario de comunicaciones."):
        _render_editable_block("1. Rack.", "MF0220_UF1_UD4_T1", "Estructura (Rack) donde se centraliza el cableado (Patch Panel) y electrónica (Switch/Router).", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 2
    with st.expander("2. Instalación de adaptadores de red y controladores."):
        _render_editable_block("2. Adaptadores.", "MF0220_UF1_UD4_T2", "Inserción física de la NIC e instalación del driver adecuado en el S.O.", 'default')

    # 3
    with st.expander("3. Instalación y configuración de protocolos de red más habituales."):
        _render_editable_block("3. Configuración TCP/IP.", "MF0220_UF1_UD4_T3", "Configurar IP, Máscara de subred, Puerta de enlace y DNS.", 'info')

    # 4
    with st.expander("4. Instalación y configuración de servicios de red."):
        _render_editable_block("4. Servicios.", "MF0220_UF1_UD4_T4", "Configuración básica de clientes para servicios como DHCP (IP automática) y DNS.", 'default')

    # 5
    with st.expander("5. Procedimiento de aplicación de configuraciones a routers y switches."):
        _render_editable_block("5. Configuración electrónica.", "MF0220_UF1_UD4_T5", "Acceso por consola o web para configurar VLANs, puertos y seguridad.", 'warning')

    st.divider()

if __name__ == '__main__':
    show_ud_1_4()