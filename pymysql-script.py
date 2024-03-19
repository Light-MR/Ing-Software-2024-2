import pymysql
import conexion  as conexion
from datetime import datetime, timedelta
import random
import string

# inserte al menos 1 registro en cada tabla cada vez que sea ejecutada

# Función para insertar registros en todas las tablas
def insertar_registros():
    c = conexion.conectar_bd()
    c.autocommit(True) 
    cursor = c.cursor()

    try:
        # Generar datos aleatorios para la película
        nombre_pelicula = generar_nombre()
        genero_pelicula = random.choice(['Accion', 'Comedia', 'Drama', 'Aventura'])
        if not verificar_existencia_pelicula(nombre_pelicula, genero_pelicula, cursor):
            cursor.execute("INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, 120, 5)", (nombre_pelicula, genero_pelicula))
            pelicula_id = cursor.lastrowid
        else:
            print("\nRegistro existente.\n")
            cursor.execute("SELECT idPelicula FROM peliculas WHERE nombre = %s AND genero = %s", (nombre_pelicula, genero_pelicula))
            pelicula_id = cursor.fetchone()
        
        # Solicitar datos al usuario
        nombre_usuario = input("Ingrese nombre del usuario: ")
        ap_pat_usuario = input("Ingrese apellido paterno del usuario: ")
        ap_mat_usuario = input("Ingrese apellido materno del usuario: ")
        email_usuario = input("Ingrese correo electrónico del usuario: ")

        # Verificar si existe el usuario
        if not verificar_existencia_usuario(nombre_usuario, ap_pat_usuario, ap_mat_usuario, email_usuario, cursor):
            cursor.execute("INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, 'password123', %s, 1)", (nombre_usuario, ap_pat_usuario, ap_mat_usuario, email_usuario))
            usuario_id = cursor.lastrowid
        else:
            print("\nRegistro ya existente\n")
            cursor.execute("SELECT idUsuario FROM usuarios WHERE nombre = %s AND apPat = %s AND apMat = %s AND email = %s", (nombre_usuario, ap_pat_usuario, ap_mat_usuario, email_usuario))
            row = cursor.fetchone()
            if row is not None:
                usuario_id = row[0]
            else:
                print("No se pudo obtener el ID del usuario.")
                return

        # Verificar si existe la renta
        if not verificar_existencia_renta(usuario_id, pelicula_id, cursor):
            fecha_renta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta) VALUES (%s, %s, %s)", (usuario_id, pelicula_id, fecha_renta))
        
        conexion.commit()
        print("Registros insertados correctamente.")
    except pymysql.Error as e:
        conexion.rollback()
        print("Error al insertar registros:", e)

    c.close()


# Auxiliares para la inserción de registros


# Función para verificar si existe una película con el nombre y género dados
def verificar_existencia_pelicula(nombre_pelicula, genero_pelicula, cursor):
    cursor.execute("SELECT COUNT(*) FROM peliculas WHERE nombre = %s AND genero = %s", (nombre_pelicula, genero_pelicula))
    row = cursor.fetchone()
    if row is  None :
        return False
    else:
        return True
# Función para verificar si existe un usuario con el nombre, apellidos y email dados
def verificar_existencia_usuario(nombre, ap_pat, ap_mat, email, cursor):
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nombre = %s AND apPat = %s AND apMat = %s AND email = %s", (nombre, ap_pat, ap_mat, email))
    row = cursor.fetchone()
    if row is  None :
        return False
    else:
        return True

# Función para verificar si existe una renta para un usuario y una película dados
def verificar_existencia_renta(id_usuario, id_pelicula, cursor):
    cursor.execute("SELECT COUNT(*) FROM rentar WHERE idUsuario = %s AND idPelicula = %s", (id_usuario, id_pelicula))
    row = cursor.fetchone()
    return row is not None

# Función para generar un nombre aleatorio
def generar_nombre():
    return ''.join(random.choices(string.ascii_letters, k=6))

# Función para generar un email aleatorio
def generar_email():
    nombre = generar_nombre()
    dominio = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
    return f'{nombre}@{dominio}'



def filtrar_usuarios_por_apellido(ap_terminacion):
    con = conexion.conectar_bd()
    con.autocommit(True) 
    cursor = con.cursor()

    try:
        # Consulta SQL para filtrar usuarios
        query = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
        apellido_like = f'%{ap_terminacion}'
        cursor.execute(query, (apellido_like, apellido_like))
        usuarios = cursor.fetchall()

        # Mostrar resultados
        if usuarios:
            print("Usuarios encontrados:")
            for usuario in usuarios:
                print(f"ID: {usuario['idUsuario']}, Nombre: {usuario['nombre']}, Apellido Paterno: {usuario['apPat']}, Apellido Materno: {usuario['apMat']}, Email: {usuario['email']}")
        else:
            print("No se encontraron usuarios con el apellido proporcionado.")

    except pymysql.Error as e:
        print("Error al filtrar usuarios:", e)

    con.close()
    
    
# Función para cambiar el género de una película
def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    con = conexion.conectar_bd()
    con.autocommit(True) 
    cursor = con.cursor()

    try:
        # Verificar si la película existe
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre_pelicula,))
        pelicula = cursor.fetchone()

        if pelicula:
            # Si la película existe, actualizar su género
            cursor.execute("UPDATE peliculas SET genero = %s WHERE idPelicula = %s", (nuevo_genero, pelicula['idPelicula']))
            conexion.commit()
            print(f"El género de la película '{nombre_pelicula}' se ha actualizado a '{nuevo_genero}'.")
        else:
            print("La película especificada no existe en la base de datos.")

    except pymysql.Error as e:
        conexion.rollback()
        print("Error al cambiar el género de la película:", e)

    con.close()
    
# Función para eliminar rentas anteriores a 3 días antes de la fecha actual
def eliminar_rentas_antiguas():
    con = conexion.conectar_bd()
    con.autocommit(True) 
    cursor = con.cursor()

    try:
        # Obtener la fecha límite (3 días antes de la fecha actual)
        fecha_limite = datetime.now() - timedelta(days=3)

        # Eliminar las rentas anteriores a la fecha límite
        cursor.execute("DELETE FROM rentar WHERE fecha_renta <= %s", (fecha_limite,))
        cantidad_eliminada = cursor.rowcount
        conexion.commit()

        print(f"Se eliminaron {cantidad_eliminada} rentas anteriores al {fecha_limite.date()}.")

    except pymysql.Error as e:
        conexion.rollback()
        print("Error al eliminar rentas antiguas:", e)

    con.close()

def main():
    insertar_registros()
    
    """
    ap_terminacion = input("Ingrese la terminación del apellido a buscar: ")
    filtrar_usuarios_por_apellido(ap_terminacion)
    
    nombre_pelicula = input("Ingrese el nombre de la película a modificar: ")
    nuevo_genero = input("Ingrese el nuevo género para la película: ")
    cambiar_genero_pelicula(nombre_pelicula, nuevo_genero)
    
    eliminar_rentas_antiguas()"""

if __name__ == "__main__":
    main()