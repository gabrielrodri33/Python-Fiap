import oracledb
import getpass
import credenciais

def conexao():
    try:
        user, pwd = credenciais.credenciais()
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
                                CONSTRAINT cliente_pk PRIMARY KEY (cpf)
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

        sql_query_imagens = """
                            CREATE TABLE imagens (
                                id_img               INTEGER NOT NULL,
                                img                  VARCHAR2(255) NOT NULL,
                                vistoria_id_vistoria INTEGER NOT NULL,
                                CONSTRAINT imagens_pk PRIMARY KEY (id_img),
                                CONSTRAINT imagens_vistoria_fk FOREIGN KEY (vistoria_id_vistoria) REFERENCES vistoria (id_vistoria)
                            )"""

        sql_query_videos = """
                            CREATE TABLE videos (
                                id_videos            INTEGER NOT NULL,
                                video                VARCHAR2(255) NOT NULL,
                                vistoria_id_vistoria INTEGER NOT NULL,
                                CONSTRAINT videos_pk PRIMARY KEY (id_videos),
                                CONSTRAINT videos_vistoria_fk FOREIGN KEY (vistoria_id_vistoria) REFERENCES vistoria (id_vistoria)
                            )"""

        cursor.execute(sql_query_cliente)
        cursor.execute(sql_query_bike_modelos)
        cursor.execute(sql_query_bikes)
        cursor.execute(sql_query_vistoria)
        cursor.execute(sql_query_imagens)
        cursor.execute(sql_query_videos)

        conn.commit()
        print("Tabelas criadas com sucesso!")
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

#Programa principal
create()