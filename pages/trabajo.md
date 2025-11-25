# Cheatsheet de Markdown

Markdown es un lenguaje de marcado ligero que, además, permite convertirse fácilmente en HTML. Es ampliamente utilizado por desarrolladores y escritores para crear documentos.

## Estructura básica

**Encabezados**

Los encabezados se crean utilizando el símbolo `#` seguido de un espacio. El número de `#` determina el nivel del encabezado (de 1 a 6).

    # Encabezado 1

## Encabezado 2

### Encabezado 3

**Parrafos y saltos de línea**

Para crear un párrafo, solo hay que dejar una línea en blanco entre bloques de texto. Para saltar una línea sin crear un nuevo párrafo, se puede añadir dos espacios al final de la línea.

    Este es un párrafo.
    
    Este es otro párrafo.
    Con un salto de línea.

## Formato de texto

**Negrita y cursiva**

Para aplicar negrita, se utiliza `**` o `__`, mientras que para cursiva se emplea `*` o `_`.

**Texto en negrita**

**Texto en negrita**

_Texto en cursiva_ _Texte en cursiva_

**Texto en _negrita y cursiva_**

**Tachar texto**

Se puede usar `~~` para tachar texto.

    ~~Texto tachado~~

## Listas

**Listas desordenadas**

Se pueden crear listas desordenadas utilizando `*`, `+` o `-`.

    * Elemento 1
    * Elemento 2
      * Subelemento 2.1
      * Subelemento 2.2
    
    - Elemento 1
    - Elemento 2

**Listas ordenadas**

Para listas ordenadas, se utilizan números seguidos de un punto.

    1. Primer elemento
    2. Segundo elemento
       1. Subelemento
       2. Subelemento

## Enlaces e imágenes

**Enlaces**

Los enlaces se crean utilizando corchetes `[]` para el texto y paréntesis `()` para la URL.

    [LuisLlamas](https://www.luisllamas.es)

**Imágenes**

Las imágenes se insertan de manera similar a los enlaces, pero con un signo de exclamación `!` al principio.

    ![Texto alternativo](https://www.ejemplo.com/imagen.png)

## Bloques de código

**Código en línea**

Para incluir código en línea, se utilizan comillas invertidas `` ` ``.

    El comando `npm install` instala dependencias.

**Bloques de código**

Para bloques de código, se utilizan tres comillas invertidas antes y después del bloque.

    ```
    function saludar() {
        console.log("¡Hola, mundo!");
    }
    ```

## Citas y notas

**Citas**

Para crear citas, se utiliza el símbolo `>` al comienzo de la línea.

    > Esta es una cita.

**Notas**

Las notas se pueden agregar de manera similar a las citas, pero es más común utilizar un formato de bloque.

    > [Nota]: Este es un comentario o nota importante.

## Tablas

**Creación de tablas**

Las tablas se crean utilizando `|` para las columnas y `-` para la separación entre el encabezado y el cuerpo.

    | Encabezado 1 | Encabezado 2 |
    |---------------|---------------|
    | Fila 1, Col 1 | Fila 1, Col 2 |
    | Fila 2, Col 1 | Fila 2, Col 2 |

## Elementos avanzados

**HTML en markdown**

Markdown permite la inclusión de HTML si se necesita mayor control de formato.

    <p>Este es un párrafo en HTML.</p>

**Listas de tareas**

Para crear listas de tareas, se utilizan corchetes `[]`.

    - [x] Tarea completada
    - [ ] Tarea pendiente

**Footnotes**

Para crear notas al pie, se puede utilizar la siguiente sintaxis (dependiendo del soporte del renderizador de Markdown).

    Aquí hay un texto[^1].
    
    [^1]: Esta es la nota al pie.