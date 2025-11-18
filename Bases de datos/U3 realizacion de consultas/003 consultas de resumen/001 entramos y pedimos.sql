-- sudo mysql -u root -p

--Entramos a la base de datos
USE clientes;

--Nos numera el numero de los clientes que tenemos
SELECT COUNT(nombre)
FROM clientes;
