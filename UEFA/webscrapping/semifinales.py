import csv
import requests
from bs4 import BeautifulSoup

# URLs de diferentes temporadas de UEFA Champions League
urls = [
    "https://es.wikipedia.org/wiki/Liga_de_Campeones_de_la_UEFA_2021-22#Semifinales",
    "https://es.wikipedia.org/wiki/Liga_de_Campeones_de_la_UEFA_2020-21#Semifinales",
    "https://es.wikipedia.org/wiki/Liga_de_Campeones_de_la_UEFA_2019-20#Semifinales",
    "https://es.wikipedia.org/wiki/Liga_de_Campeones_de_la_UEFA_2018-19#Semifinales",
    "https://es.wikipedia.org/wiki/Liga_de_Campeones_de_la_UEFA_2017-18#Semifinales"
]

# Creamos una lista para almacenar los datos de todas las temporadas
datos_totales = []

# Iteramos sobre los URLs
for url in urls:

    # Realizamos una solicitud GET a la URL
    r = requests.get(url)
    # Extraemos el HTML de la respuesta
    html = r.text

    # Creamos un objeto BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Buscamos la sección de texto que contiene la información de los octavos
    semifinales_html = soup.find('span', id='Semifinales').find_next('table', class_='wikitable')

    # Obtenemos las filas de la tabla
    filas = semifinales_html.find_all('tr')

    # Iteramos sobre las filas y obtenemos los datos de cada celda
    for fila in filas:
        # Obtenemos las celdas de la fila
        celdas = fila.find_all(['th', 'td'])
        # Extraemos el texto de cada celda y lo agregamos a la lista de datos
        datos_fila = [celda.get_text(strip=True) for celda in celdas]
        # Agregamos la temporada como la primera columna en cada fila, extrayéndola de la URL directamente
        temporada = url.split('_')[-1]
        datos_fila.insert(0, temporada.split('#')[0])
        # Agregamos la fila a la lista de datos totales
        datos_totales.append(datos_fila)

# Cambiamos el encabezado de la primera columna
datos_totales[0][0] = 'Temporada'

# Escribimos los datos en un archivo CSV
ruta_csv = '../data/semifinales.csv'
with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in datos_totales:
        escritor_csv.writerow(fila)

# Imprimimos un mensaje de éxito
print(f"El archivo CSV '{ruta_csv.split('/')[-1]}' ha sido creado exitosamente.")