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

def show_ud_4_1_3():
    st.subheader(":blue[UNIDAD DIDACTICA 3 -- ]" ":blue[ *Instalación de programas de cifrado de correos*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Descarga e instalación."):
        _render_editable_block("1. Instalación.", "MF0222_UF1_UD3_T1", "Herramientas como GPG (GnuPG) o complementos S/MIME. Proceso de setup en el cliente de correo.", 'default')

    # 2
    with st.expander("2. Generación de claves pública y privada."):
        _render_editable_block("2. Claves.", "MF0222_UF1_UD3_T2", "Concepto de Cifrado Asimétrico. Generación del par de claves. Importancia de proteger la clave privada.", 'info')

    # 3
    with st.expander("3. La gestión de claves."):
        _render_editable_block("3. Gestión.", "MF0222_UF1_UD3_T3", "Almacenamiento seguro (Keyrings), backup de claves y revocación.", 'warning')

    # 4
    with st.expander("4. Configuración."):
        _render_editable_block("4. Configuración.", "MF0222_UF1_UD3_T4", "Asociar las claves a la cuenta de correo en el cliente (ej. Outlook o Thunderbird con Enigmail).", 'default')

    # 5
    with st.expander("5. Distribución y obtención de claves."):
        _render_editable_block("5. Distribución.", "MF0222_UF1_UD3_T5", "Servidores de claves (Keyservers), intercambio manual de claves públicas.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 6
    with st.expander("6. Envío de correos cifrados/firmados."):
        _render_editable_block("6. Envío.", "MF0222_UF1_UD3_T6", "Diferencia entre Firmar (Autenticidad/Integridad) y Cifrar (Confidencialidad). Proceso de uso.", 'success')

    st.divider()

if __name__ == '__main__':
    show_ud_4_1_3()