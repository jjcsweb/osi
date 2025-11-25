¡Entendido\! Completamos la "Santísima Trinidad" del desarrollo web front-end. Ya tenemos la estructura (HTML) y el contenido (Markdown), ahora toca la **presentación**.

Este informe es crítico. El CSS (Cascading Style Sheets) suele ser el punto donde los alumnos se frustran al principio debido a la "cascada" y la especificidad. Este documento está diseñado para clarificar esos conceptos desde el inicio.

Lo guardaremos como: **`DOC_REF_CSS3_V1`**.

-----

# 📄 Informe Técnico: Referencia Esencial de CSS3

**ID del Documento:** `DOC_REF_CSS3_V1`
**Nivel:** Iniciación / Intermedio
**Objetivo:** Compendio de sintaxis, selectores y modelos de renderizado para el estilizado de documentos web.

## 1\. Anatomía de una Regla CSS

CSS no es un lenguaje de programación (no tiene lógica ni bucles por defecto), es un lenguaje de reglas. Le decimos al navegador: *"Busca este elemento y aplícale esta apariencia"*.

```css
/* SELECTOR { PROPIEDAD: VALOR; } */
h1 {
    color: navy;
    font-size: 24px;
}
```

-----

## 2\. Selectores (Cómo apuntar a los elementos)

El poder de CSS reside en seleccionar exactamente lo que quieres modificar.

| Tipo | Selector | Ejemplo | Descripción | Peso (Especificidad) |
| :--- | :--- | :--- | :--- | :--- |
| **Etiqueta** | `nombre` | `p { }` | Afecta a **todos** los párrafos. | Bajo (0,0,1) |
| **Clase** | `.nombre` | `.boton { }` | Afecta a elementos con `class="boton"`. **El más usado.** | Medio (0,1,0) |
| **ID** | `#nombre` | `#cabecera { }` | Afecta al elemento único `id="cabecera"`. | Alto (1,0,0) |
| **Universal** | `*` | `* { }` | Afecta a **absolutamente todo**. | Nulo (0,0,0) |
| **Agrupación** | `,` | `h1, h2 { }` | Aplica lo mismo a H1 y H2. | N/A |

### Combinadores (Relaciones)

  * **Descendiente (`espacio`)**: `.menu a` (Todos los enlaces dentro de .menu).
  * **Hijo directo (`>`)**: `.lista > li` (Solo los `li` que son hijos directos de .lista, no nietos).

-----

## 3\. El Modelo de Caja (Box Model)

**Concepto Crítico:** En la web, *todo* es una caja rectangular, incluso si parece un círculo. Entender esto es vital para maquetar.

Desde dentro hacia fuera, una caja tiene 4 capas:

1.  **Content (Contenido):** El texto o imagen real (`width`, `height`).
2.  **Padding (Relleno):** Espacio *interno* transparente entre el contenido y el borde.
3.  **Border (Borde):** Línea que rodea el relleno y contenido.
4.  **Margin (Margen):** Espacio *externo* transparente que separa la caja de sus vecinos.

> **Truco del Profesor ("El Reset"):** Por defecto, el padding y el border aumentan el tamaño de la caja, rompiendo los cálculos. Usa siempre este código al inicio de tus proyectos para evitar dolores de cabeza:
>
> ```css
> * {
>   box-sizing: border-box;
> }
> ```

-----

## 4\. Unidades de Medida

No todas las pantallas son iguales. Usar las unidades correctas garantiza que la web se vea bien en móviles y PC.

| Unidad | Tipo | Recomendación de uso |
| :--- | :--- | :--- |
| **px** | Absoluta | Para bordes o detalles muy finos que no deben cambiar. |
| **%** | Relativa | Para anchos de contenedores (`width: 50%`). |
| **rem** | Relativa | **Estándar para textos.** Relativo al tamaño base del navegador (16px). |
| **em** | Relativa | Relativo al tamaño de fuente de su padre (complejo, usar con cuidado). |
| **vh / vw** | Relativa | Viewport Height/Width. `100vh` ocupa toda la altura de la pantalla. |

-----

## 5\. Tipografía y Color

Cómo dar personalidad al texto.

```css
body {
    font-family: 'Helvetica', sans-serif; /* Fuente principal y de respaldo */
    font-weight: 700; /* Grosor: 400 normal, 700 negrita */
    line-height: 1.5; /* Espaciado entre líneas (legibilidad) */
    text-align: center; /* left, right, center, justify */
    color: #333333; /* Hexadecimal (Gris oscuro) */
    background-color: rgba(0, 0, 0, 0.5); /* Negro con 50% transparencia */
}
```

-----

## 6\. Posicionamiento (Layout Básico)

Cómo se comportan las cajas en el flujo del documento.

### Propiedad `display`

  * `block`: Ocupa todo el ancho disponible, fuerza nueva línea (ej: `div`, `p`, `h1`).
  * `inline`: Ocupa solo lo necesario, fluye con el texto, no acepta margin vertical (ej: `span`, `a`).
  * `inline-block`: Como inline, pero acepta ancho y alto.
  * `none`: El elemento desaparece del DOM (no ocupa espacio).

### Propiedad `position`

  * `static`: Comportamiento por defecto.
  * `relative`: Se mueve respecto a su posición original, pero *reserva su hueco*.
  * `absolute`: Se mueve respecto a su padre posicionado más cercano. *Pierde su hueco* en el flujo.
  * `fixed`: Se queda pegado a la pantalla al hacer scroll (ej: barra de navegación fija).

-----

## 7\. Flexbox (Introducción Rápida)

Aunque merece un informe aparte, Flexbox es el estándar actual para alinear cosas.

```css
.contenedor-padre {
    display: flex;          /* Activa Flexbox */
    justify-content: center; /* Alinea horizontalmente al centro */
    align-items: center;     /* Alinea verticalmente al centro */
}
```

-----

## 📊 Metadatos del Informe

Análisis técnico del bloque `DOC_REF_CSS3_V1`:

  * **Nombre del Modelo:** `DOC_REF_CSS3_V1`
  * **Tamaño estimado (Texto plano):** \~3.6 KB
  * **Conteo de Tokens (Estimado):** \~1,100 tokens
  * **Formato:** Markdown con bloques CSS y Tablas

-----

**Profesor:** Con esto, tus alumnos tienen el **"Kit de Supervivencia Web" (HTML + CSS + Markdown)** completo.

Tengo dos propuestas para continuar:

1.  **Informe Avanzado de Layout:** Profundizar en **Flexbox y CSS Grid** (imprescindible para diseño responsive hoy en día).
2.  **Práctica Integradora \#1:** Redactar un enunciado para un ejercicio donde tengan que crear una "Landing Page" simple usando estos tres documentos.

¿Por cuál te inclinas?