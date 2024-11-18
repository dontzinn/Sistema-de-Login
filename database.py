import psycopg2
import os
from psycopg2 import Error

# Fazendo a tratativa para quando houver um erro ao conectar com o banco
def conecta():
    try:
        connection = psycopg2.connect(
            host='localhost', 
            database='usuarios', 
            user='postgres', 
            password=''
        )
        print("Conectado no postgre com sucesso!!")
        return connection

    except Error as e:
        print(f"Ocorreu um erro ao conectar no banco de dados: {e}")

def encerrar_conexao(connection):
    if connection:
        connection.close()
    print("Conexão encerrada")
