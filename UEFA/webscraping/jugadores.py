import csv
import requests
from bs4 import BeautifulSoup

def webscraping_jugadores():
    '''
    Función que realiza web scraping de los datos de jugadores de la UEFA Champions League
    '''
    
    # URLs de diferentes temporadas de UEFA Champions League
    urls = [
        'https://fbref.com/en/comps/8/2023-2024/stats/2023-2024-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2022-2023/stats/2022-2023-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2021-2022/stats/2021-2022-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2020-2021/stats/2020-2021-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2019-2020/stats/2019-2020-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2018-2019/stats/2018-2019-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2017-2018/stats/2017-2018-Champions-League-Stats',
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

        # Buscamos la sección de texto que contiene la información de los jugadores
        html = soup.find('div',attrs={'data-label': 'Player Standard Stats'}).find_next('table', id='stats_standard')

        # Obtenemos las filas de la tabla
        filas = html.find_all('tr')
        # Eliminamos la primera fila que no nos interesa
        filas.pop(0)
        
        # Iteramos sobre las filas y obtenemos los datos de cada celda
        for fila in filas:
            # Obtenemos las celdas de la fila
            celdas = fila.find_all(['th', 'td'])
            # Extraemos el texto de cada celda y lo agregamos a la lista de datos
            datos_fila = [celda.get_text(strip=True) for celda in celdas]
            # Si la fila contiene datos, agregamos temporada y fila a la lista de datos totales
            if datos_fila:
                # Extraemos la termporada del URL directamente
                temporada = url.split('/')[-3]
                # Si la lista de datos totales está vacía, agregamos el encabezado de la tabla
                if len(datos_totales) == 0:
                    # Agregamos la temporada al encabezado
                    datos_fila.insert(0, 'Season')
                else:
                    if datos_fila[:19] == datos_totales[0][1:]:
                        # Si la fila ya está en la lista de datos totales, pasa a la siguiente fila
                        continue
                    else:
                        # Si la fila no coincide con la primera fila de datos totales, agregamos la temporada a la fila
                        datos_fila.insert(0, temporada)
                # Agregamos la fila a la lista de datos totales 
                # Solo añadimos los primeros 19 elementos de la lista (+ la temporada que ya hemos añadido), ya que el resto no nos interesa
                datos_totales.append(datos_fila[:20])

    # Escribimos los datos en un archivo CSV
    ruta_csv = '../data/jugadores.csv'
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for fila in datos_totales:
            escritor_csv.writerow(fila)

    # Imprimimos un mensaje de éxito
    print(f"El archivo CSV '{ruta_csv.split('/')[-1]}' ha sido creado exitosamente.")