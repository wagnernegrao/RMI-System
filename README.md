# RMI-System

[Documentação](https://pyro4.readthedocs.io/en/stable/index.html#) da biblioteca utilizada.

## Como executar:

1. Instalar Docker e Docker-compose.

2. Construir os contêineres com `docker-compose build`.

3. Subir os contêineres com `docker-compose up --detach`.

4. Entrar no contêiner de um cliente com `docker exec -it rmi_client_{numero}` e executar `python rmi_client.py`.

5. Entrar no contêiner de um cliente com `docker exec -it rmi_client_{numero}` e executar `python time_execution.py`.

6. Entrar no contêiner de um cliente com `docker exec -it rmi_client_{numero}` e executar `python Client{numero}.py`.

7. Descer os contêineres com `docker-compose down --remove-orphans --volumes`.
