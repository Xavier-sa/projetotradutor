import os
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


@app.route('/listar')
def listar():
    palavras = modelo.listar_palavras()  # Pega as palavras corretamente do modelo
    
    if palavras == []:
        palavras = []  # Se não houver palavras, passamos uma lista vazia
    
    return render_template('listar.html', palavras=palavras)



@app.route("/excluir", methods=["GET", "POST"])
def excluir():
    mensagem = ""
    if request.method == "POST":
        palavra_ingles = request.form["palavra_ingles"]
        sucesso = modelo.excluir_palavra(palavra_ingles)
        mensagem = f"Palavra '{palavra_ingles}' excluída com sucesso!" if sucesso else "Essa palavra não foi encontrada."
    return render_template("excluir.html", mensagem=mensagem)




if __name__ == "__main__":
    # Usar a variável de ambiente PORT, que o Render define automaticamente
    port = int(os.environ.get("PORT", 5000))  # 5000 é o valor padrão se não encontrar a variável
    app.run(debug=True, host="0.0.0.0", port=port)
