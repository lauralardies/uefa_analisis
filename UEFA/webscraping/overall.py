import csv
import requests
from bs4 import BeautifulSoup

def webscraping_overall():
    '''
    Función que realiza web scraping de los datos generales de la UEFA Champions League
    '''
    
    # URLs de diferentes temporadas de UEFA Champions League
    urls = [
        'https://fbref.com/en/comps/8/2023-2024/2023-2024-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2022-2023/2022-2023-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2021-2022/2021-2022-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2020-2021/2020-2021-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2019-2020/2019-2020-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2018-2019/2018-2019-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2017-2018/2017-2018-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2016-2017/2016-2017-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2015-2016/2015-2016-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2014-2015/2014-2015-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2013-2014/2013-2014-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2012-2013/2012-2013-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2011-2012/2011-2012-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2010-2011/2010-2011-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2009-2010/2009-2010-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2008-2009/2008-2009-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2007-2008/2007-2008-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2006-2007/2006-2007-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2005-2006/2005-2006-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2004-2005/2004-2005-Champions-League-Stats',
        'https://fbref.com/en/comps/8/2003-2004/2003-2004-Champions-League-Stats',
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

        # Buscamos la sección de texto que contiene la información general del torneo
        html = soup.find('span', attrs={'data-label': 'League Table'}).find_next('table', id=lambda x: x and 'overall' in x)
        
        # Obtenemos las filas de la tabla
        filas = html.find_all('tr')

        # Iteramos sobre las filas y obtenemos los datos de cada celda
        for fila in filas:
            # Obtenemos las celdas de la fila
            celdas = fila.find_all(['th', 'td'])
            # Eliminamos las celdas que contienen 'xg' y que son 'last_5' en el atributo 'data-stat' ya que no están en todas las temporadas
            celdas = [celda for celda in celdas if 'xg' not in celda.get('data-stat') and celda.get('data-stat') != 'last_5']
            # Extraemos el texto de cada celda y lo agregamos a la lista de datos
            datos_fila = [celda.get_text(strip=True) for celda in celdas]
            # Si la fila contiene datos, agregamos temporada y fila a la lista de datos totales
            if datos_fila:
                # Extraemos la termporada del URL directamente
                temporada = url.split('/')[-2]
                # Si la lista de datos totales está vacía, agregamos el encabezado de la tabla
                if len(datos_totales) == 0:
                    # Agregamos la temporada al encabezado
                    datos_fila.insert(0, 'Season')
                else:
                    if datos_fila == datos_totales[0][1:]:
                        # Si la fila ya está en la lista de datos totales, pasa a la siguiente fila
                        continue
                    else:
                        # Si la fila no coincide con la primera fila de datos totales, agregamos la temporada a la fila
                        datos_fila.insert(0, temporada)
                # Agregamos la fila a la lista de datos totales 
                datos_totales.append(datos_fila)

    # Escribimos los datos en un archivo CSV
    ruta_csv = '../data/overall.csv'
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for fila in datos_totales:
            escritor_csv.writerow(fila)

    # Imprimimos un mensaje de éxito
    print(f"El archivo CSV '{ruta_csv.split('/')[-1]}' ha sido creado exitosamente.")