import mistune
from flask import Flask, jsonify, request, render_template
from validate import val_heart_rate, val_email, val_interval_average
from database import add_heart_rate, get_hr, get_avg_hr, get_int_avg

app = Flask(__name__, static_url_path='/static')


def handle_data(input, validator, action):
    """Handles API calls

    :param input: input data from request
    :param validator: validator function to use
    :param action: database function to apply to data
    :return: jsonified response
    """

    if(not validator(input)):
        message = '[ERROR] input was incorrectly formatted.'
        data = None
        code = 400
    else:
        (message, data, code) = action(input)

    res = {
        'message': message,
        'input': input
    }
    if(data):
        res['data'] = data
    return jsonify(res), code


@app.route('/', methods=['GET'])
def welcome():
    with open('README.md', 'r') as f:
        content = mistune.markdown(f.read())
        return render_template('index.html', content=content)


@app.route('/api/heart_rate', methods=['POST'])
def new_data():
    r = request.get_json()
    return handle_data(r, val_heart_rate, add_heart_rate)


@app.route('/api/heart_rate/<user_email>', methods=['GET'])
def user_data(user_email):
    return handle_data(user_email, val_email, get_hr)


@app.route('/api/heart_rate/average/<user_email>', methods=['GET'])
def average(user_email):
    return handle_data(user_email, val_email, get_avg_hr)


@app.route('/api/heart_rate/interval_average', methods=['POST'])
def interval_average():
    r = request.get_json()
    return handle_data(r, val_interval_average, get_int_avg)
