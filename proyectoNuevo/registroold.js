var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var fechanac = document.getElementById('fechanac');
var email = document.getElementById('email');
var password = document.getElementById('password');
var error = document.getElementById('error');
error.style.color = 'red';

var form = document.getElementById ('formulario');
    form.addEventListener('submit', function(evt){
        evt.preventDefault();
        var mensajesError = [];
        if (nombre.value === null || nombre.value === ''){
            mensajesError.push('Ingrese tu Nombre');
        }
        if (apellido.value === null || apellido.value === ''){
            mensajesError.push('Ingrese tu apellido');
        }
        if (fechanac.value === null || fechanac.value === ''){
            mensajesError.push('Ingrese tu Fecha de Nacimiento');
        }
        if (email.value === null || email.value === ''){
            mensajesError.push('Ingrese tu email');
        }
        if (password.value === null || password.value === ''){
            mensajesError.push('Ingrese tu contraseña');
            
        }
        if (password2.value === null || password2.value === ''){
            mensajesError.push('Repite tu contraseña');
            
        }
        if (password2.value != password){
            mensajesError.push('Las contraseñas no coinciden');
        }
    
        error.innerHTML = mensajesError.join(', ');
    });