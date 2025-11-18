'''
Para instalar MySQL, primero se descarga desde su página oficial y se ejecuta el instalador. Durante la instalación se configuran el usuario root, la contraseña y los puertos de conexión. Una vez completado, se puede acceder a MySQL desde la consola o herramientas como MySQL Workbench para administrar bases de datos.
'''

CREATE TABLE empleados(                         #Aqui hemos utilizado este comando para poder crear la nueva tabla y                                                                                        añadir la informacion.
	ID VARCHAR (20),
	NOMBRE VARCHAR (50),
	APELLIDOS VARCHAR (50),
	EMAIL VARCHAR(255)
);

INSERT INTO empleados VALUES(              #Empezamos a insertar los datos de los nuevos clientes para las diferentes celdas.
	'56782124Y',
	'Oscar',
	'Camps',
	'pepeg@gmail.com'
);

INSERT INTO empleados VALUES(
	'34598535H',
	'Seguismundo',
	'Barriga',
	'carlosg@gmail.com'
);

'''
CONCLUSION
En este ejercicio se puede entender cómo instalar, configurar y utilizar MySQL para crear bases de datos relacionales. Este conocimiento será útil para futuros proyectos y poder gestionar información de forma organizada, segura y eficiente.
'''
