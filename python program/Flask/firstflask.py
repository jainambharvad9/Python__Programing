from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi():
    return ' Jay Shree'

if __name__ == '__main__':
    app.run()