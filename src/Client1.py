import sys
import Pyro4
from rmi_client import RMIClient
import time_execution as te


HELP_TEXT = '''
[1] Listar todas as pessoas formadas em um determinado curso;
[2] Listar as habilidades dos perfis que moram em uma determinada cidade;
[3] Acrescentar uma nova experiência em um perfil;
[4] Dado o email do perfil, retornar sua experiência;
[5] Listar todas as informações de todos os perfis;
[6] Dado o email de um perfil, retornar suas informações.
'''

# def get_command_code():
#     while True:
#         try:
#             n = int(input('Comando: '))
#             if not 1 <= n <= 6:
#                 raise ValueError()
#             break
#         except ValueError:
#             print('Valor invalido!')
#             pass
#     return n

def execute_operation(command):
    # print(f'Operação {command}')
    # Listar todas as pessoas formadas em um determinado curso 
    if command == 1:
        # curso = input("Digite uma formação acadêmica: ")
        client.list_users_by_course("Design")
        print("Passou aqui 1")
    # Listar as habilidades dos perfis que moram em uma determinada cidade
    elif command == 2:
        # cidade = input("Digite uma localização: ")
        client.list_abilities_by_city("Belem")
    # Acrescentar uma nova experiência em um perfil
    elif command == 3:
        # email = input("Digite um E-mail: ")
        # experiencia = input("Digite a nova experiencia: ")
        client.add_experience("samille@email.com", "Trabalha com design")
    # Dado o email do perfil, retornar sua experiência
    elif command == 4:
        # email = input("Digite um E-mail: ")
        client.experience_by_email("samille@email.com")
    # Listar todas as informações de todos os perfis
    elif command == 5:
        client.list_all_userinfo()
    # Dado o email de um perfil, retornar suas informações
    elif command == 6:
        # email = input("Digite um E-mail: ")
        client.user_by_email("samille@email.com")
        print("Passou aqui 6")

if __name__ == '__main__':
    server = Pyro4.Proxy("PYRONAME:server")
    client = RMIClient(server)

    # print(HELP_TEXT)

    tempo = te.TimeExecution()

    # Aqui inicia o loop principal, pra cada código de operação de 1 a 6
    # são feitas 20 execuções
    for op in range(1, 7):
        for _ in range(20):
            print("Passou aqui -> ", op)
            execute_operation(op)

    tempo.exportData(sys.argv[1])
    # Escolha da operação pela linha de comandos, com N repetições
    #while n < 5:
    #    c = get_command_code() # espera a entrada do usuario
    #    execute_operation(c)
    #    n += 1
    
