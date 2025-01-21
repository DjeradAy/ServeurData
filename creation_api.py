from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=("GET","POST"))
def index() : 
    return render_template("index.html")

@app.route('/qui-suis-je', methods=("GET","POST"))
def getName() : 
    return 'Aymen DJERAD'


if __name__ == '__main__':
    app.run(host='0.0.0.0')    