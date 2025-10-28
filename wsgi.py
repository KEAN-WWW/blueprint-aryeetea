# wsgi.py (at project root)
from application.app import init_app

app = init_app()

if __name__ == "__main__":
    app.run(debug="True")