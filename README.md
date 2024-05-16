# UEFA Champions League

Este es el link del [repositorio](https://github.com/lauralardies/uefa_analisis).

## Objetivo

Mediante este proyecto buscamos analizar los datos de temporadas anteriores del campeonato de fútbol UEFA Champions League con el fin de hacer una predicción del ganador de la actual temporada 2023-24.

## Archivos

Todos los elementos de este repositorio se encuentran en la carpeta `UEFA`, que a su vez contiene:
- Carpeta `analisis`, donde realizamos el análisis de los datos. Hay varios archivos, uno en el que realizamos la limpieza de los datos y otro donde analizamos los datos, creando visualizaciones para entenderlos mejor.
- Carpeta `data` que contiene archivos CSV donde se guarda la información que usamos para analizar. Además, una vez analizados los datos guardamos los datos limpios en esta carpeta.
- Carpeta `img` que almacena imágenes que usamos en nuestros modelos. Aquí encontramos 3 subcarpetas: `clasificaciones`, donde guardamos los resultados del torneo según haya predicho el modelo; `jugadores`, que guarda varias imágenes de jugadores de fútbol con el fin usarlas para entrenar redes neuronales; y por último `prueba`, donde podemos encontrar 4 imágenes que usaremos para evaluar las redes que entrenamos anteriormente con la carpeta que hemos mencionado antes.
- Carpeta `modelos` donde guardamos todos los modelos desarrollados para predecir el resultado del torneo. Estos modelos están clasificados en 4 subcarpetas: Aprendizaje no Supervisado, Aprendizaje por Refuerzo, Aprendizaje Profundo y Aprendizaje Supervisado.
- Carpeta `webscraping`, donde obtenemos los datos de temporadas anteriores del campeonato y los almacenamos en un CSV que guardamos en la carpeta `data`. Los datos los adquirimos haciendo web scraping de esta [web](https://fbref.com), una fuente para las estadísticas del fútbol.
- Archivo `requirements.txt` que nos indica cuales son las dependencias de Python necesarias para el correcto funcionamiento del proyecto.

## Ejecución

Para que funcionen correctamente todos los archivos de este repositorio, debes asegurarte primero que descargas todas las dependencias indicadas en el archivo `requirements.txt` en tu entorno.

### Web Scraping

Para ejecutar los archivos de la carpeta `webscraping` debes ir accediendo a las carpetas donde se encuentra el archivo manualmente desde la terminal. Es decir, abres la terminal y ejecutas el siguiente comando que nos permite acceder dentro de la primera carpeta, UEFA.

```
cd UEFA
```

Seguidamente accedes a la carpeta webscraping, donde se encuentra el archivo que deseas ejecutar.

```
cd webscraping
```

Por último, una vez en la ruta correcta, ejecutamos el archivo `main.py`, que nos abrirá un menú en la terminal donde nos dejará escoger sobré qué datos queremos hacer webscraping.

```
python main.py
```

### Análisis

Para ejecutar los archivos de la carpeta `analisis` simplemente le das al botón de ejecutar de la celda que quieras. Hay que tener en cuenta que puede pasar que al ejecutar una celda salga un mensaje de error por no haber ejecutado una celda anterior a ella.

### Modelos

Al igual que en la carpeta `analisis`, para ejecutar cualquier archivo de esta carpeta simplemente le das al botón de ejecutar de la celda que quieras. Hay que tener en cuenta que puede pasar que al ejecutar una celda salga un mensaje de error por no haber ejecutado una celda anterior a ella.

### Resultados

De todos los modelos que hemos desarrollado y evaluado en este repositorio, los que presentan un mejor rendimiento son el modelo SVC con una precisión del 62,3% y el modelo de regresión logística con un 60,49%. Veamos las predicciones que nos dan estos dos modelos:

![SVC](https://github.com/lauralardies/uefa_analisis/blob/main/UEFA/img/clasificaciones/LR, SVC.jpg?raw=true)

![LR](https://github.com/lauralardies/uefa_analisis/blob/main/UEFA/img/clasificaciones/LR, SVC.jpg?raw=true)

Observamos que ambos modelos predicen el mismo resultado final: Real Madrid como ganador de la UEFA Champions League. Como conclusión de nestro análisis, podemos decir que el ganador de esta temporada será el Real Madrid.
