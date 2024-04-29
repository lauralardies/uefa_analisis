from equipos import webscraping_equipos
from jugadores import webscraping_jugadores
from partidos import webscraping_partidos
from overall import webscraping_overall
from helpers import limpiar_pantalla

if __name__ == '__main__':
    while True:
        limpiar_pantalla()
        print('¡Bienvenido a la aplicación de web scraping de la UEFA Champions League!\n')

        print('Seleccione una opción:')
        print('1. Realizar web scraping de equipos')
        print('2. Realizar web scraping de jugadores')
        print('3. Realizar web scraping de partidos')
        print('4. Realizar web scraping de datos generales')
        print('5. Realizar web scraping de todos los datos')
        print('6. Salir')
        opcion = input('\nOpción: ')
        limpiar_pantalla()

        if opcion == '1':
            print('Iniciando web scraping de equipos...\n')
            webscraping_equipos()
        elif opcion == '2':
            print('Iniciando web scraping de jugadores...\n')
            webscraping_jugadores()
        elif opcion == '3':
            print('Iniciando web scraping de partidos...\n')
            webscraping_partidos()
        elif opcion == '4':
            print('Iniciando web scraping de datos generales...\n')
            webscraping_overall()
        elif opcion == '5':
            print('Iniciando web scraping de todos los datos...\n')
            webscraping_equipos()
            webscraping_jugadores()
            webscraping_partidos()
            webscraping_overall()
        elif opcion == '6':
            print('Saliendo...')
            break
        else:
            print('Opción no válida. Intente de nuevo.')

        input('\nPresione Enter para continuar...')