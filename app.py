from flask import render_template
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def blog():
    service = os.environ['ECS_SERVICE']
    message = "Hello, from App to Demo! Service is " + service
    return message



if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)