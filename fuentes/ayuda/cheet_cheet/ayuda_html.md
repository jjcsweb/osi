   ¡Excelente iniciativa\! Continuamos construyendo el repositorio. El HTML (HyperText Markup Language) es el cimiento de la web; sin él, no hay nada que estilizar ni programar.

Este documento sigue la misma estructura rigurosa del anterior para mantener la coherencia en el material didáctico de tus alumnos. Lo guardaremos como: **`DOC_REF_HTML5_V1`**.

Este informe se centra en **HTML5 Semántico**, que es el estándar actual y profesional que debemos inculcar a los futuros técnicos desde el día uno.

-----

# 📄 Informe Técnico: Referencia Esencial de HTML5 Semántico

**ID del Documento:** `DOC_REF_HTML5_V1`
**Nivel:** Iniciación / Intermedio
**Objetivo:** Proveer una guía rápida de sintaxis, estructura y etiquetas semánticas para el desarrollo web moderno.

## 1\. Estructura Base del Documento (Boilerplate)

Todo documento HTML5 válido debe comenzar con esta estructura mínima. Es el lienzo sobre el que trabajarán los navegadores.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Descripción del sitio para SEO">
    <title>Título de la Pestaña</title>
</head>
<body>
    </body>
</html>
```

> **Nota del Profesor:** El `<meta charset="UTF-8">` es crucial. Sin él, los acentos y caracteres especiales (ñ) se verán como errores (glifos extraños) en el navegador.

-----

## 2\. Etiquetas Semánticas (Estructura del Layout)

En HTML5, no usamos `<div>` para todo. Usamos etiquetas que describen *qué es* el contenido. Esto es vital para el SEO (Google) y la Accesibilidad (Lectores de pantalla).

| Etiqueta | Descripción y Uso Correcto |
| :--- | :--- |
| `<header>` | Cabecera del sitio o de una sección. Suele contener el logo y menú principal. |
| `<nav>` | Bloque de enlaces de navegación principales. |
| `<main>` | Contenido principal y único de la página. **Solo debe haber uno por página.** |
| `<section>` | Agrupa contenido temático relacionado. Debe tener un título (`h2`-`h6`). |
| `<article>` | Contenido independiente y autónomo (ej. un post de blog, una noticia). |
| `<aside>` | Contenido tangencial o relacionado indirectamente (barras laterales, publicidad). |
| `<footer>` | Pie de página. Copyright, enlaces legales, contacto. |
| `<div>` | Contenedor genérico **sin significado semántico**. Úsalo solo para agrupar por estilos CSS. |

-----

## 3\. Texto y Enlaces

Las herramientas fundamentales para mostrar información.

| Categoría | Etiqueta | Función | Atributos Clave |
| :--- | :--- | :--- | :--- |
| **Títulos** | `<h1>` a `<h6>` | Jerarquía de títulos. `h1` es el más importante. | N/A |
| **Párrafos** | `<p>` | Bloques de texto estándar. | N/A |
| **Enlaces** | `<a>` | Crea hipervínculos. | `href="url"`, `target="_blank"` (abre nueva pestaña) |
| **Énfasis** | `<strong>` | Importancia fuerte (Negrita semántica). | N/A |
| **Énfasis** | `<em>` | Énfasis de voz (Cursiva semántica). | N/A |
| **Listas** | `<ul>` + `<li>` | Lista desordenada (puntos). | N/A |
| **Listas** | `<ol>` + `<li>` | Lista ordenada (números). | N/A |

-----

## 4\. Imágenes y Multimedia

El contenido visual enriquece la experiencia, pero debe manejarse con cuidado para no afectar el rendimiento.

### Imágenes

```html
<img src="ruta/imagen.jpg" alt="Descripción textual de la imagen" width="500" height="300">
```

> **Importante:** El atributo `alt` es obligatorio por validación y accesibilidad. Si la imagen no carga, se muestra este texto.

### Video (Nativo)

```html
<video controls poster="miniatura.jpg">
    <source src="video.mp4" type="video/mp4">
    Tu navegador no soporta video.
</video>
```

-----

## 5\. Formularios Interactivos

Es la vía principal de comunicación usuario-servidor. Se agrupan en la etiqueta `<form>`.

**Ejemplo de Estructura:**

```html
<form action="/enviar-datos" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre_usuario" required>
    
    <button type="submit">Enviar</button>
