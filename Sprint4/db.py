import oracledb
from datetime import datetime

def credenciais():
    return "RM98626", "311003"

def conexao():
    try:
        user, pwd = credenciais()
        conn = oracledb.connect(user=user, password=pwd, host="oracle.fiap.com.br", port="1521", service_name="orcl")
        cursor = conn.cursor()
        # print(f"Conexão {conn.version}")
    except Exception as e:
        print(f'Something went wrong - conexao: {e}') 
    return conn, cursor

def create():
    try:
        conn, cursor = conexao()
        sql_query_cliente = """
                            CREATE TABLE cliente (
                                cpf         VARCHAR2(15) NOT NULL,
                                nome        VARCHAR2(100) NOT NULL,
                                dt_nasc     DATE NOT NULL,
                                tel_fixo    VARCHAR2(15),
                                tel_celular VARCHAR2(15),
                                email       VARCHAR2(100) NOT NULL,
                                senha       VARCHAR2(1000) NOT NULL,
                                CONSTRAINT cliente_pk PRIMARY KEY (cpf)
                            )"""
        
        sql_query_endereco = """
                            CREATE TABLE endereco (
                                cliente_cpf   VARCHAR2(15) PRIMARY KEY,
                                logradouro    VARCHAR2(255) NOT NULL,
                                bairro        VARCHAR2(255) NOT NULL,
                                numero        VARCHAR2(10),
                                complemento   VARCHAR2(100),
                                cidade        VARCHAR2(100) NOT NULL,
                                estado        VARCHAR2(2) NOT NULL,
                                cep           VARCHAR2(8) NOT NULL,
                                CONSTRAINT endereco_cliente_fk FOREIGN KEY (cliente_cpf) REFERENCES cliente (cpf)
                            )"""

        sql_query_bike_modelos = """
                            CREATE TABLE bike_modelos (
                                id_modelo   INTEGER NOT NULL,
                                nome        VARCHAR2(255) NOT NULL,
                                valor_aprox NUMBER(18, 2),
                                CONSTRAINT bike_modelos_pk PRIMARY KEY (id_modelo)
                            )"""

        sql_query_bikes = """
                            CREATE TABLE bikes (
                                num_serie              VARCHAR2(255) NOT NULL,
                                valor                  NUMBER(18, 2) NOT NULL,
                                cor                    VARCHAR2(255) NOT NULL,
                                bike_modelos_id_modelo INTEGER NOT NULL,
                                CONSTRAINT bikes_pk PRIMARY KEY (num_serie),
                                CONSTRAINT bikes_bike_modelos_fk FOREIGN KEY (bike_modelos_id_modelo) REFERENCES bike_modelos (id_modelo)
                            )"""

        sql_query_vistoria = """
                            CREATE TABLE vistoria (
                                id_vistoria     INTEGER NOT NULL,
                                dt_inicio       DATE NOT NULL,
                                dt_fim          DATE,
                                aprov           CHAR(1) NOT NULL,
                                obs             CLOB,
                                bikes_num_serie VARCHAR2(255) NOT NULL,
                                cliente_cpf     VARCHAR2(15) NOT NULL,
                                CONSTRAINT vistoria_pk PRIMARY KEY (id_vistoria),
                                CONSTRAINT vistoria_bikes_fk FOREIGN KEY (bikes_num_serie) REFERENCES bikes (num_serie),
                                CONSTRAINT vistoria_cliente_fk FOREIGN KEY (cliente_cpf) REFERENCES cliente (cpf)
                            )"""

        cursor.execute(sql_query_cliente)
        cursor.execute(sql_query_endereco)
        cursor.execute(sql_query_bike_modelos)
        cursor.execute(sql_query_bikes)
        cursor.execute(sql_query_vistoria)
        conn.commit()
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f'Something went wrong - create: {e}')
    finally:
        conn.close()

def insert(cpf, nome, dt_nasc, tel_fixo, tel_celular, email, senha):
    try:
        conn, cursor = conexao()

        dt_nasc_formatada = datetime.strptime(dt_nasc, '%d/%m/%Y').strftime('%Y-%m-%d')

        sql_query = "INSERT INTO cliente (cpf, nome, dt_nasc, tel_fixo, tel_celular, email, senha) VALUES (:cpf, :nome, TO_DATE(:dt_nasc, 'YYYY-MM-DD'), :tel_fixo, :tel_celular, :email, :senha)"
        cursor.execute(sql_query, {
            'cpf': cpf,
            'nome': nome,
            'dt_nasc': dt_nasc_formatada,
            'tel_fixo': tel_fixo,
            'tel_celular': tel_celular,
            'email': email,
            'senha': senha
        })
        conn.commit()
        print("Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Something went wrong - insert {e}")
    finally:
        conn.close()

