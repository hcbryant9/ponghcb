import os
import random
from flask import Flask, jsonify, request 
from flask_httpauth import HTTPDigestAuth as FlaskDigestAuth

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = FlaskDigestAuth()
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
tester = random.randint(1,10)

users = {
    "vcu":"rams"
    }

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class ValidationError(ValueError):
    pass

@app.route('/users', methods=['GET'])
@auth.login_required
def index():
   return jsonify(tester),201


