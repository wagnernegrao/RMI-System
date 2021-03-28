import Pyro4


@Pyro4.expose
class Server(object):

    userList = []

    def createUser(self, user):
        
        self.userList.append(user)
    
        return "User created"

    def listOfUser(self):
        return self.userList






daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Server)
ns.register("server", uri)

print("Ready. Object uri =", uri)
daemon.requestLoop()
