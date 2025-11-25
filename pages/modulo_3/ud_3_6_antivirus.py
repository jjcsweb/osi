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

def show_ud_3_6():
    st.subheader(":blue[UNIDAD DIDACTICA 6 -- ]" ":blue[ *Instalación y configuración del software antivirus*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Virus informáticos."):
        _render_editable_block("1. Virus.", "MF0221_UD6_T1", "Definición de malware, tipos (Troyanos, Gusanos, Ransomware) y vías de infección.", 'default')

    # 2
    with st.expander("2. Definición de software antivirus."):
        _render_editable_block("2. Antivirus.", "MF0221_UD6_T2", "Programa diseñado para prevenir, detectar y eliminar software malicioso.", 'info')

    # 3
    with st.expander("3. Componentes activos de los antivirus."):
        _render_editable_block("3. Componentes.", "MF0221_UD6_T3", "Monitor residente (tiempo real), Motor de escaneo, Base de datos de firmas, Cuarentena.", 'default')

    # 4
    with st.expander("4. Características generales de los paquetes de software antivirus."):
        _render_editable_block("4. Características.", "MF0221_UD6_T4", "Detección heurística, protección web, firewall integrado, bajo consumo de recursos.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 5
    with st.expander("5. Instalación de software antivirus."):
        _render_editable_block("5. Instalación.", "MF0221_UD6_T5", "Importancia de desinstalar antivirus previos (conflicto), proceso de instalación y actualización inicial de firmas.", 'warning')

    # 6
    with st.expander("6. La ventana principal."):
        _render_editable_block("6. Interfaz.", "MF0221_UD6_T6", "Gestión del estado de protección, acceso a escaneos rápidos/completos y configuración de alertas.", 'success')

    st.divider()

if __name__ == '__main__':
    show_ud_3_6()