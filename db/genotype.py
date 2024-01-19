import sqlite3
from sqlite3 import Error
from .connection import create_connection

# Insertar muestra nueva
def insert_genotype(data):
    conn = create_connection()
    sql = """ INSERT INTO genotypes (temperature_melting_1016, temperature_melting_1534, temperature_melting_1016_SS, temperature_melting_1016_SR, temperature_melting_1016_RR, temperature_melting_1534_SS, temperature_melting_1534_SR, temperature_melting_1534_RR)
              VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nueva muestra agregada")
        return True
    except Error as e:
        print("Error inserting new genotype: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

# Modificar muestra
def update_genotype(_id, data):
    conn = create_connection()

    sql = f""" UPDATE genotypes SET
                               temperature_melting_1016 = ?,
                               temperature_melting_1534 = ?,
                               temperature_melting_1016_SS = ?,
                               temperature_melting_1016_SR = ?,
                               temperature_melting_1016_RR = ?,
                               temperature_melting_1534_SS = ?,
                               temperature_melting_1534_SR = ?,
                               temperature_melting_1534_RR = ?
                            
            WHERE genotype_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Muestra Actualizada")
        return True
    except Error as e:
        print("Error updating genotype: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()


# Eliminar muestra
def delete_genotype(_id):
    conn = create_connection()
    sql = f"DELETE FROM genotypes WHERE genotype_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Muestra Eliminada")
        return True
    except Error as e:
        print("Error deleting genotype: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()


# Consulta que devuelve todos las muestras de la base de datos
def select_all_genotypes():
    conn = create_connection()
    sql = "SELECT * from genotypes"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        genotypes = cur.fetchall()
        return genotypes
    except Error as e:
        print("Error selecting all genotypes: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

# Consulta todos las muestras de la base de datos
def delete_all_genotypes():
    conn = create_connection()
    sql = "DELETE FROM genotypes"
    sql_reset_sequence = "DELETE FROM sqlite_sequence WHERE name='genotypes'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        cur.execute(sql_reset_sequence)
        conn.commit()
        genotypes = cur.fetchall()
        print("Todos los genotipos eliminados y contador de ID restablecido")
        return genotypes
    except Error as e:
        print("Error deleting all genotypes: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

# Devuelve una muestra con su ID
def select_genotype_by_id(_id):
    conn = create_connection()
    sql = f"SELECT * FROM genotypes WHERE genotype_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        genotype = cur.fetchone()
        return genotype
    except Error as e:
        print("Error selecting genotype by ID: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

# Búsqueda por ID
def select_genotype_by_id(_id):
    conn = create_connection()
    sql = f"SELECT * FROM genotypes WHERE genotype_id LIKE '%{_id}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        genotype = cur.fetchall()
        return genotype
    except Error as e:
        print("Error selecting genotype by ID: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

# Búsqueda por Temperatura de Melting (1016)
def select_genotype_by_temperature_melting_1016(temperature):
    conn = create_connection()
    sql = f"SELECT * FROM genotypes WHERE temperature_melting_1016 LIKE '%{temperature}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        genotype = cur.fetchall()
        return genotype
    except Error as e:
        print("Error selecting genotype by temperature melting 1016: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

# Búsqueda por Temperatura de Melting (1534)
def select_genotype_by_temperature_melting_1534(temperature):
    conn = create_connection()
    sql = f"SELECT * FROM genotypes WHERE temperature_melting_1534 LIKE '%{temperature}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        genotype = cur.fetchall()
        return genotype
    except Error as e:
        print("Error selecting genotype by temperature melting 1534: " + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()