import streamlit as st
import sys
import os

# --- Ajuste del path para asegurar la importación de las UDs ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# --- IMPORTS DE UNIDADES DIDÁCTICAS (UDs) ---

# UF1: Instalación y configuración de los nodos (4 UDs)
import ud_1_1_arquitectura_redes
import ud_1_2_elementos_red_local
import ud_1_3_protocolos_red
import ud_1_4_instalacion_nodos

# UF2: Verificación y resolución de incidencias (5 UDs) - ¡CORREGIDO!
import ud_2_1_verificacion_conectividad
import ud_2_2_tipos_incidencias
import ud_2_3_deteccion_diagnostico
import ud_2_4_comprobacion_cables
import ud_2_5_solucion_incidencias  # ¡NUEVO IMPORT!

# ---------------------------------------------


st.divider()
st.markdown(f"##### :green[MÓDULO 2. IMPLANTACIÓN DE LOS ELEMENTOS DE LA RED LOCAL]")

# PESTAÑAS PRINCIPALES: Dividen el Módulo 2 en sus dos Unidades Formativas (UF)
st.divider()
tab1, tab2 = st.tabs([
    "Unidad Formativa 1: Instalación y configuración",
    "Unidad Formativa 2: Verificación y resolución de incidencias"
], width="stretch")

# =========================================================================
# --- UNIDAD FORMATIVA 1 (UF1) ---
# =========================================================================
with tab1:
    st.header(
        ":grey[*UNIDAD FORMATIVA 1 --*]" ":grey[ *Instalación y configuración de los nodos de una red de área local*] ")


    # Define las pestañas para cada Unidad Didáctica (UD) de la UF1 (4 UDs)
    ud_tab1, ud_tab2, ud_tab3, ud_tab4 = st.tabs(
        [
            "UD 1: Arquitectura de Redes",
            "UD 2: Elementos de Red Local",
            "UD 3: Protocolos de Red",
            "UD 4: Instalación de Nodos"
        ]
    )

    # Mapeo de contenidos UF1
    with ud_tab1:
        ud_1_1_arquitectura_redes.show_ud_1_1()

    with ud_tab2:
        ud_1_2_elementos_red_local.show_ud_1_2()

    with ud_tab3:
        ud_1_3_protocolos_red.show_ud_1_3()

    with ud_tab4:
        ud_1_4_instalacion_nodos.show_ud_1_4()

    # =========================================================================
# --- UNIDAD FORMATIVA 2 (UF2) ---
# =========================================================================
with tab2:
    st.header(
        ":grey[*UNIDAD FORMATIVA 2 --*]" ":grey[ *Verificación y resolución de incidencias en una red de área local*] ")


    # Define las pestañas para cada Unidad Didáctica (UD) de la UF2 (5 UDs) - ¡CORREGIDO!
    ud_tab_a, ud_tab_b, ud_tab_c, ud_tab_d, ud_tab_e = st.tabs(
        [
            "UD 1: Verificación y Prueba",
            "UD 2: Tipos de Incidencias",
            "UD 3: Detección y Diagnóstico",
            "UD 4: Comprobación de Cables",
            "UD 5: Solución Incidencias"  # ¡NUEVA PESTAÑA!
        ]
    )

    # Mapeo de contenidos UF2
    with ud_tab_a:
        ud_2_1_verificacion_conectividad.show_ud_2_1()

    with ud_tab_b:
        ud_2_2_tipos_incidencias.show_ud_2_2()

    with ud_tab_c:
        ud_2_3_deteccion_diagnostico.show_ud_2_3()

    with ud_tab_d:
        ud_2_4_comprobacion_cables.show_ud_2_4()

    with ud_tab_e:
        ud_2_5_solucion_incidencias.show_ud_2_5()  # ¡NUEVO MAPEO!