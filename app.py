from flask import Flask, render_template, request
from pytube import YouTube
import ssl

app = Flask(__name__)
ssl._create_default_https_context = ssl._create_unverified_context

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['videoUrl']
    save_directory = request.form['saveDirectory']
    result = download_video(video_url, save_directory)
    return render_template('result.html', result=result)

def download_video(video_url, save_directory):
    try:
        yt = YouTube(video_url)
        highest_resolution = yt.streams.get_highest_resolution().download(save_directory)
        return {"status": "success", "message": "Downloaded Successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    app.run(debug=True)
