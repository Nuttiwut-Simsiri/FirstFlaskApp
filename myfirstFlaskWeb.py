from flask import Flask, request ,render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index_page():
    return render_template('index.html')
    