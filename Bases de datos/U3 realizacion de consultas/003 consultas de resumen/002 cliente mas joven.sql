-- sudo mysql -u root -p

--Entramos a la base de datos
USE clientes;

--Nos numera el numero de los clientes que tenemos
SELECT 
	nombre, 
	apellidos, 
	edad
FROM clientes
ORDER BY edad ASC;		--Con esto ordenamos a los clientes por edad de manera ascendente
LIMIT 1;
