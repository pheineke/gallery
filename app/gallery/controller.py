from flask import *
import os

gallery_bp = Blueprint('gallery', __name__)


# Define the folder that contains your media files
MEDIA_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'media')

# Route to serve the media files dynamically
@gallery_bp.route('/')
def index():
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