-Iniciando sesion en MySQL:
sudo mysql -u root -p

-Creamos la base de datos:
CREATE DATABASE simulacro;

-Hacemos la comprobacion de que se haya creado correctamente:
SH0W DATABASES;

-Usamos la base de datos:
USE simulacro;

-Creamos una tabla:
CREATE TABLE autores(
    identificador INT(10) AUTO_INCREMENT PRIMARI KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);


-Miramos que la hemos creado bien
SHOW TABLES;


-Quiero tirar la columna Identificador para crearla bien
ALTER TABLE autores DROP Identificador;


-Ahora creo columna
ALTER TABLE autores ADD COLUMN Identificador INT
auto_increment PRIMARI KEY FIRTS;


-Vamos a ver que es lo que se ha hecho
DESCRIBE autores;


-Ahora quiero insertar un autor de prueba:
INSERT INTO autores VALUES(
    'Pau',
    'Contreras Romero, 
    'prueba@gmail.com'
);


-Nos aseguramos de que lo hemos hecho bien:
SELECT* FROM autores;


-Creamos una tabla:
CREATE TABLE entradas(
    identificador INT(100) INT AUTO_INCREMENT,
    titulo VARCHAR(100),
    fecha VARCHAR(100),
    imagen VARCHAR(100)
    id_autor VARCHAR(100),
    contenido TEXT,
    PRIMARI KEY (Identificador)
);


-Volvemos a comprobar que lo hayamos hecho bien:
SHOW TABLES;

-Describimos:
DESCRIBE entradas;


-Creamos una foreing key:
ALTER TABLE entradas
ADD CONSTRAINT autores_a_entradas
FOREIGN KEY (id_autor)
REFERENCES autores(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;


-Cambiamos tipo de datos:
ALTER TABLE entradas
MODIFY COLUMN id_autor INT;         #Aqui hemos utilizado MODIFY COLUMN para cambiar el valor de id_autor de VARCHAR a INT.


-Insertamos una entrada:
INSERT INTO entradas VALUES(
    NULL,
    'Titulo de la primera entrada',
    '2025-11-03',
    'imagen.jpg',                                   #Dato textual siempre comillas (VARCHAR)
    1,                                              #Dato numerico siempre sin comillas
    'Este es el contenido de la primera entrada'
);
SELECT * FROM entradas;


Peticion para unir las dos tablas antes de crear la view:
SELECT
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido,
autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;


-Por ultimo creamos una vista: 
CREATE VIEW vista_entradas AS
SELECT
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido,
autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;

SELECT * FROM vista_entradas;











