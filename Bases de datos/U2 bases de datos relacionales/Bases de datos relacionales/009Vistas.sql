--- Iniciamos MySQL para hacer el ejercicio. ---
sudo MySQL -u root -p

--- Le pedimos que cree una vista para que combine la informacion de las dos tablas. ---
CREATE VIEW personas_correos AS
SELECT 
    personas.identificador,
    emails.direccion,
    personas.nombre,
    personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

--- Le decimos que nos muestre la tabla para consultar la informacion. ---
SELECT * FROM personas_correos;

+---------------+----------------+--------+-----------+
| identificador | direccion      | nombre | apellidos |
+---------------+----------------+--------+-----------+
|          NULL | pau@gmail.com  | NULL   | NULL      |
|          NULL | jose@gmail.com | NULL   | NULL      |
|          NULL | alba@gmail.com | NULL   | NULL      |
+---------------+----------------+--------+-----------+
3 rows in set (0,01 sec)

