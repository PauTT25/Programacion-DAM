'''
En este ejercicio de final de unidad tenemos que  crear y rellenar una base de datos para una biblioteca llamada biblioteca25, con cuatro tablas principales con diferentes valores, obviamente el ejercicio incluye la creación de las tablas, la definición de claves primarias y foráneas y los índices para optimizar búsquedas.
'''


CREATE DATABASE biblioteca25;                                      #Con este comando creamos la base de datos
USE biblioteca25                                                   #Con este comando entramos en la base de datos 
SELECT DABATASE();

CREATE TABLE autores(                                              #Dentro de la base de datos empezamos a crear la primera tabla, en este caso la de los autores.
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	pais  VARCHAR(80) NULL
);

DESCRIBE autores;                                                  #Aqui utilizamos este comando para que nos describa la tabla que acabamos de crear.
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0,03 sec)


CREATE TABLE libros(                                              #Creamos la segunda tabla "libros" dentro de la base de datos principal.
	id INT AUTO_INCREMENT PRIMARY KEY,
   	titulo VARCHAR(200) NOT NULL,
   	isbn VARCHAR(20) NOT NULL UNIQUE,
   	precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0),
   	autor_id INT NOT NULL,
   	INDEX idx_titulo (titulo)
);

DESCRIBE libros;                                                 #Aqui utilizamos este comando para que nos describa la tabla que acabamos de crear.
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   |     | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)

SHOW INDEX FROM libros;                                            #Utilizamos este comando para que nos muestre los apartados del indice de libros.
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table  | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| libros |          0 | PRIMARY  |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          0 | isbn     |            1 | isbn        | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
2 rows in set (0,02 sec)


CREATE TABLE socios(                                              #Creamos la tercera tabla "socios" dentro de la base de datos principal.
	id INT AUTO_INCREMENT PRIMARY KEY,
   	nombre VARCHAR(100) NOT NULL,
   	email VARCHAR(120) NOT NULL UNIQUE,
   	fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE)
);

DESCRIBE socios;                                                  #Aqui utilizamos este comando para que nos describa la tabla que acabamos de crear.
+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0,00 sec)

