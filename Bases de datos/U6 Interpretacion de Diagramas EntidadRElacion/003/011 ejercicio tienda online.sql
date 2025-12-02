CREATE TABLE cliente(
	id INT VARCHAR (255),
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	email VARCHAR(255)
);

CREATE TABLE pedido(
	id INT VARCHAR (255),
	cliente_id VARCHAR(255),
	fecha VARCHAR(255)
);
