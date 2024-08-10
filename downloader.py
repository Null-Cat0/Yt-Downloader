import re
from time import time
from pytubefix import YouTube
from colorama import Fore, Style


def es_url_valida(url):
    # Expresión regular para verificar el formato de la URL de YouTube
    patron = r' ?(https?://)?(www\.)?(youtube)\.(com)/.+'
    # Comprobar si la URL coincide con el patrón
    if re.match(patron, url):
        return True
    else:
        return False

def descargar_video(stream,folder):
    try:
        stream.download(folder)
        print(f"{Fore.GREEN}Descarga completada exitosamente.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error durante la descarga: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    print("--Descargador de videos de youtube--")
    url = input("Introduzca la url del video a descargar (ejemplo: https://www.youtube.com/watch?v=XXXXXXXXXXX):")

    if es_url_valida(url):
        print(f"{Fore.GREEN}La URL es válida.{Style.RESET_ALL}")
        yt = YouTube(url)
        print(f"Titulo: {Fore.CYAN}{yt.title}{Style.RESET_ALL}")
        print(f"Creador/a: {Fore.CYAN}{yt.author}{Style.RESET_ALL}")
        streams = yt.streams.filter(file_extension="mp4", progressive=True)
        
        # Seleccionar el primer stream disponible
        stream = streams.first()
        if stream:
            print(f"Resolución: {stream.resolution}")
            print(f"Tipo de archivo: {stream.mime_type}")
            print(f"Tamaño del archivo: {stream.filesize} bytes")             
            folder = input("Donde quieres almacenar el video: ")
            
            time_initial = time()
            descargar_video(stream,folder)
            time_finish = time()
            total_time = time_finish - time_initial
            print(f"Tiempo tardado: {total_time}s")
        else:
            print(f"{Fore.RED}No se encontraron streams adecuados para descargar.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}La URL no es válida.{Style.RESET_ALL}")
