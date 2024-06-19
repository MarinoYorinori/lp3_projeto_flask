from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    { "nome": "Coca-cola", "descricao": "veneno", "preco": 4.40, "img": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpt.pngtree.com%2Ffree-water-png&psig=AOvVaw23-yLWu2SMm6a8j0SzDqe7&ust=1718915377438000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCJD0uvzA6IYDFQAAAAAdAAAAABAJ"},
    { "nome": "Doritos", "descricao": "suja mão", "preco": 1.47, "img": "static/img/Doritos.png" },
    { "nome": "Água", "descricao": "vida", "preco": 0.50, "img": "static/img/Água.png" },
    { "nome": "Miasma", "descricao": "foda", "preco": 200.00, "img": "static/img/Miasma.png" }
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

# GET, get é automatico do app.route
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

# method POST (recebe) - chamar o objeto request biblioteca
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome'] #nome ta linkado com o name do formulario no html
    descricao = request.form['descricao']
    preco = float(request.form['preco'])
    img = request.form['img']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "img": img}
    lista_produtos.append(produto) #append = função que adiciona no final da lista

    return redirect(url_for("produtos")) # importar funcao redirect e url_for na briblioteca