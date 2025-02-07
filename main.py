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

@app.route("/listarUsuarios")
def listarUsuarios():
    return render_template("listaUsuarios.html", lista = usuarios)

@app.route("/paginaRecuperarSenha")
def paginaAlterarSenha():
    return render_template("recuperarSenha.html")

@app.route("/recuperarSenha", methods=['POST'])
def verSenha():
    nome = request.form.get("nomeUsuario")
    email = request.form.get("emailUsuario")
    encontrado = False

    for usuario in usuarios:
        if(usuario[0] == nome and usuario[1] == email):
            encontrado = True
            senha = usuario[2]
    if(encontrado == True):
        mensagem = "Sua senha é: " + senha
        return render_template("recuperarSenha.html", mensagem=mensagem)
    else:
        mensagem = "Usuário não encontrado"
        return render_template("recuperarSenha.html", mensagem=mensagem)

@app.route("/paginaAlterarSenha")
def paginaAlterarSenha():
    return render_template("alterarSenha.html")
   
@app.route("/alterarSenha", methods=[POST])
def alterarSenha():
    nome = request.form.get("nomeUsuario")
    email = request.form.get("emailUsuario")
    novaSenha = str(request.form.get("novaSenha"))
    alterado = False
    global usuarios

    for usuario in usuarios:
        if(usuario[0] == nome and usuario[1] == email):
            alterado = True
            usuario[2] = novaSenha
    if(alterado == True):
        mensegem = "Sua senha foi alterada com sucesso!"
        return render_template("alterarSenha.html", mensagem=mensagem)
    else:
            mensegem = "Erro! Usuário não encontrado"
        return render_template("alterarSenha.html", mensagem=mensagem)

#execução do servidor (chamar a função responsavel por executar o servidor web)
#colocar no modo servidor (recarregar o srvidor web automaticamente)
app.run(debug= True)