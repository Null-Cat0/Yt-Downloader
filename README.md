
# Yt-Downloader

## Descripción

Yt-Downloader es una herramienta de línea de comandos diseñada para facilitar la descarga de videos de YouTube. Este programa emplea la biblioteca `pytubefix` para realizar las descargas y utiliza `colorama` para mejorar la experiencia del usuario en la terminal mediante la adición de colores al texto.

## Dependencias

Para asegurar el correcto funcionamiento de Yt-Downloader, es necesario instalar las siguientes dependencias de Python:

1. **colorama**: Esta biblioteca se utiliza para permitir la impresión de texto en color en la consola, mejorando así la legibilidad y la presentación de la información.
   ```bash
   python -m pip install colorama
   ```

2. **pytubefix**: Esta biblioteca se utiliza para gestionar la descarga de videos de YouTube. `pytubefix` es una versión modificada de `pytube` que corrige un error presente en `pytube` relacionado con cambios recientes en la API de YouTube.
   ```bash
   python -m pip install pytubefix
   ```

## Instalación

Para instalar Yt-Downloader, siga estos pasos:

1. Clone este repositorio en su máquina local o descargue el código fuente directamente desde la página del proyecto.
2. Navegue al directorio del proyecto utilizando su terminal o línea de comandos preferida.

## Uso

Para utilizar Yt-Downloader, ejecute el script principal como se indica a continuación:

```bash
python downloader.py
```

El programa le solicitará que ingrese la URL del video de YouTube que desea descargar. Siga las instrucciones que aparecen en pantalla para completar el proceso de descarga.

## Notas

- **Requisito de Python:** Asegúrese de que Python esté correctamente instalado en su sistema. Puede verificarlo ejecutando `python --version` en la terminal.
- **Verificación de dependencias:** Antes de ejecutar el script, verifique que todas las dependencias necesarias estén correctamente instaladas utilizando `pip list` para confirmar su presencia.
