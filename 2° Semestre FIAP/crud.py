import cx_Oracle
#import oracledb

#Obter conexao
def conexao():
    try:
        conn = cx_Oracle.connect(user="RM98626", password="311003", host="oracle.fiap.com.br", port="1521", 
                                 service_name="orcl")
        print(f"Conexão: {conn.version}")
    except Exception as e:
        print("Erro ao obter uma conexão", e)
    return conn

def select():
    conn = conexao()
    cursor = conn.cursor()
    sql_query = "SELECT * FROM <tabela>"
    cursor.execute(sql_query)
    for result in cursor:
        print(result)
    conn.commit()

def insert():
    conn = conexao()
    cursor = conn.cursor()
    sql_query = "INSERT INTO ceo_details VALUES('Steve', 'Jobs', 'Apple', 50)"
    cursor.execute(sql_query)
    conn.commit()

def update():
    try:
        conn = conexao()
        cursor = conn.cursor()
        sql_query = "UPDATE ceo_details SET AGE = 50 WHERE first_name = 'Steve'"
        cursor.execute()
        conn.commit()
        print("CEO updated!")
    except Exception as e:
        print(f'Something went wrong - update: {e}')
    finally:
        
        conn.close()

def delete():
    try:
        conn = conexao()
        cursor = conn.cursor()
        sql_query = "DELETE FROM ceo_details WHERE AGE = 50"
        cursor.execute(sql_query)
        conn.commit()
        print("CEO removed!")
    except Exception as e:
        print(f'Something went wrong - delete: {e}')
    finally:
        conn.close()

def close_connection(conn):
    try:
        conn.close()
        print(f'Connection closed!')
    except Exception as e:
        print(f'Something went wrong - close_connection {e}')

#Programa pricipal
print(f'Obtendo dados do BD')
conn = conexao()
select()
close_connection(conn)