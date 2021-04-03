# RMI-System

## Primeiro
Instalar o Pyro4

```
pip3 install Pyro4
```

[Documentação](https://pyro4.readthedocs.io/en/stable/index.html#)

## Segundo

Abrir 3 abas no terminal

1ª aba:
  rodar o comando ```python3 -m Pyro4.naming``` esse comando serve pra deixar global o nome do servidor, ai não precisa ficar copiando a URI do servidor.
  
2ª e 3ª aba:
  rodar o servidor e outra o cliente.


## Docker

1. Instalar Docker e Docker-compose.

2. Construir os contêineres com `docker-compose build`.

3. Subir os contêineres com `docker-compose up --detach`.

4. Entrar no contêiner de um cliente com `docker exec -it rmi_client_{numero}` e executar `python Client.py`.

5. Descer os contêineres com `docker-compose down --remove-orphans --volumes`.