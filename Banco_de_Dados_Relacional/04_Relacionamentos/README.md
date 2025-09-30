"""
Criando_Relacionamentos.py

Este script cria tabelas relacionadas em um banco de dados PostgreSQL utilizando Python e a biblioteca psycopg2.  
As tabelas representam um modelo de vendas, incluindo clientes, endereços, categorias, produtos, vendas e itens de venda, com chaves estrangeiras e regras de integridade referencial.

Funcionalidades:
- Criação das tabelas: categorias, produtos, endereco, clientes, vendas e itens_venda.
- Definição de relacionamentos entre tabelas usando chaves estrangeiras.
- Uso de regras ON DELETE (SET NULL, CASCADE) para manter a integridade dos dados ao excluir registros relacionados.
- Mensagem de confirmação ao executar o script diretamente.

Pré-requisitos:
- Python 3.x
- psycopg2 instalado (`pip install psycopg2`)
- Arquivo db_config.py com o dicionário DB_CONFIG contendo as configurações de acesso ao banco de dados PostgreSQL.

Como executar:
$ python Criando_Relacionamentos.py

Autor: Luan
Data de criação: 30/09/2025
"""