import streamlit as st
from funciones.ui_manager import show_editable_content


# --- Función Auxiliar para la Maquetación del Bloque Editable ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""

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

def show_ud_1_7():
    """Muestra el contenido de la UD 1.7: Actualización del Sistema Operativo Informático."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.7 -- ]" ":blue[ *Actualización del Sistema Operativo Informático*]")

    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # =================================================================
    # 1. Clasificación de las fuentes de actualización.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD7_T1"
    with st.expander("1. Clasificación de las fuentes de actualización."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Fuentes de actualización.",
            default_text="Las actualizaciones pueden provenir de: Repositorios oficiales del fabricante (Windows Update, repos de Linux), Servidores locales (WSUS), Medios físicos o Descargas manuales.",
            default_widget='default'
        )

    # =================================================================
    # 2. Actualización automática.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD7_T2"
    with st.expander("2. Actualización automática."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Actualización automática.",
            default_text="Configuración del sistema para detectar, descargar e instalar actualizaciones críticas y de seguridad sin intervención constante del usuario.",
            default_widget='info'
        )

    # =================================================================
    # 3. Los centros de soporte y ayuda.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF1_UD7_T3"
    with st.expander("3. Los centros de soporte y ayuda."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Centros de soporte.",
            default_text="Recursos para solucionar problemas: Bases de Conocimiento (KB), Foros técnicos, Documentación oficial (TechNet, Man pages) y Soporte telefónico/remoto.",
            default_widget='default'
        )

    # =================================================================
    # 4. Procedimientos de actualización.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF1_UD7_T4"
    with st.expander("4. Procedimientos de actualización."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Procedimientos de actualización.",
            default_text="Pasos seguros: 1. Realizar copia de seguridad. 2. Verificar espacio en disco. 3. Ejecutar actualización. 4. Reiniciar. 5. Verificar funcionamiento.",
            default_widget='warning'
        )

    # =================================================================
    # 5. Actualización de sistemas operativos.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF1_UD7_T5"
    with st.expander("5. Actualización de sistemas operativos."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Actualización del SO.",
            default_text="Incluye Service Packs (paquetes acumulativos), actualizaciones de características (versiones nuevas) y parches de seguridad (hotfixes).",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # =================================================================
    # 6. Actualización de componentes software.
    # =================================================================
    TEMA_ID_T6 = "MF0219_UF1_UD7_T6"
    with st.expander("6. Actualización de componentes software."):
        _render_editable_block(
            id_base=TEMA_ID_T6,
            topic_title="6. Componentes software.",
            default_text="No solo se actualiza el núcleo, también los controladores (drivers), librerías (.NET, Java) y aplicaciones integradas.",
            default_widget='default'
        )

    # =================================================================
    # 7. Verificación de la actualización.
    # =================================================================
    TEMA_ID_T7 = "MF0219_UF1_UD7_T7"
    with st.expander("7. Verificación de la actualización."):
        _render_editable_block(
            id_base=TEMA_ID_T7,
            topic_title="7. Verificación.",
            default_text="Comprobar el historial de actualizaciones para confirmar instalación exitosa (""Successfully installed"") y revisar logs de eventos en caso de error.",
            default_widget='success'
        )

    # =================================================================
    # 8. Documentación de la actualización.
    # =================================================================
    TEMA_ID_T8 = "MF0219_UF1_UD7_T8"
    with st.expander("8. Documentación de la actualización."):
        _render_editable_block(
            id_base=TEMA_ID_T8,
            topic_title="8. Documentación.",
            default_text="Registro de cambios: qué parches se aplicaron, fecha, motivo, incidencias resueltas y cualquier problema derivado.",
            default_widget='default'
        )

    st.divider()


if __name__ == '__main__':
    show_ud_1_7()