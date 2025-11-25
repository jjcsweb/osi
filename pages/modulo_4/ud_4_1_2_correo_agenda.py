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

def show_ud_4_1_2():
    st.subheader(":blue[UNIDAD DIDACTICA 2 -- ]" ":blue[ *Gestión del correo electrónico y de la agenda*]")
    RUTA_IMAGEN_GENERICA = "fuentes/imagenes/logo.jpg"

    # 1
    with st.expander("1. Definiciones y términos."):
        _render_editable_block("1. Términos.", "MF0222_UF1_UD2_T1", "SMTP, POP3, IMAP, Spam, Phishing, Adjuntos.", 'default')

    # 2
    with st.expander("2. Funcionamiento."):
        _render_editable_block("2. Funcionamiento.", "MF0222_UF1_UD2_T2", "Ciclo de envío y recepción: Cliente -> Servidor Saliente -> Internet -> Servidor Entrante -> Cliente.", 'info')

    # 3
    with st.expander("3. El formato de un correo electrónico."):
        _render_editable_block("3. Formato.", "MF0222_UF1_UD2_T3", "Cabeceras (To, Cc, Bcc, Subject) y Cuerpo (Texto plano vs HTML).", 'default')

    # 4
    with st.expander("4. Configuración de cuentas de correo."):
        _render_editable_block("4. Configuración.", "MF0222_UF1_UD2_T4", "Parámetros necesarios: Servidores entrante/saliente, puertos, seguridad (SSL/TLS) y credenciales.", 'warning')

    # 5
    with st.expander("5. Gestores de correo electrónico."):
        _render_editable_block("5. Gestores.", "MF0222_UF1_UD2_T5", "Software cliente local: Microsoft Outlook, Mozilla Thunderbird, Apple Mail.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    # 6
    with st.expander("6. Correo Web."):
        _render_editable_block("6. Webmail.", "MF0222_UF1_UD2_T6", "Acceso al correo vía navegador (Gmail, Outlook.com). Ventajas y desventajas frente a clientes locales.", 'default')

    # 7
    with st.expander("7. Plantillas y firmas corporativas."):
        _render_editable_block("7. Plantillas.", "MF0222_UF1_UD2_T7", "Estandarización de la imagen corporativa en las comunicaciones. Creación de firmas automáticas.", 'default')

    # 8
    with st.expander("8. Gestión de la libreta de direcciones."):
        _render_editable_block("8. Contactos.", "MF0222_UF1_UD2_T8", "Creación de contactos, grupos de distribución y libretas de direcciones globales (LDAP).", 'default')

    # 9
    with st.expander("9. Gestión de correo."):
        _render_editable_block("9. Gestión.", "MF0222_UF1_UD2_T9", "Organización mediante carpetas, reglas de filtrado, etiquetas y búsquedas.", 'success')

    # 10
    with st.expander("10. Componentes fundamentales de una aplicación de gestión de correos y agendas electrónicas."):
        _render_editable_block("10. Componentes.", "MF0222_UF1_UD2_T10", "Integración de Correo, Calendario, Tareas, Notas y Contactos en una sola interfaz.", 'default')

    # 11
    with st.expander("11. Foros de noticias “news”."):
        _render_editable_block("11. News.", "MF0222_UF1_UD2_T11", "Protocolo NNTP y grupos de noticias (Usenet). Relevancia actual y alternativas.", 'info')

    # 12
    with st.expander("12. Programas de agendas en sincronización con dispositivos portátiles."):
        _render_editable_block("12. Sincronización.", "MF0222_UF1_UD2_T12", "Sincronización ActiveSync/Exchange con smartphones y tablets.", 'default')

    # 13
    with st.expander("13. Gestión de la agenda."):
        _render_editable_block("13. Agenda.", "MF0222_UF1_UD2_T13", "Creación de citas, reuniones, invitaciones, recordatorios y calendarios compartidos.", 'columna_img', image_url_fija=RUTA_IMAGEN_GENERICA)

    st.divider()

if __name__ == '__main__':
    show_ud_4_1_2()