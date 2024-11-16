class Usuario:
    def __init__(self, username, password, id):
        self.username = username
        self.password = password
        self.id = id

    def set_password(self, password):
        self.password = password
        return self

    def get_username(self):
        return self.username


