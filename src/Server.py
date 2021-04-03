import Pyro4


@Pyro4.expose # expoem a classe de forma global
class Server(object):

    userList = []

    def createUser(self, user):
        self.userList.append(user)
        return "User created"

    def listOfUser(self):
        return self.userList



daemon = Pyro4.Daemon(host="server", port=9100) # inicia o processo
ns = Pyro4.locateNS(host="pyro-ns", port=9090) # Inicia o processo local
uri = daemon.register(Server) # Registra o processo
ns.register("server", uri) # Cria um alias para o processo registrado

# print("Ready. Object uri =", uri)
print("Abrindo processo para chamadas")
daemon.requestLoop() # Deixa o processo aberto para chamadas
