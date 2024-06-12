from flask import Flask, render_template

lista_produtos = [
    { "nome": "Coca-cola", "descricao": "veneno" },
    { "nome": "Doritos", "descricao": "suja mão" },
    { "nome": "Água", "descricao": "vida" },
    { "nome": "Miasma", "descricao": "foda" }
]

app = Flask(__name__)
# cria aplicação na memória que responde na porta 5000

# Quando receber um requerimento com "/", executa a seguinte função:  (basicamente o comando que o usuario executa e o que ele retorna)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)
# PARA ACESSAR PAG HTML, é necessario usar a função importada render_template 
# ele busca o arquivo em uma pasta de nome "templates" (precisa ser criada manualmente)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)
    return 'Produto não existe!!!!!!'