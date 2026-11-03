from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello from Karim’s Dockerized Web App!</h1><p>Fachinformatiker Portfolio Project</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)