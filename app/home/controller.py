from flask import *
import os

home_bp = Blueprint('home', __name__)

# Route to serve the media files dynamically
@home_bp.route('/')
def index():
    return render_template('home.html')
