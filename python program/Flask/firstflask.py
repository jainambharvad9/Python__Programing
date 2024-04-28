from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi():
    return '<H1>Hi I Am Jainam Bharvad</h1>  '

if __name__ == '__main__':
    app.run(debug=True)