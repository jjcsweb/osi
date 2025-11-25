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
        # Width="content" para evitar error de Streamlit
        if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}', type="secondary", width="content"):
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

def show_ud_1_4():
    """Muestra el contenido de la UD 1.4: Sistemas Operativos Informáticos Actuales."""

    st.subheader(":blue[UNIDAD DIDACTICA 1.4 -- ]" ":blue[ *Sistemas Operativos Informáticos Actuales*]")

    # Ruta de imagen genérica existente
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # =================================================================
    # 1. Clasificación de los sistemas operativos.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF1_UD4_T1"
    with st.expander("1. Clasificación de los sistemas operativos."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Clasificación de los S.O.",
            default_text="""
            Los sistemas operativos se pueden clasificar según:
            * **Usuarios:** Monousuario vs. Multiusuario.
            * **Tareas:** Monotarea vs. Multitarea.
            * **Procesadores:** Monoprocesador vs. Multiprocesador.
            """,
            default_widget='info'
        )

    # =================================================================
    # 2. Software libre.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF1_UD4_T2"
    with st.expander("2. Software libre."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Software libre.",
            default_text="Software que respeta la libertad de los usuarios para ejecutar, copiar, distribuir, estudiar, cambiar y mejorar el software (Las 4 libertades).",
            default_widget='columna_img',
            image_url_fija=RUTA_IMAGEN_GENERICA
        )

    # =================================================================
    # 3. Características y utilización.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF1_UD4_T3"
    with st.expander("3. Características y utilización."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Características y utilización.",
            default_text="Uso generalizado de interfaces gráficas (GUI), soporte de red integrado y gestión avanzada de seguridad en entornos corporativos y domésticos.",
            default_widget='default'
        )

    # =================================================================
    # 4. Diferencias.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF1_UD4_T4"
    with st.expander("4. Diferencias."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Diferencias entre S.O.",
            default_text="Diferencias clave entre Windows (propietario, uso masivo), Linux (libre, servidores/desarrollo) y macOS (propietario, diseño/multimedia).",
            default_widget='warning'
        )

    # =================================================================
    # 5. Versiones y distribuciones.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF1_UD4_T5"
    with st.expander("5. Versiones y distribuciones."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Versiones y distribuciones.",
            default_text="**Versiones:** Actualizaciones mayores de un mismo software (ej. Windows 10, 11). **Distribuciones:** Variantes de Linux con diferentes paquetes y escritorios (ej. Ubuntu, Debian).",
            default_widget='success'
        )

    st.divider()

if __name__ == '__main__':
    show_ud_1_4()