CREATE TABLE prestamos(                                          #Creamos la ultima tabla "prestamos" dentro de la base de datos principal.
	id INT AUTO_INCREMENT PRIMARY KEY,
   	socio_id INT NOT NULL,
   	libro_id INT NOT NULL,
   	fecha_prestamo DATE NOT NULL  DEFAULT (CURRENT_DATE),
   	fecha_devolucion DATE NULL,
);
   	ALTER TABLE prestamos
  	ADD CONSTRAINT fk_prestamos_socios
   	FOREIGN KEY (socio_id) REFERENCES socios(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE;
    
    ALTER TABLE prestamos
    ADD CONSTRAINT fk_prestamos_libros
    FOREIGN KEY (libro_id) REFERENCES libros(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT;

DESCRIBE prestamos;                                             #Aqui utilizamos este comando para que nos describa la tabla que acabamos de crear.
+------------------+------+------+-----+-----------+-------------------+
| Field            | Type | Null | Key | Default   | Extra             |
+------------------+------+------+-----+-----------+-------------------+
| id               | int  | NO   | PRI | NULL      | auto_increment    |
| socio_id         | int  | NO   | MUL | NULL      |                   |
| libro_id         | int  | NO   | MUL | NULL      |                   |
| fecha_prestamo   | date | NO   |     | curdate() | DEFAULT_GENERATED |
| fecha_devolucion | date | YES  |     | NULL      |                   |
+------------------+------+------+-----+-----------+-------------------+
5 rows in set (0,01 sec)


SHOW INDEX FROM prestamos;                                       #Utilizamos este comando para que nos muestre los apartados del indice de prestamos.
+-----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name            | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY             |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | fk_prestamos_socios |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | fk_prestamos_libros |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
3 rows in set (0,03 sec)


INSERT INTO autores (nombre) VALUES                         #Empezamos a insertar los valores de los autores dentro de la tabla.
('Isabel Allende'),
('Gabriel García Márquez'),
('Haruki Murakami');

SELECT * FROM autores                                      #Aqui comprobamos que todos los valores se hayan añadido correctamente.            
+----+--------------------------+------+ 
| id | nombre                   | pais |
+----+--------------------------+------+
|  1 | Isabel Allende           | NULL |
|  2 | Gabriel García Márquez   | NULL |
|  3 | Haruki Murakami          | NULL |
+----+--------------------------+------+
3 rows in set (0,00 sec)


INSERT INTO libros (titulo, isbn, precio, autor_id) VALUES       #Empezamos a insertar los valores de los libros dentro de la tabla.
('Isabel Allende'),
('La casa de los espíritus', '9788401352836', 20.00, 1),
('Cien años de soledad', '9780307474728', 15.00, 2),
('Kafka en la orilla', '9788499082478', 12.00, 3);

SELECT * FROM libros                                            #Aqui comprobamos que todos los valores se hayan añadido correctamente.            
+----+---------------------------+---------------+--------+----------+
| id | titulo                    | isbn          | precio | autor_id |
+----+---------------------------+---------------+--------+----------+
|  1 | La casa de los espíritus  | 9788401352836 |  20.00 |        1 |
|  2 | Cien años de soledad      | 9780307474728 |  15.00 |        2 |
|  3 | Kafka en la orilla        | 9788499082478 |  12.00 |        3 |
+----+---------------------------+---------------+--------+----------+
3 rows in set (0,00 sec)


INSERT INTO socios (nombre, email, fecha_alta) VALUES          #Empezamos a insertar los valores de los socios dentro de la tabla.
('Ana Ruiz', 'ana.ruiz@example.com', DEFAULT),
('Luis Pérez', 'luis.perez@example.com', DEFAULT);

SELECT * FROM socios                                           #Aqui comprobamos que todos los valores se hayan añadido correctamente.            
+----+-------------+------------------------+------------+
| id | nombre      | email                  | fecha_alta |
+----+-------------+------------------------+------------+
|  1 | Ana Ruiz    | ana.ruiz@example.com   | 2025-10-31 |
|  2 | Luis Pérez  | luis.perez@example.com | 2025-10-31 |
+----+-------------+------------------------+------------+
2 rows in set (0,00 sec)


INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_devolucion) VALUES    #Empezamos a insertar los valores de los prestamos dentro de la tabla.
(1,1, DEFAULT, NULL),
(2,1, DEFAULT, '2025/10/31');

SELECT * FROM prestamos                                         #Aqui comprobamos que todos los valores se hayan añadido correctamente.            

+----+----------+----------+----------------+------------------+
| id | socio_id | libro_id | fecha_prestamo | fecha_devolucion |
+----+----------+----------+----------------+------------------+
|  3 |        1 |        1 | 2025-10-31     | NULL             |
|  4 |        2 |        1 | 2025-10-31     | 2025-10-31       |
+----+----------+----------+----------------+------------------+
2 rows in set (0,00 sec)


SHOW TABLES;                                                 #Finalmente comprobamos paso por paso los diferentes apartados de la base de datos.

+------------------------+
| Tables_in_biblioteca25 |
+------------------------+
| autores                |
| libros                 |
| prestamos              |
| socios                 |
+------------------------+
4 rows in set (0,01 sec)


DESCRIBE autores;                                                #Y comprobamos que la informcion este toda correctamente en las diferentes tablas.

+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0,00 sec)


DESCRIBE libros;

+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   |     | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)


DESCRIBE socios;

+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0,00 sec)

'''
CONCLUSION
En este ejercicio podemos practicar la creación de una base de datos relacional completa, el resultado es una base de datos organizada y funcional para poder gestionar información de una biblioteca, junto con sus autores, libros, socios y préstamos.
'''






