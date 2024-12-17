from flask import Flask, render_template, request
from models.model import DicionarioModel

app = Flask(__name__)
modelo = DicionarioModel()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    mensagem = ""
    if request.method == "POST":
        palavra_ingles = request.form["palavra_ingles"]
        traducao_portugues = request.form["traducao_portugues"]
        sucesso = modelo.adicionar_palavra(palavra_ingles, traducao_portugues)
        mensagem = f"Palavra '{palavra_ingles}' adicionada com sucesso!" if sucesso else "Essa palavra já existe."
    return render_template("adicionar.html", mensagem=mensagem)

@app.route("/procurar", methods=["GET", "POST"])
def procurar():
    resultado = ""
    if request.method == "POST":
        busca = request.form["busca"]
        resultado = modelo.procurar_palavra(busca)
    return render_template("procurar.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
