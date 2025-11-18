--- Le pedimos que nos muestre todos los usuarios que hay en el sistema. ---
SELECT User, Host FROM mysql.user;

+------------------+-------------+
| User             | Host        |
+------------------+-------------+
| debian-sys-maint | localhost   |
| empresadam       | localhost   |
| mysql.infoschema | localhost   |
| mysql.session    | localhost   |
| mysql.sys        | localhost   |
| portafolioceac   | localhost   |
| root             | localhost   |
| [Pau]            | [localhost] |
+------------------+-------------+
8 rows in set (0,00 sec)

--- Creamos un nuevo usuario con su respectiva contraseña. ---
CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'Contraseña123$';

--- Permitimos el acceso al usuario. ---
GRANT USAGE ON *.* TO 'nuevo_usuario'@'localhost';

--- Quitamos todos los límites del usuario. ---
ALTER USER 'nuevo_usuario'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

--- Le damos acceso a una base de datos específica. ---
GRANT ALL PRIVILEGES ON empresadam.* TO 'nuevo_usuario'@'localhost';

--- Recargamos la tabla de los privilegios. ---
FLUSH PRIVILEGES;

--- Le volvemos a pedir que nos muestre todos los usuarios para confirmar que se a añadido el usuario nuevo. ---
SELECT User, Host FROM mysql.user;

+------------------+-------------+
| User             | Host        |
+------------------+-------------+
| debian-sys-maint | localhost   |
| empresadam       | localhost   |
| mysql.infoschema | localhost   |
| mysql.session    | localhost   |
| mysql.sys        | localhost   |
| nuevo_usuario    | localhost   |
| portafolioceac   | localhost   |
| root             | localhost   |
| [Pau]            | [localhost] |
+------------------+-------------+
9 rows in set (0,00 sec)

