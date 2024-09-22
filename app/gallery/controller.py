from flask import *
import os

import flask

from app.resources.wallpaper_downloader import WallpaperDownloader

gallery_bp = Blueprint('gallery', __name__)

downloader = WallpaperDownloader('https://wallhaven.cc/hot')


# Define the folder that contains your media files
MEDIA_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'media', 'wallpapers')

# Route to serve the media files dynamically
@gallery_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            number = int(request.form['quantity'])  # Extrahiere den Wert für "quantity" und wandle ihn in eine Zahl um
            print(number)
            downloader.download_wallpapers(num_wallpapers=number)
            return jsonify({"status": "ok", "message": "Wallpapers downloaded successfully!"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500


    # Get a list of files in the media folder
    media_files = []
    for file_name in os.listdir(MEDIA_FOLDER):
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.webm')):
            media_files.append(file_name)
    return render_template('gallery.html', media_files=media_files)

# Serve media files dynamically
@gallery_bp.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

@gallery_bp.route('/download_wallpapers/<int:number>')
def download_wallpapers(number: int):
    try:
        downloader.download_wallpapers(num_wallpapers=number)
        return jsonify({"status": "ok", "message": "Wallpapers downloaded successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500