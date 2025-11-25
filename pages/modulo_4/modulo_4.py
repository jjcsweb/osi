import streamlit as st
import sys
import os

# --- Ajuste del path para asegurar la importación de las UDs ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# --- IMPORTS DE UNIDADES DIDÁCTICAS (UDs) ---

# UF1: Asistencia de usuarios (4 UDs)
import ud_4_1_1_comunicacion
import ud_4_1_2_correo_agenda
import ud_4_1_3_cifrado
import ud_4_1_4_firma_electronica

# (Aquí se importarán las UDs de las UF 2, 3, 4 y 5 en el futuro)

# ---------------------------------------------

st.divider()
st.markdown(f"##### :green[MÓDULO 4. APLICACIONES MICROINFORMÁTICAS]")

# PESTAÑAS PRINCIPALES (5 Unidades Formativas)
st.divider()
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "UF1: Asistencia y Correo",
    "UF2: Documentos de Texto",
    "UF3: Hojas de Cálculo",
    "UF4: Presentaciones",
    "UF5: Gráficos e Imágenes"
], width="stretch")

# =========================================================================
# --- UNIDAD FORMATIVA 1 (UF1) ---
# =========================================================================
with tab1:
    st.header(
        ":grey[*UNIDAD FORMATIVA 1 --*]" ":grey[ *Asistencia de usuarios en el uso de aplicaciones ofimáticas y de correo electrónico*] ")
    st.divider()

    # UF1 tiene 4 Unidades Didácticas
    ud_tab1, ud_tab2, ud_tab3, ud_tab4 = st.tabs(
        [
            "UD 1: Técnicas de Comunicación",
            "UD 2: Correo y Agenda",
            "UD 3: Cifrado de Correos",
            "UD 4: Firma Electrónica"
        ]
    )

    with ud_tab1:
        ud_4_1_1_comunicacion.show_ud_4_1_1()

    with ud_tab2:
        ud_4_1_2_correo_agenda.show_ud_4_1_2()

    with ud_tab3:
        ud_4_1_3_cifrado.show_ud_4_1_3()

    with ud_tab4:
        ud_4_1_4_firma_electronica.show_ud_4_1_4()

# =========================================================================
# --- OTRAS UNIDADES FORMATIVAS (Estructura preparada) ---
# =========================================================================
with tab2:
    st.header(":grey[*UNIDAD FORMATIVA 2 --*]" ":grey[ *Elaboración de documentos de texto*] ")
    st.info("Contenido en desarrollo...")

with tab3:
    st.header(":grey[*UNIDAD FORMATIVA 3 --*]" ":grey[ *Elaboración de hojas de cálculo*] ")
    st.info("Contenido en desarrollo...")

with tab4:
    st.header(":grey[*UNIDAD FORMATIVA 4 --*]" ":grey[ *Elaboración de presentaciones*] ")
    st.info("Contenido en desarrollo...")

with tab5:
    st.header(
        ":grey[*UNIDAD FORMATIVA 5 --*]" ":grey[ *Elaboración y modificación de imágenes u otros elementos gráficos*] ")
    st.info("Contenido en desarrollo...")