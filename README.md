# UEFA Champions League

Este es el link del [repositorio](https://github.com/lauralardies/uefa_analisis).

## Objetivo

Mediante este proyecto buscamos analizar los datos de temporadas anteriores del campeonato de fútbol UEFA Champions League con el fin de hacer una predicción del ganador de la actual temporada 2023-24.

## Archivos

Todos los elementos de este repositorio se encuentran en la carpeta `UEFA`, que a su vez contiene:
- Carpeta `analisis`, donde realizamos el análisis de los datos. Hay dos archivos, uno en el que realizamos la limpieza y análisis de datos mientras que en el segundo archivo hacemos una regresión lineal, donde predecimos el número de goles.
- Carpeta `data` que contiene archivos CSV donde se guarda la información que usamos para analizar.
- Carpeta `scalers` que empleamos para guardar un archivo pickle que se genera al normalizar los datos para la regresión lineal.
- Carpeta `webscraping`, donde obtenemos los datos de temporadas anteriores del campeonato y los almacenamos en un CSV que guardamos en la carpeta `data`. Los datos los adquirimos haciendo web scraping de esta [web](https://fbref.com), una fuente para las estadísticas del fútbol.
- Archivo `requirements.txt` que nos indica cuales son las dependencias de Python necesarias para el correcto funcionamiento del proyecto.

## Ejecución

### Web Scraping

Para ejecutar los archivos de la carpeta `webscraping` debes ir accediendo a las carpetas donde se encuentra el archivo manualmente desde la terminal. Es decir, abres la terminar y ejecutas el siguiente comando que nos permite acceder dentro de la primera carpeta, UEFA.

```
cd UEFA
```

Seguidamente accedes a la carpeta webscraping, donde se encuentra el archivo que deseas ejecutar.

```
cd webscraping
```

Por último, una vez en la ruta correcta, ejecutamos el archivo de webscraping que queramos (`equipos.py`, `overall.py` o `partidos.py`.)

```
python archivo.py
```

### Análisis

Para ejecutar los archivos de la carpeta `analisis` simplemente le das al botón de ejecutar de la celda que quieras. Hay que tener en cuenta que puede pasar que al ejecutar una celda salga un mensaje de error por no haber ejecutado una celda anterior a ella.
