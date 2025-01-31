from flask import *

#inicialização do flask (instanciar o servidor flask)
app = Flask(__name__)

usuarios = []

#criar uma função atrelada a rota (a ser quando a rota receber uma requisição)
#a função sempre precisa retonar algo (String, pagina html, etc)
@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/paginaCadastro")
def paginaCadastro():
    return render_template("cadastro.html")


@app.route("/cadastrarUsuario", methods=['GET', 'POST'])
def cadastrar():
    
    global usuarios
    nome = request.form.get("nomeUsuario")
    email = request.form.get("emailUsuario")
    senha = str(request.form.get("senhaUsuario"))
    usuarios.append([nome, email, senha])
    print(usuarios)
    mensagem = "Usuário cadastrado com sucesso"

    return render_template("index.html", mensagem = mensagem)

@app.route("/verificarLogin", methods=['POST'])
def login():

    global usuarios
    email = request.form.get("emailUsuario")
    senha = str(request.form.get("senhaUsuario"))
    logado = False
    
    for usuario in usuarios:
        if(usuario[1] == email and usuario[2] == senha):
            logado = True
    if(logado == True):
        return render_template("logado.html")
    else:
        mensagem = "Usuário ou senha incorretos"
        return render_template("index.html", mensagem = mensagem)
 
    


    return render_template("index.html")

@app.route("/paginaAlterarSenha", methods=['POST'])
def paginaAlterarSenha():
    return render_template("alterarSenha.html")

#execução do servidor (chamar a função responsavel por executar o servidor web)
#colocar no modo servidor (recarregar o srvidor web automaticamente)
app.run(debug= True)