import streamlit as st
from funciones.ui_manager import show_editable_content


def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    if sub_heading: st.markdown(f"##### {sub_heading}")
    edit_key = f'edit_{id_base}';
    is_editing = st.session_state.get(edit_key, False)
    col_btn, _ = st.columns([1, 10])
    with col_btn:
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary",
                     width="content"):
            st.session_state[edit_key] = not is_editing;
            st.rerun()
    show_editable_content(id_tema=id_base, titulo=topic_title, default_text=default_text, default_widget=default_widget,
                          default_image_url_fija=image_url_fija)


def show_ud_1_3():
    st.subheader(":blue[UNIDAD DIDACTICA 1.3 -- ]" ":blue[ *Protocolos de una red de área local*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Introducción a los protocolos."):
        _render_editable_block("1. Intro protocolos.", "MF0220_UF1_UD3_T1",
                               "Reglas y convenios que permiten la comunicación entre dispositivos heterogéneos.",
                               'default')

    # 2
    with st.expander("2. Modelo de Interconexión de Sistemas Abiertos (OSI)."):
        _render_editable_block("2. Modelo OSI.", "MF0220_UF1_UD3_T2",
                               "Modelo de 7 capas: Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación.",
                               'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 3
    with st.expander("3. El nivel físico."):
        _render_editable_block("3. Nivel físico.", "MF0220_UF1_UD3_T3",
                               "Transmisión de bits puros sobre el medio (voltajes, frecuencias, conectores).",
                               'default')

    # 4
    with st.expander("4. Protocolos del nivel de enlace."):
        _render_editable_block("4. Nivel enlace.", "MF0220_UF1_UD3_T4",
                               "Control de acceso al medio (MAC), direccionamiento físico y detección de errores.",
                               'default')

    # 5
    with st.expander("5. Ethernet."):
        _render_editable_block("5. Ethernet.", "MF0220_UF1_UD3_T5",
                               "Estándar IEEE 802.3. Usa CSMA/CD y tramas con direcciones MAC.", 'info')

    # 6
    with st.expander("6. Otros protocolos de nivel de enlace: Token Ring, FDDI, etc."):
        _render_editable_block("6. Otros protocolos.", "MF0220_UF1_UD3_T6",
                               "Tecnologías legacy como Token Ring (paso de testigo) o FDDI (anillo de fibra).",
                               'default')

    # 7
    with st.expander("7. Protocolos de nivel de red."):
        _render_editable_block("7. Nivel de red.", "MF0220_UF1_UD3_T7",
                               "Encaminamiento y direccionamiento lógico. El protocolo principal es IP (IPv4/IPv6).",
                               'success')

    # 8
    with st.expander("8. Direcciones físicas y lógicas."):
        _render_editable_block("8. Direccionamiento.", "MF0220_UF1_UD3_T8",
                               "Física: MAC (48 bits, hardware). Lógica: IP (32/128 bits, jerárquica).", 'warning')

    st.divider()


if __name__ == '__main__':
    show_ud_1_3()