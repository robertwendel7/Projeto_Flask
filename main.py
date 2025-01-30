from flask import *

#inicialização do flask (instanciar o servidor flask)
app = Flask(__name__)

#criar uma função atrelada a rota (a ser quando a rota receber uma requisição)
#a função sempre precisa retonar algo (String, pagina html, etc)
@app.route("/")
def principal():
    return render_template("cadastro.html")



usuarios = []
@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    
    global usuarios
    nome = request.form.get("nomeUsuario")
    email = request.form.get("emailUsuario")
    senha = request.form.get("senhaUsuario")
    usuarios.append([nome, email, senha])
    print(usuarios)

    return render_template("login.html")

@app.route("/verificarLogin", methods=['GET', 'POST'])
def login():
    titulo_pagina = "Login de Usuários"
    global usuarios
    nome = request.form.get("nomeUsuario")
    email = request.form.get("emailUsuario")
    senha = request.form.get("senhaUsuario")

    for i in usuarios :
        if(i.nome == nome and i.email == email and i.senha == senha):
            mensagem = "Login com sucesso!"
            return render_template("login.html", mensagem)
        else:
            mensagem = "Esse usuário nao está cadastrado ;-;"
            return render_template("login.html", mensagem)


    return render_template("login.html", titulo = titulo_pagina)

#execução do servidor (chamar a função responsavel por executar o servidor web)
#colocar no modo servidor (recarregar o srvidor web automaticamente)
app.run(debug= True)