<?php
   //conexion con la base de datos y el servidor
  $link = mysql_connect("localhost","root","") or die ("<h2>No se encuentra el servidor</h2>");
  $db = mysql_select_db("usuarios",$link) or die("<h2>Error de conexion</h2>");
  
  //Obtenemos los valores del formulario
  $Nombre = $_POST('nombreUsuario');
  $apellido = $_POST('apellidoUsuario');
  $fechanac = $_POST('dateUsuario');
  $email = $_POST('emailUsuario');
  $password = $_POST('passwordUsuario');

  //Obtiene la longitud de un string
  $req = (strlen($Nombre)*strlen($apellido)*strlen($fechanac)*strlen($email)*strlen($password)) or die("No se han llenado todos los campos <br></br><a href='registro.html'></a>");

  //Se encritpa la contraseña
  $contrasenaUsuario = md5($password);

  //Ingresar la información a la tabla de datos
  mysql_query("INSERT INTO datos VALUES ('','$Nombre','$apellido,'$fechanac','$email','$contrasenaUsuario')",$link) or die("<h2>Error de envio</h2>");

  echo '
    <h2>Registro Completo</h2>
    <h5>Gracias por registraste en Ricos Sabores. Ahora puedes ingresar como usuario</h5>
    <a href="loguin.html">Loguearse</a>
    ';