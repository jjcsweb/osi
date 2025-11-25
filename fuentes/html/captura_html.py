import streamlit as st
import requests
import streamlit
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

# --- Configuración ---
URL_ORIGINAL = "https://creately.com/es/guides/tipos-de-mapas-conceptuales/"
NOMBRE_ARCHIVO_SALIDA = "mapas_conceptuales.html"
# --------------------

# **CABECERAS ANTI-BLOQUEO:** Simulamos ser un navegador estándar
'''HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}'''
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
}

def is_absolute(url):
    """Verifica si una URL es absoluta."""
    return bool(urlparse(url).netloc)


def capturar_y_estilizar(url, archivo_salida):
    """
    Descarga el HTML, identifica los enlaces a CSS y los incrusta
    dentro del HTML para visualización local, usando un User-Agent.
    """
    streamlit.write(f"Descargando contenido y estilos de: {url}...")

    # 1. Petición principal (con HEADERS)
    try:
        respuesta = requests.get(url, headers=HEADERS, timeout=15)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al acceder a la URL: {e}")
        return

    soup = BeautifulSoup(respuesta.text, 'html.parser')
    base_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"

    css_acumulado = ""
    elementos_a_eliminar = []

    # 2. Procesar enlaces a CSS externos
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if not href:
            continue

        css_url = urljoin(base_url, href) if not is_absolute(href) else href

        try:
            # Petición del CSS (también con HEADERS)
            css_respuesta = requests.get(css_url, headers=HEADERS, timeout=10)
            css_respuesta.raise_for_status()

            # Acumular el CSS y marcar la etiqueta <link> original para eliminar
            css_acumulado += "\n/* Estilos de: " + css_url + " */\n"
            css_acumulado += css_respuesta.text
            elementos_a_eliminar.append(link)
            st.write(f"   -> CSS externo incrustado: {css_url}")

        except requests.exceptions.RequestException as e:
            st.write(f"   ⚠️ No se pudo descargar el CSS de {css_url}. Ignorando. Error: {e}")

    # 3. Eliminar elementos interactivos y de enlace

    # Eliminar enlaces <link> de CSS externos procesados
    for elemento in elementos_a_eliminar:
        elemento.decompose()

        # Eliminar etiquetas <meta> (solicitado por el usuario para limpiar el HEAD)
        for meta in soup.find_all('meta'):
            meta.decompose()
        st.write("   -> Etiquetas <meta> eliminadas.")

        # Eliminar etiquetas <style> internas originales (solo queremos el CSS acumulado)
        for style in soup.find_all('style'):
            style.decompose()
        st.write("   -> Etiquetas <style> originales eliminadas.")

    # Eliminar scripts de JavaScript (elimina interactividad)
    for script in soup.find_all('script'):
        script.decompose()
    st.write("   -> Scripts de JavaScript eliminados.")

    # 4. Incrustar el CSS acumulado en el <head>
    if css_acumulado:
        tag_style = soup.new_tag('style')
        tag_style.string = css_acumulado

        head = soup.find('head')
        if head:
            head.append(tag_style)
            st.write("   -> CSS acumulado incrustado en el <head>.")
        else:
            soup.body.insert(0, tag_style)

        # --- Modificación en captura_html.py, cerca de la línea 99 ---

        # 5. Guardar el resultado final
        ruta_salida = os.path.join(os.path.dirname(__file__), archivo_salida)
        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            # ⚠️ CAMBIO CRUCIAL: Usar el serializador 'lxml' para prevenir la re-inserción de <meta>
            archivo.write(soup.prettify(formatter="html"))
            # Si no quieres el formato prettify, usa: archivo.write(str(soup.html.prettify()))

    st.write(f"\n✅ Captura visual guardada exitosamente en: **{archivo_salida}**")


# Ejecutar el proceso
if __name__ == "__main__":
    capturar_y_estilizar(URL_ORIGINAL, NOMBRE_ARCHIVO_SALIDA)