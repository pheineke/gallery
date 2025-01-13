from flask import *
import os
import time

gallery__bp = Blueprint('gallery_', __name__)


# Define the folder that contains your media files
#MEDIA_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'media', 'p')
MEDIA_FOLDER = '/DATA/gallery_'
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
    # Get query parameters for pagination
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)

    media_files = get_media_files()

    # Calculate start and end indices for the current page
    start = (page - 1) * per_page
    end = start + per_page

    # Get the media files for the current page
    paginated_media = media_files[start:end]

    # Determine if there are more pages
    total_pages = (len(media_files) + per_page - 1) // per_page

    return render_template(
        'gallery_.html',
        media_files=paginated_media,
        page=page,
        total_pages=total_pages,
        per_page=per_page
    )

# Serve media files dynamically
@gallery__bp.route('/media/p/<path:filename>')
def media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)
