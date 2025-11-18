'''
En este ejercicio de final de unidad tenemos que  crear y rellenar una base de datos para una biblioteca llamada portafolio, con dos tablas principales con diferentes valores, obviamente el ejercicio incluye la creación de las tablas, la definición de claves primarias y foráneas y los índices para optimizar búsquedas.
'''

-Iniciando sesion en MySQL:
sudo mysql -u root -p

-Creamos la base de datos:
CREATE DATABASE portafolio;

-Usamos la base de datos:
USE portafolio

SELECT DATABASE();

-Creamos una tabla:
CREATE TABLE pieza(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	titulo varchar (100),
	descripcion varchar (100),
	imagen varchar (100),
	url varchar (100),
	id_categoria INT
); 	
-Añadimos una columna 
ALTER TABLE pieza ADD COLUMN id_categoria INT

-Creamos la segunda tabla:
CREATE TABLE categoria(
	identificador INT (40) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR (100),
	descripcion VARCHAR (100)
);
	
-Miramos que la hemos creado bien
SHOW TABLES;

+----------------------+
| Tables_in_portafolio |
+----------------------+
| categoria            |
| pieza                |
+----------------------+
2 rows in set (0,00 sec)

-Creamos una foreing key:
ALTER TABLE pieza
ADD CONSTRAINT pieza_a_categoria
FOREIGN KEY (id_categoria)
REFERENCES categoria(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

-Insertamos los valores:
INSERT INTO pieza (Identificador, titulo, descripcion, imagen, url) VALUES(
	NULL,
	'Pieza roja',
	'La pieza es roja',
	'imagen.png',
	'piezas.com/diferentes-piezas'	
);

SELECT * FROM pieza;
+---------------+------------+------------------+------------+------------------------------+--------------+
| identificador | titulo     | descripcion      | imagen     | url                          | id_categoria |
+---------------+------------+------------------+------------+------------------------------+--------------+
|             1 | Pieza roja | La pieza es roja | imagen.png | piezas.com/diferentes-piezas |         NULL |
+---------------+------------+------------------+------------+------------------------------+--------------+
1 row in set (0,00 sec)


Peticion para unir las dos tablas antes de crear la view:

SELECT
pieza.titulo,pieza.descripcion,pieza.imagen,pieza.url,
categoria.titulo,categoria.descripcion
FROM pieza
LEFT JOIN categoria
ON pieza.id_categoria = categoria.Identificador;


-Por ultimo creamos una vista:
CREATE VIEW vista_pieza AS
SELECT
  pieza.titulo AS titulo_pieza,
  pieza.descripcion AS descripcion_pieza,
  pieza.imagen,
  pieza.url,
  categoria.titulo AS titulo_categoria,
  categoria.descripcion AS descripcion_categoria
FROM pieza
LEFT JOIN categoria
ON pieza.id_categoria = categoria.Identificador;

SELECT * FROM vista_pieza;

+--------------+-------------------+------------+------------------------------+------------------+-----------------------+
| titulo_pieza | descripcion_pieza | imagen     | url                          | titulo_categoria | descripcion_categoria |
+--------------+-------------------+------------+------------------------------+------------------+-----------------------+
| Pieza roja   | La pieza es roja  | imagen.png | piezas.com/diferentes-piezas | NULL             | NULL                  |
+--------------+-------------------+------------+------------------------------+------------------+-----------------------+
1 row in set (0,01 sec)

-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'portafolioceac'@'localhost' 
IDENTIFIED  BY 'Simulacro123$';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolioceac'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'portafolioceac'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON portafolio.* TO 'portafolioceac'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;

'''
CONCLUSION
En este ejercicio podemos practicar la creación de una base de datos relacional completa, el resultado es una base de datos organizada y funcional para poder gestionar información de una pagina web, junto con sus piezas, descripciones, imagenes y sus url.
'''

	
