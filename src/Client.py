import Pyro4
from rmi_client import RMIClient

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
        "email": "wagner@email.com",
        "residencia": "rua jarbas passarinho",
        "formacao_academica": "pedreiro",
        "habilidades": "javaboy",
        "experiencia_profissional": "dev"
}

HELP_TEXT = '''
[1] Listar todas as pessoas formadas em um determinado curso;
[2] Listar as habilidades dos perfis que moram em uma determinada cidade;
[3] Acrescentar uma nova experiência em um perfil;
[4] Dado o email do perfil, retornar sua experiência;
[5] Listar todas as informações de todos os perfis;
[6] Dado o email de um perfil, retornar suas informações.
'''

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

def execute_operation(command):
    # Listar todas as pessoas formadas em um determinado curso 
    if command == 1:
        curso = input("Digite uma formação acadêmica: ")
        client.list_users_by_course(curso)
    # Listar as habilidades dos perfis que moram em uma determinada cidade
    elif command == 2:
        cidade = input("Digite uma localização: ")
        client.list_abilities_by_city(cidade)
    # Acrescentar uma nova experiência em um perfil
    elif command == 3:
        email = input("Digite um E-mail: ")
        experiencia = input("Digite a nova experiencia: ")
        client.add_experience(email, experiencia)
    # Dado o email do perfil, retornar sua experiência
    elif command == 4:
        email = input("Digite um E-mail: ")
        client.experience_by_email(email)
    # Listar todas as informações de todos os perfis
    elif command == 5:
        client.list_all_userinfo()
    # Dado o email de um perfil, retornar suas informações
    elif command == 6:
        email = input("Digite um E-mail: ")
        client.user_by_email(email)

if __name__ == '__main__':
    server = Pyro4.Proxy("PYRONAME:server")

    # Criando usuarios para testes
    server.createUser(user)
    server.createUser(user2)

    client = RMIClient(server)
    print(HELP_TEXT)

    n = 0
    while n < 5:
        c = get_command_code() # espera a entrada do usuario
        execute_operation(c)
        n += 1
    
