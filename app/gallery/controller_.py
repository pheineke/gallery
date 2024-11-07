from flask import *
import os
import time

gallery__bp = Blueprint('gallery_', __name__)


# Define the folder that contains your media files
#MEDIA_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'media', 'p')
MEDIA_FOLDER = '/DATA/gallery_'
cache_timeout = 3600  # Cache timeout in seconds

def get_media_items(path=""):
    full_path = os.path.join(MEDIA_FOLDER, path)
    items = []
    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)
        if os.path.isdir(item_path):  # Check if it's a directory
            items.append({"name": item, "is_folder": True})
        elif item.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.webm')):
            items.append({"name": item, "is_folder": False})
    return items

def get_media_files():
    if 'media_files' in session and time.time() - session['timestamp'] < cache_timeout:
        return session['media_files']
    
    media_files = [
        file_name for file_name in os.listdir(MEDIA_FOLDER)
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.webm'))
    ]
    
    session['media_files'] = media_files
    session['timestamp'] = time.time()
    return media_files

# Route to serve the media files dynamically
@gallery__bp.route('/')
@gallery__bp.route('/<path:folder_path>')
def index(folder_path=""):
    media_items = get_media_items(folder_path)
    return render_template('gallery_.html', media_files=media_items, folder_path=folder_path)

@gallery__bp.route('/media/p/<path:filepath>')
def media(filepath):
    return send_from_directory(MEDIA_FOLDER, filepath)
