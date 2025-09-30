# Excluindo Tabelas e Dados no PostgreSQL com Python

Este módulo demonstra como excluir dados e tabelas em um banco de dados PostgreSQL utilizando Python e a biblioteca `psycopg2`.

## Funcionalidades

- Excluir todas as linhas de uma tabela com o comando `DELETE`.
- Excluir uma tabela do banco de dados com o comando `DROP TABLE`.

## Exemplo de Uso

O script `Excluindo_Tabelas.py` realiza as seguintes operações:
1. Remove todos os registros da tabela `clientes`.
2. Exclui a tabela `clientes` do banco de dados.

## Pré-requisitos

- Python 3.x
- Biblioteca `psycopg2` instalada (`pip install psycopg2`)
- Arquivo `db_config.py` com as configurações de acesso ao banco de dados PostgreSQL.

## Como Executar

1. Certifique-se de que o PostgreSQL está em execução e o arquivo `db_config.py` está configurado corretamente.
2. Execute o script:
$ python Excluindo_Tabelas.py

Autor: Luan
Data de criação: 28/09/2025
"""