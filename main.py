from flask import *

#inicialização do flask (instanciar o servidor flask)
app = Flask(__name__)

#criar uma função atrelada a rota (a ser quando a rota receber uma requisição)
#a função sempre precisa retonar algo (String, pagina html, etc)
@app.route("/")
def principal():
    titulo_pagina = "Gestão de Usuários"
    usuarios = [
        {"nome" : "Alex", "membro_ativo": True },
        {"nome" : "Pedrin", "membro_ativo": False}
    ]
    return render_template("index.html", titulo = titulo_pagina, lista_usuarios = usuarios)

#
@app.route("/rotaExtra", methods=['GET', 'POST', 'PUT'])
def pagina_extra():
    return """
        <p> Testando HTML</p>
        <h1>Testando</h1>
    """

#execução do servidor (chamar a função responsavel por executar o servidor web)
#colocar no modo servidor (recarregar o srvidor web automaticamente)
app.run(debug= True)