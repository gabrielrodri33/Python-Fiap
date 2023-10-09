# https://www.geeksforgeeks.org/how-to-install-cx_oracle-in-python-on-windows

'''
1 - Oracle DB
2 - Python Lib (Bibliotecas Python)
3 - DB details
4 - Driver: cx_Oracle

PEP 249 - Python Database specification 2.0

Módulos Python
- cx_Oracle - Oracle Database
- pyodbc - Microsoft SQL Server
- pymsql - MySQL
- Psycopg2 - PostgreeSQL

1. Importar o driver cx_Oracle
2. Estabelecer uma conexão entre o Python e o DB
3. Criar um cursor (objeto para executar queries e obter resultados após a execução)
'''

import cx_Oracle

#Create connection

conn = cx_Oracle.connect(user="RM98626", password="311003", host="oracle.fiap.com.br", port="1521", service_name="orcl")
# conn = cx_Oracle.connect(user="RM98626", password="311003", host="oracle.fiap.com.br/orcl")
print(conn.version)

#Create cursor
cursor = conn.cursor()

#Create table
sql_create = """
CREATE TABLE ceo_details(
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    company VARCHAR2(50),
    age NUMBER()
);
"""

#Execute query
cursor.execute(sql_create)
print("Tabela criada!")

#Fechar a conexão e o cursor
conn.close()
cursor.close()