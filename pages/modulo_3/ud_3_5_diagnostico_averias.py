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

def show_ud_3_5():
    st.subheader(":blue[UNIDAD DIDACTICA 5 -- ]" ":blue[ *Diagnóstico y resolución de averías software*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Metodología para la resolución de problemas."):
        _render_editable_block("1. Metodología.", "MF0221_UD5_T1", "Pasos lógicos: Recopilar datos, Identificar síntomas, Establecer hipótesis, Probar solución y Verificar.", 'default')

    # 2
    with st.expander("2. Programas de diagnóstico."):
        _render_editable_block("2. Herramientas diagnóstico.", "MF0221_UD5_T2", "Software para testear memoria, disco duro y estabilidad del sistema.", 'info')

    # 3
    with st.expander("3. Configuración de informes de errores del sistema y de las aplicaciones."):
        _render_editable_block("3. Informes errores.", "MF0221_UD5_T3", "Uso del Visor de Eventos (Event Viewer) para analizar logs de aplicación y sistema.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 4
    with st.expander("4. Identificación de los fallos."):
        _render_editable_block("4. Identificación.", "MF0221_UD5_T4", "Diferenciar entre fallo de aplicación (cuelgue), fallo de sistema (BSOD) o conflicto de recursos.", 'warning')

    # 5
    with st.expander("5. Procedimientos comunes de solución."):
        _render_editable_block("5. Soluciones.", "MF0221_UD5_T5", "Reinstalación, reparación de instalación, modo compatibilidad, actualización de parches.", 'success')

    st.divider()

if __name__ == '__main__':
    show_ud_3_5()