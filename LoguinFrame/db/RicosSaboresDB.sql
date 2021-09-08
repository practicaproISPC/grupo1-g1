--crear base de datos
create database RicosSaboresCS
use RicosSaboresDB

--crear tablas
create table NombreUsuario(
	id_usuario int primary key identity (1,1) not null,
	Usuario varchar(50) not null,
	Password varchar(50) not null
);
create table Usuarios(
	id_usuario int primary key identity (1,1) not null,
	Usuario varchar(50) not null,
	email varchar(50) not null,
	Apellido varchar(50) not null,
	Nombre varchar(50) not null,
	Apellido varchar(50) not null,
	constraint fk_Usuarios foreign key (id_usuario) references NombreUsuario (id_usuario) 
);


--procedimientos carga de usuarios
create procedure CargarUsuario
	@Usuario varchar(50)
as
	insert into NombreUsuario values (@Usuario)
go

create procedure CrearUsuario
	@Usuario varchar(50),
	@email varchar(50),
	@Nombre varchar(50),
	@Apellido varchar(50)

as
	insert into Usuarios values ( @Usuario, @email, @Nombre, @Apellido, @id_Actividad)
go
