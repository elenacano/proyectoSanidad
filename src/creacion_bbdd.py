import psycopg2 # type: ignore
from psycopg2 import OperationalError, errorcodes, errors # type: ignore

from src import soporte_queries_creacion

def establecer_conexion(nombre_bbdd):
    try:  
        conexion = psycopg2.connect(
            database = nombre_bbdd,
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = "5432")
        
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La contraseña es erronea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexion")
        else:
            print(f"Ocurrió el error {e}")

    cursor = conexion.cursor()

    return conexion, cursor


def ejecutar_commit(cursor, conexion, query):
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    cursor.close()


def creacion_tablas(cursor, conexion):
    
    # Creación tabla ncodi
    ejecutar_commit(soporte_queries_creacion.query_creacion_ncodi)


    # Creación tabla TipoHospi
    ejecutar_commit(soporte_queries_creacion.query_creacion_tipo_hospi)
    


    # Creación tabla gastos
    ejecutar_commit(soporte_queries_creacion.query_creacion_gastos)


    # Creación tabla ingresos
    ejecutar_commit(soporte_queries_creacion.query_creacion_ingresos)


def dbeaver_commitmany(conexion, query, *values):
    """
    Ejecuta múltiples consultas y realiza un commit de los cambios.

    Args:
        conexion (connection): Un objeto de conexión a la base de datos.
        query (str): La consulta SQL a ejecutar.
        *values: Los valores a incluir en la consulta.

    Returns:
        str: Un mensaje de confirmación después del commit.
    """
    cursor = conexion.cursor()
    cursor.executemany(query, *values)
    conexion.commit()