</form>
```

**Tipos de Input (`<input type="...">`) comunes:**

| Tipo (`type`) | Uso | Validación Navegador |
| :--- | :--- | :--- |¡Excelente iniciativa\! Continuamos construyendo el repositorio. El HTML (HyperText Markup Language) es el cimiento de la web; sin él, no hay nada que estilizar ni programar.

Este documento sigue la misma estructura rigurosa del anterior para mantener la coherencia en el material didáctico de tus alumnos. Lo guardaremos como: **`DOC_REF_HTML5_V1`**.

Este informe se centra en **HTML5 Semántico**, que es el estándar actual y profesional que debemos inculcar a los futuros técnicos desde el día uno.

-----

# 📄 Informe Técnico: Referencia Esencial de HTML5 Semántico

**ID del Documento:** `DOC_REF_HTML5_V1`
**Nivel:** Iniciación / Intermedio
**Objetivo:** Proveer una guía rápida de sintaxis, estructura y etiquetas semánticas para el desarrollo web moderno.

## 1\. Estructura Base del Documento (Boilerplate)

Todo documento HTML5 válido debe comenzar con esta estructura mínima. Es el lienzo sobre el que trabajarán los navegadores.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Descripción del sitio para SEO">
    <title>Título de la Pestaña</title>
</head>
<body>
    </body>
</html>
```

> **Nota del Profesor:** El `<meta charset="UTF-8">` es crucial. Sin él, los acentos y caracteres especiales (ñ) se verán como errores (glifos extraños) en el navegador.

-----

## 2\. Etiquetas Semánticas (Estructura del Layout)

En HTML5, no usamos `<div>` para todo. Usamos etiquetas que describen *qué es* el contenido. Esto es vital para el SEO (Google) y la Accesibilidad (Lectores de pantalla).

| Etiqueta | Descripción y Uso Correcto |
| :--- | :--- |
| `<header>` | Cabecera del sitio o de una sección. Suele contener el logo y menú principal. |
| `<nav>` | Bloque de enlaces de navegación principales. |
| `<main>` | Contenido principal y único de la página. **Solo debe haber uno por página.** |
| `<section>` | Agrupa contenido temático relacionado. Debe tener un título (`h2`-`h6`). |
| `<article>` | Contenido independiente y autónomo (ej. un post de blog, una noticia). |
| `<aside>` | Contenido tangencial o relacionado indirectamente (barras laterales, publicidad). |
| `<footer>` | Pie de página. Copyright, enlaces legales, contacto. |
| `<div>` | Contenedor genérico **sin significado semántico**. Úsalo solo para agrupar por estilos CSS. |

-----

## 3\. Texto y Enlaces

Las herramientas fundamentales para mostrar información.

| Categoría | Etiqueta | Función | Atributos Clave |
| :--- | :--- | :--- | :--- |
| **Títulos** | `<h1>` a `<h6>` | Jerarquía de títulos. `h1` es el más importante. | N/A |
| **Párrafos** | `<p>` | Bloques de texto estándar. | N/A |
| **Enlaces** | `<a>` | Crea hipervínculos. | `href="url"`, `target="_blank"` (abre nueva pestaña) |
| **Énfasis** | `<strong>` | Importancia fuerte (Negrita semántica). | N/A |
| **Énfasis** | `<em>` | Énfasis de voz (Cursiva semántica). | N/A |
| **Listas** | `<ul>` + `<li>` | Lista desordenada (puntos). | N/A |
| **Listas** | `<ol>` + `<li>` | Lista ordenada (números). | N/A |

-----

## 4\. Imágenes y Multimedia

El contenido visual enriquece la experiencia, pero debe manejarse con cuidado para no afectar el rendimiento.

### Imágenes

```html
<img src="ruta/imagen.jpg" alt="Descripción textual de la imagen" width="500" height="300">
```

> **Importante:** El atributo `alt` es obligatorio por validación y accesibilidad. Si la imagen no carga, se muestra este texto.

### Video (Nativo)

```html
<video controls poster="miniatura.jpg">
    <source src="video.mp4" type="video/mp4">
    Tu navegador no soporta video.
</video>
```

-----

