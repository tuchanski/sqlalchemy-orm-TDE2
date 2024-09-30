
# SQLAlchemy ORM 🛠️

## Objetivo

Este projeto tem como objetivo realizar operações de inserção, atualização, exclusão e consulta de dados em um banco de dados utilizando o ORM SQLAlchemy em uma aplicação Python.
O banco de dados em questão foi desenvolvido para fins de estudo.
Projeto da matéria "Arquitetura de Banco de Dados" do curso de Ciência da Computação da PUCPR, 2° período.

## Requisitos

### Inserção e Atualização de Dados

1. Inserir pelo menos 6 registros em cada uma das tabelas do banco de dados utilizando as classes que mapeiam as tabelas no Python.
2. Atualizar 5 registros do banco de dados utilizando o ORM SQLAlchemy.
3. Criar 5 instruções de exclusão de registros em diferentes tabelas utilizando o ORM SQLAlchemy.

### Consulta de Dados

1. Realizar 20 consultas definidas no levantamento de requisitos funcionais utilizando o ORM SQLAlchemy.
2. Cada consulta deve ser realizada utilizando as respectivas classes que mapeiam as tabelas do banco de dados.

## Estrutura do Projeto

- `app.py`: Cria o banco de dados populado.
- `deletes.py`: Queries de DELETE.
- `updates.py`: Queries de UPDATE.
- `queries.py`: Queries de SELECT.
- `../config/`: Configurações do projeto.
- `../inserts_data/`: Dados dos inserts feitos no banco.
- `../models/`: Classes de mapeamento.
- `../services/`: Encapsulamento da criação do banco.

# Ferramentas

- Python 3.x
- MySQL

## Dependências

- SQLAlchemy

### Instalação de Dependências

```bash
pip install sqlalchemy
pip install sqlalchemy_orm
pip install sqlalchemy_utils
pip install pymysql
```

### Ordem de execução

1. app.py
2. deletes.py
3. updates.py
4. queries.py

## Autor

- [Guilherme Tuchanski Rocha | GitHub](https://github.com/tuchanski)