from flask import Flask, render_template, request, redirect, url_for

def obter_produtos():
    lista_produtos = []
    with open("produtos.csv", "r") as file:
        linhas = file.readlines()
        for linha in linhas:
            print(linha.strip().split(","))
            nome, descricao, valor, img = linha.strip().split(",")
            produto = {
                "nome": nome,
                "descricao": descricao,
                "valor": valor,
                "img_url": img
            }
            lista_produtos.append(produto)
        
        return lista_produtos
    
def adicionar_produto(produto):
    with open("produtos.csv", "a") as file:
        linha = f"\n{produto['nome']},{produto['descricao']},{produto['valor']},{produto['img_url']}"
        file.write(linha)

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
    return render_template("produtos.html", produtos=obter_produtos())
# PARA ACESSAR PAG HTML, é necessario usar a função importada render_template 
# ele busca o arquivo em uma pasta de nome "templates" (precisa ser criada manualmente)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)
    return 'Produto não existe!!!!!!'

# GET, get é automatico do app.route salvar_produto():
    nome = request.f
    return render_template("cadastro_produto.html")

# method POST (recebe) - chamar o objeto request biblioteca
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome'] #nome ta linkado com o name do formulario no html
    descricao = request.form['descricao']
    preco = float(request.form['preco'])
    img = request.form['img']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "img": img}
    adicionar_produto(produto)

    return redirect(url_for("produtos")) # importar funcao redirect e url_for na briblioteca

if __name__ == "__main__":
    app.run(port=5001)