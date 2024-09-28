from flask import *
import os
import subprocess


from app.resources.wallpaper_downloader import WallpaperDownloader

scripts_bp = Blueprint('scripts', __name__)

@scripts_bp.route('/')
def index():
    return render_template('scripts.html', logs="No current logs")

@scripts_bp.route('/start-pc', methods=['POST'])
def run_script():
    if request.method == 'POST':
        try:
            #Führe das Bash-Skript aus
            result = subprocess.run(['bash', './scripts/pc-start.sh'], capture_output=True, text=True)
            #return f"Script executed successfully: {result.stdout}"
            return render_template('scripts.html', logs=f"Script executed successfully: {result.stdout}")

        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"
