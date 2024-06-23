import requests
from string import Template

html_template = Template('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves</title>
</head>
<body>

$contenido


</body>
</html>                        
''')


elem_template = Template('''<h2>$nombre</h2>
                            <img src="$imagen">
                        ''')



def request_get(url):
    return requests.get(url).json()

def build_html(url):
    response = request_get(url)[:10]
    texto = ''
    
    for ave in response:
        nombre_espanol = ave ['name']['spanish']
        nombre_ingles = ave['name']['english']
        nombre = f"{nombre_espanol} ({nombre_ingles})"
        detalle_url = f"https://aves.ninjas.cl/api/birds/{ave['uid']}"
        detalle = request_get(detalle_url)
        imagen_url = detalle['images']['main']
        texto += elem_template.substitute(nombre=nombre, imagen= imagen_url)
        
    return html_template.substitute(contenido=texto)
    

html = build_html('https://aves.ninjas.cl/api/birds')
with open('aves.html', 'w') as f:
    f.write(html)