## 5\. Formularios Interactivos

Es la vía principal de comunicación usuario-servidor. Se agrupan en la etiqueta `<form>`.

**Ejemplo de Estructura:**

```html
<form action="/enviar-datos" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre_usuario" required>
    
    <button type="submit">Enviar</button>
</form>
```

**Tipos de Input (`<input type="...">`) comunes:**

| Tipo (`type`) | Uso | Validación Navegador |
| :--- | :--- | :--- |
| `text` | Texto simple de una línea. | Ninguna. |
| `password` | Oculta los caracteres. | Ninguna. |
| `email` | Correos electrónicos. | Verifica formato `a@b.com`. |
| `number` | Solo números. | Permite rangos (`min`, `max`). |
| `date` | Selector de fecha (calendario). | Formato fecha nativo. |
| `checkbox` | Selección múltiple (casilla). | `checked` para marcar por defecto. |
| `radio` | Selección única (círculo). | Agrupar con mismo `name`. |

-----

## 6\. Atributos Globales

Estos atributos se pueden aplicar a prácticamente cualquier etiqueta HTML.

  * **`class`**: Clasifica elementos para aplicar estilos CSS (se puede repetir en varios elementos).
      * *Ejemplo:* `<p class="texto-destacado">`
  * **`id`**: Identificador **único** en toda la página (para JS o anclas internas).
      * *Ejemplo:* `<section id="contacto">`
  * **`style`**: Estilos CSS en línea (No recomendado, mejor usar hoja de estilos externa).
  * **`title`**: Muestra un *tooltip* (globo de texto) al pasar el ratón por encima.

-----

## 📊 Metadatos del Informe

Aquí tienes el análisis técnico de este bloque (`DOC_REF_HTML5_V1`):

  * **Nombre del Modelo:** `DOC_REF_HTML5_V1`
  * **Tamaño estimado (Texto plano):** \~3.8 KB
  * **Conteo de Tokens (Estimado):** \~1,150 tokens
  * **Formato:** Markdown con bloques de código HTML

-----

**Profesor, ¿cuál es el siguiente paso?** Podríamos crear ahora la hoja de referencia para **CSS3 (Selectores y Box Model)** para que los alumnos puedan empezar a dar estilo a este HTML, o quizás prefieres un **Ejercio Práctico combinando Markdown y HTML** para evaluar lo visto hasta ahora.
| `text` | Texto simple de una línea. | Ninguna. |
| `password` | Oculta los caracteres. | Ninguna. |
| `email` | Correos electrónicos. | Verifica formato `a@b.com`. |
| `number` | Solo números. | Permite rangos (`min`, `max`). |
| `date` | Selector de fecha (calendario). | Formato fecha nativo. |
| `checkbox` | Selección múltiple (casilla). | `checked` para marcar por defecto. |
| `radio` | Selección única (círculo). | Agrupar con mismo `name`. |

-----

## 6\. Atributos Globales

Estos atributos se pueden aplicar a prácticamente cualquier etiqueta HTML.

  * **`class`**: Clasifica elementos para aplicar estilos CSS (se puede repetir en varios elementos).
      * *Ejemplo:* `<p class="texto-destacado">`
  * **`id`**: Identificador **único** en toda la página (para JS o anclas internas).
      * *Ejemplo:* `<section id="contacto">`
  * **`style`**: Estilos CSS en línea (No recomendado, mejor usar hoja de estilos externa).
  * **`title`**: Muestra un *tooltip* (globo de texto) al pasar el ratón por encima.

-----

## 📊 Metadatos del Informe

Aquí tienes el análisis técnico de este bloque (`DOC_REF_HTML5_V1`):

  * **Nombre del Modelo:** `DOC_REF_HTML5_V1`
  * **Tamaño estimado (Texto plano):** \~3.8 KB
  * **Conteo de Tokens (Estimado):** \~1,150 tokens
  * **Formato:** Markdown con bloques de código HTML

-----

**Profesor, ¿cuál es el siguiente paso?** Podríamos crear ahora la hoja de referencia para **CSS3 (Selectores y Box Model)** para que los alumnos puedan empezar a dar estilo a este HTML, o quizás prefieres un **Ejercio Práctico combinando Markdown y HTML** para evaluar lo visto hasta ahora.