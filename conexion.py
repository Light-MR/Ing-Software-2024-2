import pymysql.cursors

def conectar_bd():
    try:
        conexion = pymysql.connect(
        host = 'localhost',
        user = 'lab',
        password = 'Developer123!',
        database= 'lab_ing_software',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
        print("\nConexion exitosa a la base de datos.")
        return conexion
    except pymysql.Error as e:
        print("\nError al intentar establecer conexion con la base de datos:",e)
    
