import streamlit as st
from funciones.ui_manager import show_editable_content


# --- Función Auxiliar para la Maquetación del Bloque Editable ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None,
                           image_url_fija=""):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""

    # 1. Título opcional
    if sub_heading:
        st.markdown(f"##### {sub_heading}")

    # 2. Botón de edición
    edit_key = f'edit_{id_base}'
    is_editing = st.session_state.get(edit_key, False)

    col_btn, col_spacer = st.columns([1, 10])

    with col_btn:
        # Width="content" para ajustar al texto y evitar error de Streamlit
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary",
                     width="content"):
            st.session_state[edit_key] = not is_editing
            st.rerun()

    # 3. Renderizado del contenido
    show_editable_content(
        id_tema=id_base,
        titulo=topic_title,
        default_text=default_text,
        default_widget=default_widget,
        default_image_url_fija=image_url_fija
    )


# -------------------------------------------------------------

def show_ud_1_5():
    """Muestra el contenido de la UD 1.5: Instalación y configuración."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.5 -- ]" ":blue[ *Instalación y configuración de Sistemas Operativos*]")

    # Uso de ruta existente
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # =================================================================
    # 1. Requisitos para la instalación.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD5_T1"
    with st.expander("1. Requisitos para la instalación. Compatibilidad hardware y software."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Requisitos de instalación.",
            default_text="Antes de instalar, es crucial verificar los requisitos mínimos de CPU, RAM y disco. Se debe consultar la HCL (Hardware Compatibility List) para asegurar la compatibilidad.",
            default_widget='info'
        )

    # =================================================================
    # 2. Fases de instalación.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD5_T2"
    with st.expander("2. Fases de instalación."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Fases de instalación.",
            default_text="El proceso típico incluye: 1. Planificación. 2. Particionamiento y formateo del disco. 3. Copia de archivos del sistema. 4. Configuración inicial (usuario, red, zona horaria).",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # =================================================================
    # 3. Tipos de instalación.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF1_UD5_T3"
    with st.expander("3. Tipos de instalación."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Tipos de instalación.",
            default_text="Existen varios métodos: Instalación limpia (formateando), Actualización (conservando datos), Instalación desatendida (automatizada) y Arranque dual (multiboot).",
            default_widget='default'
        )

    # =================================================================
    # 4. Verificación de la instalación.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF1_UD5_T4"
    with st.expander("4. Verificación de la instalación. Pruebas de arranque y parada."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Verificación y pruebas.",
            default_text="Tras instalar, se debe verificar que el sistema arranca correctamente, que todos los drivers están cargados y que el proceso de apagado/reinicio se completa sin errores.",
            default_widget='success'
        )

    # =================================================================
    # 5. Documentación de la instalación y configuración.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF1_UD5_T5"
    with st.expander("5. Documentación de la instalación y configuración."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Documentación.",
            default_text="Es fundamental registrar la configuración aplicada: nombre del equipo (hostname), dirección IP, cuentas de usuario creadas, licencias aplicadas y software adicional instalado.",
            default_widget='default'
        )

    st.divider()


if __name__ == '__main__':
    show_ud_1_5()