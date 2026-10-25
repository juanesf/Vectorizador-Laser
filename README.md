# Vectorizador Láser

Programa para crear y preparar archivos de corte y grabado con láser CO₂. Convierte letras, números, palabras e imágenes en vectores, diseña cajas y carteles, transforma fotos en tramas y exporta a los formatos que usan LightBurn, RDWorks, Inkscape, CorelDRAW e Illustrator.

Es **un solo archivo HTML** que funciona en el navegador **sin instalar nada y sin internet**: tipografías, íconos y librerías vienen incluidos.

**Autores:** Cecilia Vivot y Juan Sanchez · Co-asistido por Claude (Anthropic)
**Licencia:** [GPL-3.0 o posterior](LICENSE)

---

## Cómo usarlo

1. Descarga `index.html` (o el `.zip` portable de la sección *Releases*).
2. Ábrelo con doble clic en Chrome, Edge, Firefox o Safari actualizados.
3. Arriba, junto a las unidades, configura el **área de trabajo de tu máquina** (por ejemplo 600 × 400 mm) y el tamaño de la cuadrícula.
4. Tu trabajo se guarda solo en el navegador. Para llevarlo a otro computador usa **Guardar proyecto** y después **Abrir proyecto**.

También puedes usarlo en línea activando **GitHub Pages** en este repositorio (Settings → Pages → rama `main`, carpeta raíz). Queda disponible en `https://<tu-usuario>.github.io/vectorizador-laser/`.

## Qué hace

| Pestaña | Para qué sirve |
|---|---|
| **Letras · Números · Palabras** | Texto con 44 tipografías libres. Estilos: entera, solo bordes o rellena con patrones (estrellas, lunas, dinosaurios, gatos…). Unir letras, ranuras, limpieza y contenido interno (textos, fechas, formas, imágenes). |
| **Imagen** | Vectoriza logos y dibujos. Limpieza de restos, engrosado de líneas finas y “conservar solo la figura principal”. |
| **Alcancía por capas** | Alcancía con la inicial de un nombre, en capas de MDF y acrílico, con el nombre en la tipografía que elijas. |
| **Diseño libre** | Carteles y letreros con formas, textos, imágenes (umbral o trama de puntos) e íconos que se mueven y editan por separado. Unir/separar, duplicar, copia matricial y espejar. |
| **Decoradores** | Relojes de pared, toppers para torta, mandalas, sets de mariposas y flores, y llaveros con nombre. Se pueden seguir editando en Diseño libre. |
| **Foto a trama** | Convierte fotos en puntos (Floyd-Steinberg, Atkinson, Stucki, Bayer, semitono…), con el tamaño de punto del láser. Exporta BMP de 1 bit con DPI. |
| **Herramientas** | Quitar fondo, recortar fotos con formas, perfiles de material, pruebas de enfoque, potencia/velocidad y kerf, y **generador de cajas**. |

### Generador de cajas

Diez tipos, todos con compensación de kerf y nombre grabado en cada pieza:

- **Simple** con uniones dentadas y tapa opcional
- **Tapa deslizante** sobre rieles
- **Tapa con bisagra flexible** (bisagra viva)
- **Bandeja con divisiones** que se cruzan
- **Redondeada flexible**, **Redonda** y **Corazón** con pared de bisagra viva y tapa que calza
- **Cofre** con tapa curva
- **Casita** (sirve como casita para pájaros)
- **Alcancía con tapón** giratorio en la base

### Formatos de salida

| Formato | Uso |
|---|---|
| SVG, DXF, PDF, EPS, PLT | Diseño editable para LightBurn, RDWorks, Inkscape, CorelDRAW, Illustrator, AutoCAD |
| PNG, BMP | Imagen para grabado (con DPI correcto) |
| **LightBurn (.lbrn2)** | Proyecto con las capas, potencia y velocidad ya configuradas |
| **Ruida (.rd)** · *beta* | Archivo que la máquina con controlador Ruida lee desde un pendrive |

Colores por capa: **rojo** = corte, **negro** = grabado, **azul** = guía (no se corta).

> **Seguridad:** revisa siempre potencia y velocidad antes de cortar. El archivo `.rd` es experimental: pruébalo primero con baja potencia y usa *Frame / Marco* en el panel para ver dónde trabajará el láser. Nunca dejes la máquina sola mientras corta.

## Armar el HTML desde el código

Solo necesitas Python 3.8 o superior, sin paquetes extra:

```bash
python3 build/build.py              # crea index.html
python3 build/build.py --portable   # además crea dist/VectorizadorLaser-portable.zip
```

### Estructura

```
src/template.html          código de la aplicación (HTML + CSS + JavaScript)
assets/fonts/              tipografías incluidas (OFL / Apache 2.0)
assets/icons/              bibliotecas de íconos comprimidas (MIT / Apache 2.0)
vendor/                    opentype.js (MIT) y Clipper (Boost)
build/build.py             arma index.html y el zip portable
build/fuentes.json         lista de tipografías y sus grupos
index.html                 aplicación lista para usar (generada)
```

Después de cambiar `src/template.html`, vuelve a correr `build/build.py` y sube también `index.html`.

## Licencia

Vectorizador Láser es software libre: puedes usarlo, estudiarlo, modificarlo y compartirlo bajo los términos de la **GNU General Public License versión 3 o posterior** (ver [LICENSE](LICENSE)). Si distribuyes una versión modificada, debe mantener la misma licencia y entregar su código.

**Lo que fabriques con el programa es tuyo.** Las piezas cortadas o grabadas y los archivos que exportes no quedan sujetos a la GPL y puedes venderlos libremente.

Componentes de terceros y sus licencias: [LICENCIAS-TERCEROS.txt](LICENCIAS-TERCEROS.txt).

## Créditos

- [opentype.js](https://github.com/opentypejs/opentype.js) — MIT
- [Clipper](http://www.angusj.com/delphi/clipper.php) (clipper-lib) — Boost Software License
- Tipografías de [Google Fonts](https://fonts.google.com) — SIL Open Font License / Apache 2.0
- Íconos: Fluent Emoji High Contrast (Microsoft, MIT), Material Design Icons (Pictogrammers, Apache 2.0), Phosphor (MIT), Tabler (MIT)
- Formato Ruida `.rd`: codificación documentada por [meerk40t](https://github.com/meerk40t/meerk40t) (MIT)
- Ideas de tipos de caja inspiradas en [boxes.py](https://github.com/florianfesti/boxes) de Florian Festi (implementación propia)
