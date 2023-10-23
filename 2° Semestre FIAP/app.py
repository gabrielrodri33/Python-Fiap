from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/') #Acrescentando um endpoint
def index():
    return 'Hello'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/status/')
def get_status():
    return {"Status" : "OK"}

@app.route('/status_/')
def get_json():
    return jsonify({"Status" : "OK"}) #caso precise transformar algo em json para passar use jsonify

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return f'A soma de {n1} com {n2} é {n1+n2}'

@app.route('/rev/<float:revNo>')
def revision(revNo):
    #return 'Revision No %f' %revNo
    return f'Revision No {revNo}'

#Programa principal
if __name__ == "__main__":
    app.run()