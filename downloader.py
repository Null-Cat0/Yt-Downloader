import re
from pytubefix import YouTube
from colorama import Fore, Style
from math import trunc

def is_valid_url(url):
    # Regular expression to check YouTube URL format
    pattern = r'(https?://)?(www\.)?(youtube)\.(com|be)/.+'
    # Check if the URL matches the pattern
    return re.match(pattern, url) is not None

def download_video(stream, folder):
    try:
        stream.download(folder)
        print(f"{Fore.GREEN}Download completed successfully.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during download: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    if is_valid_url(url):
        print(f"{Fore.GREEN}The URL is valid.{Style.RESET_ALL}")
        yt = YouTube(url)
        print(f"Title: {Fore.CYAN}{yt.title}{Style.RESET_ALL}")
        print(f"Creator: {Fore.CYAN}{yt.author}{Style.RESET_ALL}")

        for index, stream in enumerate(yt.streams):
            print(f"[{index}]\t File type: {stream.mime_type}")
            print(f"\t Audio codec: {stream.codecs}" if stream.includes_audio_track else f"\t Resolution: {stream.resolution}")
            print(f"\t File size: {trunc(stream.filesize / (1024*1024))} MB")
            print(f"\t Progressive: {stream.is_progressive}\n")

        stream_input = int(input("Select the stream to download: "))
        if stream_input >= 0 and stream_input < len(yt.streams):
            folder = input("Enter the folder: ")
            download_video(list(yt.streams)[stream_input], folder)
        else:
            print(f"{Fore.RED}No suitable streams found for download.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}The URL is not valid.{Style.RESET_ALL}")
