import yt_dlp
class Downloader:
    
    def __init__(self, url, folder):
        self.url = url
        self.folder = folder

    def main(self):
        ydl_opts = {
            'outtmpl': f'{self.folder}/%(title)s.%(ext)s',
            'format': 'best',  # Choose the best quality available
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])