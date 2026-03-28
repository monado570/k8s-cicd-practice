import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://backend-service:5001/api')
    return f'Frontend received: {response.text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
