import sys
import os

# Adiciona o caminho da pasta "Arquivos" à lista de caminhos de importação
sys.path.append('/Users/luanmorais/Desktop/Arquivos')

from db_config import DB_CONFIG
import psycopg2

# Usa o dicionário de configuração
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("""
	CREATE TABLE IF NOT EXISTS categorias(
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL
    );
			
	CREATE TABLE IF NOT EXISTS produtos(
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        preco DECIMAL(10, 2) NOT NULL,
        quantidade_estoque INT NOT NULL,
        categoria_id INT REFERENCES categorias(id) ON DELETE SET NULL
    );

	CREATE TABLE IF NOT EXISTS endereco(
        id SERIAL PRIMARY KEY,
        rua VARCHAR(255) NOT NULL,
        cidade VARCHAR(100) NOT NULL,
        estado VARCHAR(50) NOT NULL,
        cep VARCHAR(20) NOT NULL
    );		
			
	CREATE TABLE IF NOT EXISTS clientes(
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        telefone VARCHAR(20),
        endereco_id INT REFERENCES endereco(id) ON DELETE SET NULL
	);
	
	CREATE TABLE IF NOT EXISTS vendas(
        id SERIAL PRIMARY KEY,
        cliente_id INT REFERENCES clientes(id) ON DELETE CASCADE,
        data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
	
	CREATE TABLE IF NOT EXISTS itens_venda(
        id SERIAL PRIMARY KEY,
        venda_id INT REFERENCES vendas(id) ON DELETE CASCADE,
        produto_id INT REFERENCES produtos(id) ON DELETE CASCADE,
        quantidade INT NOT NULL,
        preco_unitario DECIMAL(10, 2) NOT NULL
    );
		    """)

if __name__ == "__main__":
    print("Tabelas criadas com sucesso.")

conn.commit()

cur.close()
conn.close()