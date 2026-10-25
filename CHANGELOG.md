# Cambios

## 1.2.1 — 2026-10-25

- Diseño libre: las tramas de foto guardan la foto original y aceptan todos los tipos de trama (Floyd–Steinberg, Atkinson, Jarvis, Stucki, Sierra, Bayer, puntos, líneas, umbral, boceto y escala de grises). También se ajustan el punto del láser, el ángulo, el contraste, el brillo y la opción de invertir.
- Al cambiar el tamaño de una trama en Diseño libre, se recalcula sola para conservar el tamaño de punto del láser.
- Herramientas → “Enviar a Diseño libre” ahora envía la foto como trama editable.

## 1.2.0 — 2026-10-25

- Diseño libre: la selección usa la forma real de cada objeto (no su rectángulo). Al hacer clic se elige el objeto más chico bajo el puntero, o el contorno que estás tocando.
- Clic otra vez en el mismo lugar: elige el objeto de abajo y avisa cuál es (por ejemplo “2 de 3”).
- Al pasar el mouse se resalta el objeto que se va a seleccionar.
- Lista de objetos con nombres numerados cuando se repiten (“Silueta 1”, “Silueta 2”) y botón × para eliminar cada uno. Al pasar el mouse sobre la lista, el objeto se resalta en la vista (en rojo sobre ×).
- La cuadrícula ahora va de 5 a 100 mm.

## 1.1.1 — 2026-10-25

- Foto a trama: nuevo botón “Enviar la trama a Diseño libre”. La trama llega como imagen (con su contorno de corte, si lo tiene) y se puede mover, escalar, girar y espejar junto al resto del cartel. Las tramas de círculos vectoriales llegan como vectores.
- Diseño libre: las tramas de foto salen en SVG, PNG y LightBurn (como imagen en su propia capa). En DXF, PDF, EPS, PLT y Ruida sale solo lo vectorial, con un aviso.

## 1.1.0 — 2026-10-25

- Área de trabajo de la máquina configurable junto a las unidades (por ejemplo 600 × 400 mm), con medidas comunes. Se dibuja en la vista previa y avisa si el diseño no cabe.
- Cuadrícula con regla en milímetros (o la unidad elegida), ajustable de 5 a 100 mm. Por defecto mide 50 mm.
- Todos los controles deslizantes permiten escribir el número directamente.
- Herramientas → Quitar fondo / Recortar con forma: nuevo botón “Enviar a Diseño libre”. La foto llega como trama de puntos vectorial, junto con su contorno de corte y alineada con él.
- Diseño libre: las imágenes tienen estilo “Umbral” (dibujos y logos) o “Trama de puntos” (fotos), con tamaño de celda y punto mínimo.
- Diseño libre: botón “Usar el área de la máquina”.

## 1.0.0 — 2026-10-23

Primera versión pública.

- Letras, números y palabras con 44 tipografías libres; estilos entera, solo bordes y con patrón (con ángulo ajustable).
- Edición: cortar, unir, ranurar, limpiar, engrosar y contenido interno (textos, fechas, formas, imágenes).
- Vectorizado de imágenes con limpieza automática.
- Alcancía por capas (MDF + acrílico) con nombre en tipografía a elección.
- Diseño libre de carteles con objetos independientes, galería de formas e íconos sin conexión.
- Foto a trama (dithering) con tamaño de punto del láser y exportación BMP de 1 bit.
- Herramientas: quitar fondo, recortar con forma, perfiles de material, pruebas de enfoque, potencia/velocidad y kerf.
- Generador de cajas con 10 tipos: simple, tapa deslizante, bisagra flexible, bandeja con divisiones, redondeada, redonda, corazón, cofre, casita y alcancía con tapón.
- Exportación SVG, DXF, PDF, EPS, PLT, PNG, BMP, LightBurn (.lbrn2) y Ruida (.rd, beta).
- Selector de unidades (mm, cm, pulgadas), guardado automático, proyectos y versión portable sin internet.
