import streamlit as st
from funciones.ui_manager import show_editable_content

# --- Función Auxiliar para la Maquetación del Bloque Editable ---
def _render_editable_block(topic_title, id_base, default_text, default_widget='default', sub_heading=None):
    """Encapsula la lógica del botón, columnas y la llamada a show_editable_content."""
    with st.container():
        if sub_heading:
            st.markdown(f"##### {sub_heading}")
        edit_key = f'edit_{id_base}'
        is_editing = st.session_state.get(edit_key, False)
        col_btn, col_spacer = st.columns([1, 10])
        with col_btn:
            if st.button("✏️ Editar" if not is_editing else "👁️ Ver", key=f'btn_toggle_{id_base}'):
                st.session_state[edit_key] = not is_editing
                st.rerun()
        show_editable_content(
            id_tema=id_base,
            titulo=topic_title,
            default_text=default_text,
            default_widget=default_widget
        )
# -------------------------------------------------------------

def show_ud_2_3():
    """Muestra el contenido de la UD 2.3: Configuración de las opciones de accesibilidad."""

    st.subheader(":blue[UNIDAD DIDACTICA 2.3 -- ]" ":blue[ *Configuración de las opciones de accesibilidad*]")



    # =================================================================
    # 1. Opciones para facilitar la visualización de pantalla.
    # =================================================================
    TEMA_ID_T1 = "MF0219_UF2_UD3_T1"
    with st.expander("1. Opciones para facilitar la visualización de pantalla."):
        _render_editable_block(
            id_base=TEMA_ID_T1,
            topic_title="1. Visualización.",
            default_text="""
            Ajustes como **alto contraste**, **magnificador** de pantalla, cambio de **tamaño de texto** y configuración de **filtros de color**.
            **Ejemplo:** *Activar el Magnifier (Lupa) de Windows para aumentar una parte específica de la pantalla.*
            """,
            default_widget='info'
        )

    # =================================================================
    # 2. Uso de narradores.
    # =================================================================
    TEMA_ID_T2 = "MF0219_UF2_UD3_T2"
    with st.expander("2. Uso de narradores."):
        _render_editable_block(
            id_base=TEMA_ID_T2,
            topic_title="2. Narradores.",
            default_text="""
            Software que lee en voz alta el contenido de la pantalla para usuarios con discapacidad visual o con dificultades de lectura.
            **Ejemplo:** *Windows Narrator o VoiceOver en macOS.*
            """
        )

    # =================================================================
    # 3. Opciones para hacer más fácil el uso del teclado o del ratón.
    # =================================================================
    TEMA_ID_T3 = "MF0219_UF2_UD3_T3"
    with st.expander("3. Opciones para hacer más fácil el uso del teclado o del ratón."):
        _render_editable_block(
            id_base=TEMA_ID_T3,
            topic_title="3. Teclado y Ratón.",
            default_text="""
            Funciones como **Teclas Adhesivas** (para combinaciones de teclas), **Teclas Filtro** (para ignorar pulsaciones rápidas) y **Teclas de Mouse** (controlar el puntero con el teclado).
            **Ejemplo:** *Usar Teclas Adhesivas para pulsar Ctrl+Alt+Supr sin tener que presionar las tres teclas simultáneamente.*
            """
        )

    # =================================================================
    # 4. Reconocimiento de voz.
    # =================================================================
    TEMA_ID_T4 = "MF0219_UF2_UD3_T4"
    with st.expander("4. Reconocimiento de voz."):
        _render_editable_block(
            id_base=TEMA_ID_T4,
            topic_title="4. Reconocimiento de voz.",
            default_text="""
            Permite controlar el SO y dictar texto mediante comandos de voz, útil para usuarios con movilidad reducida.
            **Ejemplo:** *Dictar un correo electrónico completo en un procesador de texto o abrir un programa con un comando de voz.*
            """,
            default_widget='success'
        )

    # =================================================================
    # 5. Uso de alternativas visuales y de texto para personas con dificultades auditivas.
    # =================================================================
    TEMA_ID_T5 = "MF0219_UF2_UD3_T5"
    with st.expander("5. Uso de alternativas visuales y de texto (subtítulos, notificaciones visuales)."):
        _render_editable_block(
            id_base=TEMA_ID_T5,
            topic_title="5. Alternativas visuales.",
            default_text="""
            Configuración de **subtítulos**, **notificaciones visuales** de sonido y **textos alternativos** para personas con discapacidad auditiva.
            **Ejemplo:** *Hacer que la pantalla parpadee en lugar de emitir un sonido de notificación.*
            """,
            default_widget='default'
        )
    st.divider()

if __name__ == '__main__':
    show_ud_2_3()