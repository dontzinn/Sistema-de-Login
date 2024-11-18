from Sistema import Sistema
from cadastro import Usuario
from database import conecta, encerrar_conexao

def __main__(): 
    # Conexão com o banco de dados
    connection = conecta()
    cursor = connection.cursor()
    
    def inserir_usuario(username, password):
        cmd_insert = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        values = username, password
        cursor.execute(cmd_insert, values)
        connection.commit()
        print("Dados inseridos com sucesso!!")
    
    print("Seja bem-vindo")
    print("Para estar cadastrando, coloque seu username e senha")
    username = input("Username: ")
    password = input("Password: ")
    inserir_usuario(username, password)
    
    
    # sistema = Sistema()
    # sistema.cadastrar_usuario('Pedro', '123pedro132',1)
    # sistema.login('Pedro', '123pedro132')
    # teste = sistema.cadastrar_usuario('Pedro', '123pedro132', 2)
    # lista_usuarios = sistema.get_usuarios()
    # print(lista_usuarios)

__main__()