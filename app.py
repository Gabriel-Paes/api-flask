from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Bem-vindo a API Flask"})

@app.route("/send-data", methods=["POST"])
def get_data():
    data = request.get_json()
    return jsonify({"message": "Dados recebidos com sucesso", "data": data})

@app.route("/user/<name>", methods=["GET"])
def get_user(name):
    return jsonify({"message": f"Ola, {name}!"})

if __name__=='__main__':
    app.run(debug=True)