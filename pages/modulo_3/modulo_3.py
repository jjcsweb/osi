import streamlit as st
import sys
import os

# --- Ajuste del path para asegurar la importación de las UDs ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# --- IMPORTS DE UNIDADES DIDÁCTICAS (UDs) ---
# UF1 Simulada: Instalación
import ud_3_1_recursos_sistema
import ud_3_2_requisitos_sistema
import ud_3_3_licencias_software
import ud_3_4_instalacion_aplicaciones

# UF2 Simulada: Aplicaciones / Mantenimiento
import ud_3_5_diagnostico_averias
import ud_3_6_antivirus

# ---------------------------------------------

st.divider()
st.markdown(f"##### :green[MÓDULO 3. INSTALACIÓN Y CONFIGURACIÓN DE APLICACIONES INFORMÁTICAS]")

# PESTAÑAS PRINCIPALES (Simulando UFs según instrucciones)
st.divider()
tab1, tab2 = st.tabs([
    "UF1: Instalación de aplicaciones",
    "UF2: Aplicaciones informáticas"
], width="stretch")

# =========================================================================
# --- UF1: Instalación de aplicaciones (UDs 1-4) ---
# =========================================================================
with tab1:
    st.header(":grey[*UNIDAD FORMATIVA 1 --*]" ":grey[ *Instalación de aplicaciones*] ")
    st.divider()

    ud_tab1, ud_tab2, ud_tab3, ud_tab4 = st.tabs(
        [
            "UD 1: Recursos del Sistema",
            "UD 2: Requisitos",
            "UD 3: Licencias",
            "UD 4: Instalación"
        ]
    )

    with ud_tab1:
        ud_3_1_recursos_sistema.show_ud_3_1()

    with ud_tab2:
        ud_3_2_requisitos_sistema.show_ud_3_2()

    with ud_tab3:
        ud_3_3_licencias_software.show_ud_3_3()

    with ud_tab4:
        ud_3_4_instalacion_aplicaciones.show_ud_3_4()

# =========================================================================
# --- UF2: Aplicaciones informáticas (UDs 5-6) ---
# =========================================================================
with tab2:
    st.header(":grey[*UNIDAD FORMATIVA 2 --*]" ":grey[ *Aplicaciones informáticas y Mantenimiento*] ")
    st.divider()

    ud_tab_a, ud_tab_b = st.tabs(
        [
            "UD 5: Diagnóstico y Averías",
            "UD 6: Antivirus"
        ]
    )

    with ud_tab_a:
        ud_3_5_diagnostico_averias.show_ud_3_5()

    with ud_tab_b:
        ud_3_6_antivirus.show_ud_3_6()