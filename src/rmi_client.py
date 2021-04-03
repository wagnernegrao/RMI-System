from Pyro4 import Proxy

# Segura as funcionalidades com as quais interagimos pelo terminal
class RMIClient:
    def __init__(self, server_proxy: Proxy):
        self.server = server_proxy 

    # 1. Listar todas as pessoas formadas em um determinado curso
    def list_users_by_course(self, curso):
        users = self.server.findByGraduation(curso) 
        for user in users:
            print('-'*50)
            print(user)
        print('-'*50)

    # 2. Listar as habilidades dos perfis que moram em uma determinada cidade
    def list_abilities_by_city(self, cidade):
        users = self.server.findByAbilities(cidade)
        
        for user in users:
            print('-'*50)
            print(f"Nome: {user['Nome']}")
            print(f"Habilidades: {user['Habilidade']}")
        print('-'*50)

    # 3. Acrescentar uma nova experiência em um perfil
    def add_experience(self, email, experiencia):
        result = self.server.modifyAbilitie(email, experiencia)
        print(result)

    # 4. Dado o email do perfil, retornar sua experiência
    def experience_by_email(self, email):
        exp = self.server.findByExperience(email)
        print(exp)

    # 5. Listar todas as informações de todos os perfis
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

    # 6. Dado o email de um perfil, retornar suas informações
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

