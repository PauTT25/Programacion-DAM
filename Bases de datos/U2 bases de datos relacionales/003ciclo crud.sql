-- create
INSERT INTO clientes VALUES(
  NULL,
  "Pau",
  "Contreras Romero",
  "pepe@gmail.com")
;
-- read
SELECT * FROM clientes;
--- update
UPDATE clientes
SET email = "pep@gmail.com"
WHERE Identificador = 1;
-- delete
DELETE FROM clientes
WHERE Identificador = 1;
