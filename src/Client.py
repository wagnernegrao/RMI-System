
import Pyro4


server = Pyro4.Proxy("PYRONAME:server") # Conecta com o servidor


# usuario teste
user = {"name": "wagner",
        "email": "wagnerfelidre@gmail.com"
        }

print(server.createUser(user))

print(server.listOfUser())