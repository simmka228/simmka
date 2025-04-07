from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first_flour')
def first_flour():
    return render_template('first_flour.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

@app.route('/cabinets/<filename>')
def cabinets(filename):
    return send_from_directory('static/cabinets', filename)

if __name__ == '__main__':
    app.run(debug=True)