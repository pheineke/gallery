import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Define the folder that contains your media files
MEDIA_FOLDER = os.path.join(os.getcwd(), 'static', 'media')

# Route to serve the media files dynamically
@app.route('/')
def index():
    # Get a list of files in the media folder
    media_files = []
    for file_name in os.listdir(MEDIA_FOLDER):
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.webm')):
            media_files.append(file_name)
    return render_template('gallery.html', media_files=media_files)

# Serve media files dynamically
@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
