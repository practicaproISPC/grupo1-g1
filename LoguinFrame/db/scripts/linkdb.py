import pyodbc
direccion_servidor = 'localhost'
nombre_bd = 'RicosSaboresDB'
nombre_usuario = 'ricosabores'
password = 'ricos1234'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # Mostrar la conexión  exitosa
    print('la conexion fue correcta')
except Exception as e:
    # Mostrar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO Usuarios(id_usuario, Usuario, email, Nombre, Apellido) VALUES (?, ?);"
        cursor.execute(consulta, (1, "Usuario1", "email1", "Nombre1", "apellido1"))
        cursor.execute(consulta, (2, "Usuario2", "email2", "Nombre2", "apellido2"))
    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
    print(" La carga de usuario fue realizada con éxito")

except Exception as e:
    print("Ocurrió un error al insertar usuario: ", e)
finally:
    conexion.close()

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT * FROM Usuarios;")
       
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()