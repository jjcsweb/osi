import streamlit as st
from funciones.ui_manager import show_editable_content


# --- Función Auxiliar Estandarizada ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    if sub_heading:
        st.markdown(f"##### {sub_heading}")

    edit_key = f'edit_{id_base}'
    is_editing = st.session_state.get(edit_key, False)
    col_btn, col_spacer = st.columns([1, 10])

    with col_btn:
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary",
                     width="content"):
            st.session_state[edit_key] = not is_editing
            st.rerun()

    show_editable_content(
        id_tema=id_base,
        titulo=topic_title,
        default_text=default_text,
        default_widget=default_widget,
        default_image_url_fija=image_url_fija
    )


# -------------------------------------------------------------

def show_ud_1_1():
    """Muestra el contenido de la UD 1.1: Arquitectura de redes de área local."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.1 -- ]" ":blue[ *Arquitectura de redes de área local*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1. Clasificación de las redes
    TEMA_ID_T1 = "MF0220_UF1_UD1_T1"
    with st.expander("1. Clasificación de las redes en función del territorio que abarcan."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Clasificación de redes.",
            default_text="Se clasifican por su alcance: LAN (Local), MAN (Metropolitana), WAN (Amplia) y PAN (Personal).",
            default_widget='info'
        )

    # 2. Características de una red local
    TEMA_ID_T2 = "MF0220_UF1_UD1_T2"
    with st.expander("2. Características de una red local."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Características LAN.",
            default_text="Velocidad de transmisión elevada, tasa de error baja, alcance limitado (edificio/campus) y propiedad privada.",
            default_widget='default'
        )

    # 3. Arquitectura de redes de área local
    TEMA_ID_T3 = "MF0220_UF1_UD1_T3"
    with st.expander("3. Arquitectura de redes de área local."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Arquitectura.",
            default_text="Define la topología física (Bus, Estrella, Anillo) y lógica (Token Ring, Ethernet). Modelos Cliente-Servidor vs. Peer-to-Peer.",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # 4. Normativa
    TEMA_ID_T4 = "MF0220_UF1_UD1_T4"
    with st.expander("4. Normativa."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Normativa IEEE.",
            default_text="Estándares del IEEE 802 (ej. 802.3 Ethernet, 802.11 Wi-Fi) que aseguran la interoperabilidad.",
            default_widget='success'
        )

    st.divider()


if __name__ == '__main__':
    show_ud_1_1()