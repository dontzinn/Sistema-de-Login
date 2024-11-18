from Sistema import Sistema
from cadastro import Usuario

def __main__():
    sistema = Sistema()
    sistema.cadastrar_usuario('Pedro', '123pedro132',1)
    sistema.login('Pedro', '123pedro132')
    teste = sistema.cadastrar_usuario('Pedro', '123pedro132', 2)
    lista_usuarios = sistema.get_usuarios()
    print(lista_usuarios)

__main__()