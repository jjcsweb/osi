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

def show_ud_1_2():
    st.subheader(":blue[UNIDAD DIDACTICA 1.2 -- ]" ":blue[ *Elementos de una red de área local*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Características y funciones."):
        _render_editable_block("1. Características.", "MF0220_UF1_UD2_T1", "Roles básicos: Emisor, Receptor, Mensaje, Medio y Protocolo.", 'default')

    # 2
    with st.expander("2. Estaciones de trabajo."):
        _render_editable_block("2. Estaciones de trabajo.", "MF0220_UF1_UD2_T2", "Equipos cliente (PC, Laptop) que inician solicitudes de servicio en la red.", 'info')

    # 3
    with st.expander("3. Servidores."):
        _render_editable_block("3. Servidores.", "MF0220_UF1_UD2_T3", "Equipos potentes que proveen recursos (archivos, impresión, BD) a los clientes.", 'default')

    # 4
    with st.expander("4. Tarjetas de red."):
        _render_editable_block("4. Tarjetas de red (NIC).", "MF0220_UF1_UD2_T4", "Hardware que conecta el equipo al medio físico. Tiene una dirección MAC única.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 5
    with st.expander("5. Equipos de conectividad."):
        _render_editable_block("5. Equipos conectividad.", "MF0220_UF1_UD2_T5", "Hub (repetidor), Switch (conmutador capa 2) y Router (enrutador capa 3).", 'default')

    # 6
    with st.expander("6. Sistemas operativos de red."):
        _render_editable_block("6. SOR.", "MF0220_UF1_UD2_T6", "Software base para gestionar usuarios y recursos de red (Windows Server, Linux Server).", 'default')

    # 7
    with st.expander("7. Medios de transmisión."):
        _render_editable_block("7. Medios.", "MF0220_UF1_UD2_T7", "Guiados (Par trenzado UTP/STP, Coaxial, Fibra óptica) y No guiados (Wi-Fi, Bluetooth).", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 8
    with st.expander("8. El cableado estructurado."):
        _render_editable_block("8. Cableado estructurado.", "MF0220_UF1_UD2_T8", "Sistema estandarizado de cableado (subsistemas horizontal, vertical/backbone).", 'success')

    # 9
    with st.expander("9. El mapa físico y lógico de una red de área local."):
        _render_editable_block("9. Mapas de red.", "MF0220_UF1_UD2_T9", "Documentación visual. Físico: ubicación de cables/equipos. Lógico: direccionamiento IP/VLANs.", 'warning')

    st.divider()

if __name__ == '__main__':
    show_ud_1_2()