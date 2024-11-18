from cadastro import Usuario
class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, username, password):
        for usuario in self.usuarios:
            if usuario.username == username:
                print('Já existe um cadastro com este username')
                return False
        usuario = Usuario(username, password, id)
        self.usuarios.append(usuario)
        print('Cadastro Criado com Sucesso')
        return True

    def login(self, username, password):
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                print("Bem-vindo ao python")
                return True
            print('Usuário não encontrado')