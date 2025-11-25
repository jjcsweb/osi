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

def show_ud_4_1_1():
    st.subheader(":blue[UNIDAD DIDACTICA 1 -- ]" ":blue[ *Técnicas de comunicación en la asistencia al usuario*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Tipos de comunicación."):
        _render_editable_block("1. Tipos comunicación.", "MF0222_UF1_UD1_T1", "Comunicación verbal (oral/escrita) y no verbal (gestos, postura). Síncrona vs Asíncrona.", 'default')

    # 2
    with st.expander("2. Efectos de la comunicación."):
        _render_editable_block("2. Efectos.", "MF0222_UF1_UD1_T2", "Impacto en la resolución de problemas, satisfacción del usuario e imagen corporativa.", 'info')

    # 3
    with st.expander("3. Obstáculos o barreras para la comunicación."):
        _render_editable_block("3. Barreras.", "MF0222_UF1_UD1_T3", "Físicas (ruido), Semánticas (tecnicismos), Psicológicas (actitud) y Administrativas.", 'warning')

    # 4
    with st.expander("4. La comunicación en la empresa."):
        _render_editable_block("4. Empresa.", "MF0222_UF1_UD1_T4", "Flujos de comunicación: Ascendente, Descendente y Horizontal. Canales formales e informales.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 5
    with st.expander("5. Formas de comunicación oral."):
        _render_editable_block("5. Comunicación oral.", "MF0222_UF1_UD1_T5", "Presencial, telefónica o videoconferencia. Importancia de la escucha activa y el tono de voz.", 'default')

    # 6
    with st.expander("6. Precisión y claridad en el lenguaje."):
        _render_editable_block("6. Claridad.", "MF0222_UF1_UD1_T6", "Uso de vocabulario adaptado al nivel del usuario, evitando jerga técnica innecesaria. Concisión.", 'success')

    # 7
    with st.expander("7. Asistencia al usuario."):
        _render_editable_block("7. Asistencia.", "MF0222_UF1_UD1_T7", "Protocolos de atención, empatía, paciencia y gestión de usuarios difíciles.", 'default')

    # 8
    with st.expander("8. Tipos de licencia de software."):
        _render_editable_block("8. Licencias.", "MF0222_UF1_UD1_T8", "Conceptos básicos sobre licenciamiento (EULA, Freeware, Propietario) relevantes al dar soporte.", 'default')

    st.divider()

if __name__ == '__main__':
    show_ud_4_1_1()