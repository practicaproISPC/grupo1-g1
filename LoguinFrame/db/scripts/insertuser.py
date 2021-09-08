from linkdb import conexion
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO Usuarios(Usuario,Nombre, Apellido) VALUES (?, ?);"
        cursor.execute(consulta, ("usuario","nombre1", "apellido1"))
        cursor.execute(consulta, ("usuario","nombre2", "apellido2"))
    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT id, Nombre, Apellido FROM Socios;")
        # Hacer un while, mientras fetchone no regrese None
        usuario = cursor.fetchone()
        while usuario:
            print(usuario)
            usuario = cursor.fetchone()

except Exception as e:
    print("Ocurrió un error al consultar usuario: ", e)
finally:
    conexion.close()