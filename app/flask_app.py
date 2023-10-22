from flask import Flask, render_template
import dash

app = Flask(__name__)

dash_app = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/dash/',
    external_stylesheets=['/static/css/styles.css']
)

@app.route('/')
def index():
    return render_template('index.html')
