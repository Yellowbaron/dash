from app.flask_app import app as flask_app
from app\dash_app.py import app as dash_app

if __name__ == "__main__":
    flask_app.run(debug=True)
