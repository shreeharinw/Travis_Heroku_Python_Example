from flask import Flask
app = Flask(__name__)

@app.route('/<msg>')
def hello_world(msg):
    return 'Hello, World!'+msg

if __name__ == '__main__':
    app.run()