def insertEndereco(cpf, logradouro, bairro, numero, complemento, cidade, estado, cep):
    try:
        conn, cursor = conexao()

        sql_query = "INSERT INTO endereco (cliente_cpf, logradouro, bairro, numero, complemento, cidade, estado, cep) VALUES (:cliente_cpf, :logradouro, :bairro, :numero, :complemento, :cidade, :estado, :cep)"
        cursor.execute(sql_query, {
            'cliente_cpf': cpf,
            'logradouro': logradouro,
            'bairro': bairro,
            'numero': numero,
            'complemento': complemento,
            'cidade': cidade,
            'estado': estado,
            'cep': cep
        })
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
            value_str = str(value)
        else:
            value_str = f"'{value.replace("'", "''")}'"

        sql_query = f"UPDATE {table} SET {dado} = {value_str} WHERE cpf = :cpf"
        cursor.execute(sql_query, {'cpf': cpf})
        conn.commit()
        print("Atualizado com sucesso")
    except Exception as e:
        print(f'Something went wrong - update: {e}')
    finally:
        conn.close()

def updatePwd(table, dado, value_bytes, email):
    try:
        conn, cursor = conexao()

        value_hex = value_bytes.hex()
        value_str = f"HEXTORAW('{value_hex}')"

        sql_query = f"UPDATE {table} SET {dado} = {value_str} WHERE email = :email"
        cursor.execute(sql_query, {'email': email})
        conn.commit()
        print("Atualizado com sucesso")
    except Exception as e:
        print(f'Something went wrong - updatePwd: {e}')
    finally:
        cursor.close()
        conn.close()

def updateDate(table, dado, value, cpf):
    try:
        conn, cursor = conexao()

        formatted_date = datetime.strptime(value, '%d/%m/%Y').strftime('%Y/%m/%d')


        sql_query = f"UPDATE {table} SET {dado} = TO_DATE(:date_value, 'YYYY/MM/DD') WHERE cpf = :cpf"
        cursor.execute(sql_query, {'date_value': formatted_date, 'cpf': cpf})
        conn.commit()
        print("Atualizado com sucesso")
    except Exception as e:
        print(f'Something went wrong - update: {e}')
    finally:
        conn.close()

def select(dado1, tbl, dado2):
    try:
        conn, cursor = conexao()

        sql_query = f"SELECT {dado1} FROM {tbl} WHERE {dado2} = :dado2"
        cursor.execute(sql_query, dado2=dado2)

        resultados = cursor.fetchall()

        for resultado in resultados:
            print(f"{dado1}: {resultado[0]}")

    except Exception as e:
        print(f'Something went wrong - select: {e}')
    finally:
        conn.close()

def verifica_cpf_existente(cpf):
    try:
        conn, cursor = conexao()

        sql_query = "SELECT COUNT(*) FROM cliente WHERE cpf = :cpf"
        cursor.execute(sql_query, cpf=cpf)

        resultado = cursor.fetchone()
        count = resultado[0]

        if count > 0:
            print(f"CPF {cpf} já cadastrado.")
            return True
        else:
            print(f"CPF {cpf} não cadastrado.")
            return False

    except Exception as e:
        print(f'Something went wrong - verifica_cpf_existente: {e}')
    finally:
        conn.close()

def verifica_email_existente(email):
    try:
        conn, cursor = conexao()

        sql_query = "SELECT COUNT(*) FROM cliente WHERE email = :email"
        cursor.execute(sql_query, email=email)

        resultado = cursor.fetchone()
        count = resultado[0]

        if count > 0:
            print(f'E-mail: "{email}" já cadastrado.')
            return True
        else:
            return False

    except Exception as e:
        print(f'Something went wrong - verifica_email_existente: {e}')
    finally:
        conn.close()


def delete(cpf):
    try:
        conn, cursor = conexao()
        sql_query = (f"DELETE FROM cliente WHERE fis_jur_cliente = {cpf}")
        cursor.execute(sql_query)
        conn.commit()
        print("Usuário deletado com sucesso!")
    except Exception as e:
        print(f"Something went wrong - delete: {e}")
    finally:
        conn.close()

#Programa principal
create()