from Pyro4 import Proxy

# Segura as funcionalidades com as quais interagimos pelo terminal
class ClientApp:
    def __init__(self, server_proxy: Proxy):
        self.server = server_proxy

    # Mantém a captação da entrada em um loop até que seja dada uma entrada
    # válida
    @staticmethod
    def get_command_code():
        while True:
            try:
                n = int(input('Comando: '))
                if not 1 <= n <= 6:
                    raise ValueError()
                break
            except ValueError:
                print('Valor invalido!')
                pass
        return n

    # Obtém todas as informações de usuários do servidor e lista no console
    def list_all_userinfo(self):
        users = self.server.listAllUsers()
        for user in users:
            print('-'*50)
            print(f'Nome: {user["nome"]}')
            print(f'Sobrenome: {user["sobrenome"]}')
            print(f'E-mail: {user["email"]}')
            print(f'Residência: {user["residencia"]}')
            print(f'Formação Acadêmica: {user["formacao_academica"]}')
            print(f'Habilidades: {user["habilidades"]}')
            print(f'Experiência Profissional: {user["experiencia_profissional"]}')
        print('-'*50)

    # Lista as informacoes de usuario com um dado email
    def user_by_email(self, email):
        user = self.server.findByEmail(email)
        if isinstance(user, str):
            print(user)
            return
        print(f'Nome: {user["nome"]}')
        print(f'Sobrenome: {user["sobrenome"]}')
        print(f'Residência: {user["residencia"]}')
        print(f'Formação Acadêmica: {user["formacao_academica"]}')
        print(f'Habilidades: {user["habilidades"]}')
        print(f'Experiência Profissional: {user["experiencia_profissional"]}')
        print('-'*50)

