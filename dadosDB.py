import sqlite3 as sqlite

def criar_tabela():
    conn = sqlite.connect('dadosDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

criar_tabela()

def inserir(nome, email, senha):
    conn = sqlite.connect('dadosDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)
    """, (nome, email, senha))
    conn.commit()
    conn.close()

def listar():
    conn = sqlite.connect('dadosDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios order by id desc')
    dadosDB = cursor.fetchall()
    usuarios= []

    for dados in dadosDB:
        usuarios.append(dados)

    conn.close()
    return usuarios

