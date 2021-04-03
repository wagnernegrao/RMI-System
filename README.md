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



## Requisitos

Um cliente deve ter:

* email (chave)
* nome
* sobrenome
* residência 
* formação acadêmica
* habilidades e experiência profissional. 


### Como sugestão tem-se as seguintes operações que podem ser realizadas por um usuário no servidor:

- [x] - 1. listar todas as pessoas formadas em um determinado curso;
- [x] - 2. listar as habilidades dos perfis que moram em uma determinada cidade;
- [x] - 3. acrescentar uma nova experiência em um perfil;
- [x] - 4. dado o email do perfil, retornar sua experiência;
- [ ] - 5. listar todas as informações de todos os perfis;
- [ ] - 6. dado o email de um perfil, retornar suas informações.
