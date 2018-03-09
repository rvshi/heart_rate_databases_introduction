import markdown
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def welcome():
    with open('README.md', 'r') as f:
        content = markdown.markdown(f.read())
        return render_template('index.html', content=content)

