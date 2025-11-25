import streamlit as st
from .db_manager import load_content, save_content


# --- Funciones de Renderizado ---

# MODIFICACIÓN: Ahora acepta 'imagen_url_fija' para la imagen estática.
# Se ELIMINA element_key_prefix y el st.text_input anterior.
def render_content(texto_md: str, tipo_widget: str, imagen_url_fija: str = ""):
    """Renderiza el contenido usando el widget de Streamlit especificado."""

    if tipo_widget == 'success':
        st.success(texto_md)
    # ... (código para 'info', 'warning', 'error') ...
    elif tipo_widget == 'columna_img':
        # 3. Un marco especial que admita dos columnas (simulado)

        col1, col2 = st.columns([1, 2])
        with col1:
            # Usar la URL de imagen fija proporcionada por el desarrollador
            if imagen_url_fija:
                st.image(imagen_url_fija, caption="Imagen de Contenido")
            else:
                st.markdown("*(Imagen Estática Fija Pendiente)*")
        with col2:
            st.markdown(f"{texto_md}")
    else:
        # 'default' o cualquier otro valor
        st.markdown(texto_md)


# --- Función Principal (Editable y Persistente) ---

# MODIFICACIÓN: show_editable_content ahora acepta 'default_image_url_fija'
def show_editable_content(id_tema: str, titulo: str, default_text: str = "Añade tu contenido aquí...",
                          default_widget: str = 'default', default_image_url_fija: str = ""):
    # 1. Cargar Contenido Existente
    content_data = load_content(id_tema)

    if content_data:
        current_text = content_data['texto_md']
        current_widget = content_data['tipo_widget']
    else:
        current_text = default_text
        current_widget = default_widget

    # La imagen URL es FIJA, se pasa al renderizado y no se guarda en la DB.
    current_image_url = default_image_url_fija

    # Clave para el estado de edición
    edit_key = f'edit_{id_tema}'

    # 2. Lógica del Modo Edición
    if st.session_state.get(edit_key):
        # --- MODO EDICIÓN ---
        st.warning("Estás en **MODO EDICIÓN**. El contenido se guarda en `curso_osi.db`.")

        with st.form(key=f'form_edit_{id_tema}'):
            # Campo para editar el texto (dinámico)
            new_text = st.text_area(
                "Contenido (Markdown permitido)",
                value=current_text,
                height=250
            )

            # Selector para el tipo de caja/widget (dinámico)
            new_widget = st.selectbox(
                "Tipo de Caja de Texto:",
                options=['default', 'info', 'success', 'warning', 'error', 'columna_img'],
                index=['default', 'info', 'success', 'warning', 'error', 'columna_img'].index(current_widget),
                key=f'select_widget_{id_tema}'
            )

            # NUEVO: Si es columna_img, muestro la ruta estática A MODO INFORMATIVO, NO EDITABLE
            if new_widget == 'columna_img':
                st.info(f"Ruta de Imagen Estática (Fija): **{current_image_url}**")

            # Botón de Guardar
            if st.form_submit_button("💾 Guardar Cambios"):
                # Se llama a save_content SIN la URL, ya que es estática.
                save_content(id_tema, titulo, new_text, new_widget)
                st.success("✅ Contenido guardado y persistido en la base de datos.")
                st.session_state[edit_key] = False  # Sale del modo edición
                st.rerun()

    else:
        # --- MODO VISUALIZACIÓN ---
        # Pasamos la URL estática al renderizado.
        render_content(current_text, current_widget, current_image_url)