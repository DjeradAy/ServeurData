from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index2.html")

@app.route('/login', methods=["GET","POST"])
def search() :
    nom = request.form.get('username')
    return f'Nom : {nom}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)