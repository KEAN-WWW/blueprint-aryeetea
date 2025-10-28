# application/app.py
from flask import Flask
from .bp.homepage import homepage as homepage_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(homepage_bp, url_prefix="/")
    return app

# ✅ alias so tests (and wsgi.py) can import `init_app`
def init_app():
    return create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    