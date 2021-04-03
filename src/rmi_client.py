import time
from Pyro4 import Proxy
from time_execution import TimeExecution

# Segura as funcionalidades com as quais interagimos pelo terminal
class RMIClient:
    def __init__(self, server_proxy: Proxy):
        self.server = server_proxy
        self.times = TimeExecution()

    # 1. Listar todas as pessoas formadas em um determinado curso
    def list_users_by_course(self, curso):
        t0 = time.time()
        users = self.server.findByGraduation(curso) 
        t1 = time.time()
        self.times.timeFindByGraduation(t0, t1)

        for user in users:
            print('-'*50)
            print(user)
        print('-'*50)
        print(f'{t1-t0} segundos')

    # 2. Listar as habilidades dos perfis que moram em uma determinada cidade
    def list_abilities_by_city(self, cidade):
        t0 = time.time()
        users = self.server.findByAbilities(cidade)
        t1 = time.time()
        self.times.timeFindByAbilities(t0, t1)
        
        for user in users:
            print('-'*50)
            print(f"Nome: {user['Nome']}")
            print(f"Habilidades: {user['Habilidade']}")
        print('-'*50)
        print(f'{t1-t0} segundos')

    # 3. Acrescentar uma nova experiência em um perfil
    def add_experience(self, email, experiencia):
        t0 = time.time()
        result = self.server.modifyAbilitie(email, experiencia)
        t1 = time.time()
        self.times.timeModifyAbilitie(t0, t1)
        print(result)
        print(f'{t1-t0} segundos')

    # 4. Dado o email do perfil, retornar sua experiência
    def experience_by_email(self, email):
        t0 = time.time()
        exp = self.server.findByExperience(email)
        t1 = time.time()
        self.times.timeFindByExperience(t0, t1)
        print(exp)
        print(f'{t1-t0} segundos')

    # 5. Listar todas as informações de todos os perfis
    def list_all_userinfo(self):
        t0 = time.time()
        users = self.server.listAllUsers()
        t1 = time.time()
        self.times.timeListAllUsers(t0, t1)

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
        print(f'{t1-t0} segundos')

    # 6. Dado o email de um perfil, retornar suas informações
    def user_by_email(self, email):
        t0 = time.time()
        user = self.server.findByEmail(email)
        t1 = time.time()
        self.times.timeFindByEmail(t0, t1)

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
        print(f'{t1-t0} segundos')

