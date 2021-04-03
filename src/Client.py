import Pyro4
import time
import timeExecution as te

server = Pyro4.Proxy("PYRONAME:server") # Conecta com o servidor


# email = input("Email: ")
# nome = input("Nome: ")
# sobrenome = input("Sobrenome: ")
# residencia = input("Residencia: ")
# formacao_academica = input("Formacao academica: ")
# habilidades = input("Habilidades: ")
# experiencia_profissional = input("Experiencia profissional: ")


# user = {"nome": nome,
#         "sobrenome": sobrenome,
#         "email": email,
#         "residencia": residencia,
#         "formacao_academica": formacao_academica,
#         "habilidades": habilidades,
#         "experiencia_profissional": experiencia_profissional 
#         }


# usuario teste
user = {"nome": "wagner",
        "sobrenome": "negrao",
        "email": "wagner@email.com",
        "residencia": "rua jarbas passarinho",
        "formacao_academica": "cientista computacao",
        "habilidades": "dev",
        "experiencia_profissional": "dev"
        }

user2 = {"nome": "wagner",
        "sobrenome": "negrao",
        "email": "email@email.com",
        "residencia": "rua jarbas passarinho",
        "formacao_academica": "pedreiro",
        "habilidades": "javaboy",
        "experiencia_profissional": "dev"
}

print(server.createUser(user))
print(server.createUser(user))
print(server.createUser(user2))

# graduacao = input("Qual graduacao: ")
# print(server.findByGraduation(graduacao))

# habilidade = input("Qual habilidade: ")
# print(server.findByAbilities(habilidade))

# email = input("Qual email: ")
# habilidade = input("Qual habilidade: ")
# print(server.modifyAbilitie(email , habilidade))

email = input("Qual email: ")
t1 = time.time()
print(server.findByExperience(email))
t2 = time.time()

te.TimeExecution().timeCreateUser(t1, t2)

te.TimeExecution().exportData()