from flask import *
import os
import time

gallery__bp = Blueprint('gallery_', __name__)


# Define the folder that contains your media files
#MEDIA_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'media', 'p')
MEDIA_FOLDER = '/run/media/dreamer/111D11EB2FA37324/NewFolder/'
cache_timeout = 3600  # Cache timeout in seconds

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
def index():
    media_files = get_media_files()
    return render_template('gallery_.html', media_files=media_files)

# Serve media files dynamically
@gallery__bp.route('/media/p/<path:filename>')
def media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)