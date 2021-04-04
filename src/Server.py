import Pyro4


@Pyro4.expose # expoem a classe de forma global
class Server(object):

    userList = []

    # 1
    def createUser(self, user):
        self.userList.append(user)
        return "Usuario criado"

    # 2 listar todas as pessoas formadas em um determinado curso
    def findByGraduation(self, graduation):
        graduates = []
        for user in self.userList:
            if (user["formacao_academica"] == graduation):
                graduates.append(user["nome"])
        return graduates

    # 3  listar as habilidades dos perfis que moram em uma determinada cidade
    def findByAbilities(self, cidade):
        abilities = []
        for user in self.userList:
            if (user["residencia"] == cidade):
                abilities.append({"Nome": user["nome"], "Habilidade": user["habilidades"]})
        return abilities

    # 4 acrescentar uma nova experiência em um perfil
    def modifyAbilitie(self, email, newAbilitie):
        for user in self.userList:
            if (user["email"] == email):
                user["experiencia_profissional"] = user["experiencia_profissional"] + ", " + newAbilitie
                return "Nova experiencia profissional adicionada: " + user["experiencia_profissional"]
            
            return "Usuario com esse email nao foi encontrado"

    # 5 dado o email do perfil, retornar sua experiência
    def findByExperience(self, email):
        for user in self.userList:
            if (user["email"] == email):
                return "Habilidades: " + user["habilidades"]
        return "Usuario com esse email nao foi encontrado"

    # 6 listar todas as informações de todos os perfis
    def listAllUsers(self):
        return self.userList

    # 7. Dado o email de um perfil, retornar suas informações
    def findByEmail(self, email):
        for user in self.userList:
            if (user["email"] == email):
                return user
        return "Esse email não corresponde a nehum usuário"

if __name__ == '__main__':
    # daemon = Pyro4.Daemon(host="server", port=9100) # inicia o processo usando docker
    # ns = Pyro4.locateNS(host="pyro-ns", port=9090) # Inicia o processo local usando docker
    daemon = Pyro4.Daemon() # inicia o processo
    ns = Pyro4.locateNS() # Inicia o processo local
    uri = daemon.register(Server) # Registra o processo
    ns.register("server", uri) # Cria um alias para o processo registrado
    print('Ready. URI =', uri)
    print("Abrindo processo para chamadas")

    daemon.requestLoop() # Deixa o processo aberto para chamadas
   