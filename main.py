import markdown
from flask import Flask, jsonify, request, render_template
from validate import val_heart_rate, val_email, val_interval_average

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def welcome():
    with open('README.md', 'r') as f:
        content = markdown.markdown(f.read())
        return render_template('index.html', content=content)


@app.route('/api/heart_rate', methods=['POST'])
def new_data():
    r = request.get_json()
    if(val_heart_rate(r)):
        res = {
            'message': 'ERROR: input was incorrectly formatted.',
            'input': r
        }
        return jsonify(res), 400

    

@app.route('/api/heart_rate/<user_email>', methods=['GET'])
def user_data(user_email):
    if(val_email(user_email)):
        res = {
            'message': 'ERROR: input was incorrectly formatted.',
            'input': user_email
        }
        return jsonify(res), 400
    

@app.route('/api/heart_rate/average/<user_email>', methods=['GET'])
def average(user_email):
    if(val_email(user_email)):
        res = {
            'message': 'ERROR: input email was incorrectly formatted.',
            'input': user_email
        }
        return jsonify(res), 400
    

@app.route('/api/heart_rate/interval_average', methods=['POST'])
def interval_average():
    r = request.get_json()
    if(val_interval_average(r)):
        res = {
            'message': 'ERROR: input data was incorrectly formatted.',
            'input': r
        }
        return jsonify(res), 400
