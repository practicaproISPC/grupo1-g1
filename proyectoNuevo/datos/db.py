import pyodbc

direccion_servidor = 'localhost'
nombre_bd = 'ricosabores'
nombre_usuario = 'admin'
password = '12345'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                            direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("\n"*2)
    print("conexi�n exitosa")
    
except Exception as e:
    print("Ocurri� un error al conectar a SQL Server: ", e)