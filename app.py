from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!', 200


@app.route('/<name>')
def hello_name(name):
    return f'Hello {name}!', 200


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')
