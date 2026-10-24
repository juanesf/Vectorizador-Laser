#!/usr/bin/env python3
"""Arma el Vectorizador Láser en un solo HTML que funciona sin internet.

Uso (desde la raíz del repositorio):
    python3 build/build.py              -> crea index.html
    python3 build/build.py --portable   -> además crea dist/VectorizadorLaser-portable.zip

No necesita paquetes extra: solo Python 3.8 o superior.
Las tipografías de assets/fonts ya vienen listas (reducidas a caracteres latinos, salvo las
que tienen "Reserved Font Name", que se incluyen sin modificar como pide la licencia OFL).
"""
import base64, json, os, re, sys, zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def ruta(*p): return os.path.join(RAIZ, *p)
def leer(*p, modo='r'):
    with open(ruta(*p), modo, **({} if 'b' in modo else {'encoding': 'utf-8'})) as f: return f.read()

def construir():
    fuentes = json.loads(leer('build', 'fuentes.json'))
    datos_fuentes = {f['key']: {'name': f['name'], 'group': f['group'],
                                'b64': base64.b64encode(leer('assets', 'fonts', f['file'], modo='rb')).decode()} for f in fuentes}
    iconos = {}
    for nombre in sorted(os.listdir(ruta('assets', 'icons'))):
        if nombre.endswith('.json.gz'):
            iconos[nombre[:-8]] = base64.b64encode(leer('assets', 'icons', nombre, modo='rb')).decode()
    h = leer('src', 'template.html')
    h = h.replace('__FONTS__', json.dumps(datos_fuentes, ensure_ascii=False)).replace('__ICONS__', json.dumps(iconos))
    libs = {'opentype': leer('vendor', 'opentype.min.js'), 'clipper': leer('vendor', 'clipper.js')}
    n = 0
    def incrustar(m):
        nonlocal n; n += 1
        js = libs['opentype' if 'opentype' in m.group(1) else 'clipper']
        return '<script>' + js.replace('</script', '<\\/script') + '</script>'
    h = re.sub(r'<script src="([^"]*(?:opentype\.min\.js|clipper\.js))"[^>]*></script>', incrustar, h)
    if n != 2: sys.exit('No se encontraron las dos librerías en src/template.html')
    html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + h + '</body></html>')
    with open(ruta('index.html'), 'w', encoding='utf-8') as f: f.write(html)
    print('index.html listo (%d KB)' % (len(html.encode()) // 1024))
    return html

def portable(html):
    os.makedirs(ruta('dist'), exist_ok=True)
    salida = ruta('dist', 'VectorizadorLaser-portable.zip')
    crlf = lambda s: s.replace('\r\n', '\n').replace('\n', '\r\n')
    with zipfile.ZipFile(salida, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr('VectorizadorLaser/Vectorizador Laser.html', html)
        z.writestr('VectorizadorLaser/LEEME.txt', crlf(leer('build', 'LEEME-portable.txt')))
        z.writestr('VectorizadorLaser/LICENCIAS-TERCEROS.txt', crlf(leer('LICENCIAS-TERCEROS.txt')))
        z.writestr('VectorizadorLaser/LICENSE.txt', crlf(leer('LICENSE')))
    print('dist/VectorizadorLaser-portable.zip listo (%d KB)' % (os.path.getsize(salida) // 1024))

if __name__ == '__main__':
    h = construir()
    if '--portable' in sys.argv: portable(h)
