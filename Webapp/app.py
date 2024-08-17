from flask import Flask, render_template, request
from downloader import Downloader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def process_data():
    youtube_url = request.form.get('youtubeUrl')
    folder = request.form.get('folder')

    download = Downloader(youtube_url, folder)
    download.main()

    return render_template('result.html', title="Video Downloaded", creator="", description="")

if __name__ == '__main__':
    app.run(debug=True)
