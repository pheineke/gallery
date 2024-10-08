from flask import *

def create_app():

    app = Flask(__name__, static_url_path='/static')
    
    app.config.update(
        TEMPLATE_AUTO_RELOAD = True
    )

    app.secret_key = 'your_secret_key'

    from app.home.controller import home_bp
    app.register_blueprint(home_bp, url_prefix='/')

    from app.scripts.controller import scripts_bp
    app.register_blueprint(scripts_bp, url_prefix='/scripts')

    from app.gallery.controller import gallery_bp
    app.register_blueprint(gallery_bp, url_prefix='/gallery')

    from app.gallery.controller_ import gallery__bp
    app.register_blueprint(gallery__bp, url_prefix='/gallery_')

    return app