--- Iniciamos MySQL para hacer el ejercicio. ---
sudo mysql -u root -p

--- Le pedimos que nos muestre las bases de datos. ---
SHOW DATABASES;

--- Seleccionamos la base de datos. ---
use ejerciciosrepaso;

--- Creamos la primera tabla de personas. ---
CREATE TABLE personas(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(40),
	apellidos VARCHAR(40)
);

--- Insertamos dentro de la tabla los diferentes valores que nos dicen. ---
INSERT INTO personas VALUES(
   NULL,
  'Pau',
  'Contreras Romero'
);

INSERT INTO personas VALUES(
   NULL,
  'Jose',
  'Garcia Molina'
);

INSERT INTO personas VALUES(
   NULL,
  'Alba',
  'Muñoz Villar'
);

--- Creamos la segunda tabla de emails. ---
CREATE TABLE emails(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	direccion VARCHAR(40),
	persona VARCHAR(40)
);

--- Insertamos dentro de la tabla los diferentes valores que nos dicen. ---
INSERT INTO emails (direccion, persona) VALUES
	('pau@gmail.com', 'Pau'),
	('jose@gmail.com', 'Jose'),
	('alba@gmail.com', 'Alba');

--- Realizamos la peticion cruzada entre las tablas 
SELECT emails.direccion, emails.persona, personas.nombre
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

+----------------+---------+--------+
| direccion      | persona | nombre |
+----------------+---------+--------+
| pau@gmail.com  | Pau     | NULL   |
| jose@gmail.com | Jose    | NULL   |
| alba@gmail.com | Alba    | NULL   |
+----------------+---------+--------+
3 rows in set (0,00 sec)


