import streamlit as st
import sys
import os
from funciones.mis_funciones import *


# --- CORRECCIÓN DE IMPORTS PARA STREAMLIT ---
# Esto permite que modulo_1.py encuentre los módulos ud_X_X.py
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# --- IMPORTS DE UNIDADES DIDÁCTICAS (UDs) ---

# UF1: Instalación y Actualización de Sistemas Operativos (7 UDs)
import ud_1_1_arquitectura
import ud_1_2_funciones_so
import ud_1_3_elementos_so
import ud_1_4_so_actuales
import ud_1_5_instalacion
import ud_1_6_replicacion
import ud_1_7_actualizacion  # <-- ¡ERROR CORREGIDO!

# UF2: Explotación de las funcionalidades del SO (6 UDs)
import ud_2_1_utilidades_so
import ud_2_2_organizacion_disco
import ud_2_3_accesibilidad
import ud_2_4_config_sistema
import ud_2_5_herramientas
import ud_2_6_gestion_procesos

# ---------------------------------------------


st.markdown(f"##### :green[MÓDULO 1. INSTALACIÓN Y CONFIGURACIÓN DE SISTEMAS OPERATIVOS]")

# PESTAÑAS PRINCIPALES: Dividen el Módulo 1 en sus dos Unidades Formativas (UF)
st.divider()
tab1, tab2 = st.tabs(
    ["Unidad Formativa 1: Instalación y actualización", "Unidad Formativa 2: Explotación de funcionalidades"],
    width="stretch")

# =========================================================================
# --- UNIDAD FORMATIVA 1 (UF1) ---
# =========================================================================
with tab1:
    st.header(":grey[*UF1 --*]" ":grey[ *Instalación y actualización de sistemas operativos*] ")

    # Define las pestañas para cada Unidad Didáctica (UD) de la UF1 (7 UDs)
    ud_tab1, ud_tab2, ud_tab3, ud_tab4, ud_tab5, ud_tab6, ud_tab7 = st.tabs(
        [
            "UD 1: Arquitecturas",
            "UD 2: Funciones S.O.",
            "UD 3: Elementos S.O.",
            "UD 4: S.O. Actuales",
            "UD 5: Instalación",
            "UD 6: Replicación",
            "UD 7: Actualización"
        ]
    )

    # Contenido de la UD 1.1

    with ud_tab1:
        ud_1_1_arquitectura.show_ud_1_1()

        # Contenido de la UD 1.2
    with ud_tab2:
        ud_1_2_funciones_so.show_ud_1_2()

        # Contenido de la UD 1.3
    with ud_tab3:
        ud_1_3_elementos_so.show_ud_1_3()

        # Contenido de la UD 1.4
    with ud_tab4:
        ud_1_4_so_actuales.show_ud_1_4()

        # Contenido de la UD 1.5
    with ud_tab5:
        ud_1_5_instalacion.show_ud_1_5()

        # Contenido de la UD 1.6
    with ud_tab6:
        ud_1_6_replicacion.show_ud_1_6()

        # Contenido de la UD 1.7
    with ud_tab7:
        ud_1_7_actualizacion.show_ud_1_7()

    # =========================================================================
# --- UNIDAD FORMATIVA 2 (UF2) ---
# =========================================================================
with tab2:
    st.header(":grey[*UF2 --*]" ":grey[ *Explotación de las funcionalidades del Sistema Operativo*] ")

    # Define las pestañas para cada Unidad Didáctica (UD) de la UF2 (6 UDs)
    ud_tab_a, ud_tab_b, ud_tab_c, ud_tab_d, ud_tab_e, ud_tab_f = st.tabs(
        [
            "UD 1: Utilidades SO",
            "UD 2: Org. Disco/Archivos",
            "UD 3: Accesibilidad",
            "UD 4: Config. Sistema",
            "UD 5: Herramientas",
            "UD 6: Gestión de Procesos"
        ]
    )

    # Contenido de la UD 2.1
    with ud_tab_a:
        ud_2_1_utilidades_so.show_ud_2_1()

        # Contenido de la UD 2.2
    with ud_tab_b:
        ud_2_2_organizacion_disco.show_ud_2_2()

        # Contenido de la UD 2.3
    with ud_tab_c:
        ud_2_3_accesibilidad.show_ud_2_3()

        # Contenido de la UD 2.4
    with ud_tab_d:
        ud_2_4_config_sistema.show_ud_2_4()

        # Contenido de la UD 2.5
    with ud_tab_e:
        ud_2_5_herramientas.show_ud_2_5()

        # Contenido de la UD 2.6
    with ud_tab_f:
        ud_2_6_gestion_procesos.show_ud_2_6()