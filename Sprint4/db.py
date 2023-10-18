import oracledb
import getpass

def conexao():
    try:
        user = getpass.getpass("User: ")
        pwd = getpass.getpass("Password: ")
        conn = oracledb.connect(user=user, password=pwd, host="oracle.fiap.com.br", port="1521", service_name="orcl")
        cursor = conn.cursor()
        # print(f"Conexão {conn.version}")
    except Exception as e:
        print(f'Something went wrong - conexao: {e}') 
    return conn, cursor

def create():
    try:
        conn, cursor =  conexao()
        cursor.execute("SELECT table_name FROM user_tables WHERE table_name = 'tbl_cliente'")
        result = cursor.fetchone()

        if result is None:
            cursor.execute("DROP TABLE tbl_cliente")

        sql_query = """
                    CREATE TABLE tbl_cliente(
                        fis_jur_cliente        NUMBER(11)     NOT NULL    PRIMARY KEY,
                        nome_cliente           VARCHAR2(45)   NOT NULL,
                        dt_nasc_cliente        DATE           NOT NULL,
                        tel_fixo_cliente       NUMBER(8),
                        tel_celular_cliente    NUMBER(11)     NOT NULL,
                        email_cliente          VARCHAR2(50)   NOT NULL
                    )
                    """

        cursor.execute(sql_query)
        conn.commit()
        # print("Tabela criada com sucesso!")
    except Exception as e:
        print(f'Something went wrong - create: {e}')
    finally:
        conn.close()

def insert(cpf, nome, dt_nasc, tel_fixo, tel_celular, email):
    try:
        conn, cursor = conexao()
        sql_query = f"INSERT INTO tbl_cliente VALUES({cpf}, '{nome}', TO_DATE('{dt_nasc}', 'YYYY-MM-DD'), {tel_fixo}, {tel_celular}, '{email}')"
        cursor.execute(sql_query)
        conn.commit()
        print("Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Something went wrong - insert {e}")
    finally:
        conn.close()

def update(table, dado, value, cpf):
    try:
        conn, cursor = conexao()

        if isinstance(value, (int, float)):
            value_str = value
        else:
            value_str = f"'{value}'"

        sql_query = f"UPDATE {table} SET {dado} = {value_str} WHERE fis_jur_cliente = {cpf}"
        cursor.execute(sql_query)
        conn.commit()
        print("Atualizado com sucesso")
    except Exception as e:
        print(f'Something went wrong - update: {e}')
    finally:
        conn.close()

def delete(cpf):
    try:
        conn, cursor = conexao()
        sql_query = (f"DELETE FROM tbl_cliente WHERE fis_jur_cliente = {cpf}")
        cursor.execute(sql_query)
        conn.commit()
        print("Usuário deletado com sucesso!")
    except Exception as e:
        print(f"Something went wrong - delete: {e}")
    finally:
        conn.close()

conexao()