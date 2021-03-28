
import Pyro4


# ns = Pyro4.locateNS()
# uri = ns.lookup('obj')

uri = "PYRO:obj_cdb7d330a64c43549f8d5747875d5f51@localhost:36943"

server = Pyro4.Proxy("PYRONAME:server")


user = {"name": "wagner",
        "email": "wagnerfelidre@gmail.com"
        }

print(server.createUser(user))

print(server.listOfUser())