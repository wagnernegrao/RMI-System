import Pyro4
from client_app import ClientApp

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
[6] Dado o email de um perfil, retornar suas informações.\n
'''

def main():
    server = Pyro4.Proxy("PYRONAME:server")

    # Criando usuarios para testes
    print(server.createUser(user))
    print(server.createUser(user2))

    client = ClientApp(server)

    print(HELP_TEXT)
    command = ClientApp.get_command_code()

    if command == 1:
        print('Listar todas as pessoas formadas em um determinado curso')

    elif command == 2:
        print('Listar as habilidades dos perfis que moram em uma determinada cidade')

    elif command == 3:
        print('Acrescentar uma nova experiência em um perfil')

    elif command == 4:
        print('Dado o email do perfil, retornar sua experiência')

    elif command == 5:
        # Listar todas as informações de todos os perfis
        client.list_all_userinfo()

    elif command == 6:
        print('Dado o email de um perfil, retornar suas informações')


if __name__ == '__main__':
    main()
