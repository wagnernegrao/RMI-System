import Pyro4


@Pyro4.expose # expoem a classe de forma global
class Server(object):

    userList = []

    def createUser(self, user):
        self.userList.append(user)
        return "User created"

    def listOfUser(self):
        return self.userList
    
    def findByGraduation(self, graduation):
        graduates = []

        for user in self.userList:
            if (user["formacao_academica"] == graduation):
                graduates.append(user["nome"])
    
        return graduates

    def findByAbilities(self, abilitie):
        abilities = []

        for user in self.userList:
            if (user["habilidades"] == abilitie):
                abilities.append({"Nome": user["nome"], "Habilidade": user["habilidades"]})
    
        return abilities

    # 5. listar todas as informações de todos os perfis
    def listAllUsers(self):
        return self.userList


daemon = Pyro4.Daemon() # inicia o processo
ns = Pyro4.locateNS() # Inicia o processo local
uri = daemon.register(Server) # Registra o processo
ns.register("server", uri) # Cria um alias para o processo registrado

daemon.requestLoop() # Deixa o processo aberto para chamadas
