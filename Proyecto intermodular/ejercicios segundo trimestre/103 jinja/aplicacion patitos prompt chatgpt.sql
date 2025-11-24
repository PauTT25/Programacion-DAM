/* ===========================================================
   CREACIÓN DE TABLAS BASE
   =========================================================== */

-- Categorías de patos
CREATE TABLE categorias (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Productos (patos de goma)
CREATE TABLE productos (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

-- Gestión de stock (una fila por producto)
CREATE TABLE stock (
    stock_id INT PRIMARY KEY AUTO_INCREMENT,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

-- Clientes
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    direccion VARCHAR(255)
);

-- Pedidos
CREATE TABLE pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado VARCHAR(50) DEFAULT 'Pendiente',
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

-- Líneas de pedido (productos dentro de un pedido)
CREATE TABLE lineas_pedido (
    linea_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);


/* ===========================================================
   VISTAS PARA MOSTRAR INFORMACIÓN DE FKs
   =========================================================== */

-- Vista de productos con su categoría
CREATE VIEW vista_productos AS
SELECT p.producto_id, p.nombre AS producto, p.descripcion, p.precio,
       c.nombre AS categoria
FROM productos p
LEFT JOIN categorias c ON p.categoria_id = c.categoria_id;

-- Vista de pedidos con información del cliente
CREATE VIEW vista_pedidos AS
SELECT ped.pedido_id, ped.fecha_pedido, ped.estado,
       cli.nombre AS cliente, cli.email
FROM pedidos ped
JOIN clientes cli ON ped.cliente_id = cli.cliente_id;

-- Vista de líneas de pedido detalladas
CREATE VIEW vista_lineas_pedido AS
SELECT lp.linea_id, lp.pedido_id,
       p.nombre AS producto,
       lp.cantidad,
       lp.precio_unitario,
       (lp.cantidad * lp.precio_unitario) AS subtotal
FROM lineas_pedido lp
JOIN productos p ON lp.producto_id = p.producto_id;

-- Vista general: pedidos + líneas + cliente
CREATE VIEW vista_pedido_completo AS
SELECT ped.pedido_id,
       cli.nombre AS cliente,
       p.nombre AS producto,
       lp.cantidad,
       lp.precio_unitario,
       (lp.cantidad * lp.precio_unitario) AS subtotal,
       ped.fecha_pedido,
       ped.estado
FROM pedidos ped
JOIN clientes cli ON ped.cliente_id = cli.cliente_id
JOIN lineas_pedido lp ON ped.pedido_id = lp.pedido_id
JOIN productos p ON lp.producto_id = p.producto_id;


/* ===========================================================
   INSERTS DE EJEMPLO (ordenados según FK)
   =========================================================== */

-- 1. Categorías
INSERT INTO categorias (nombre, descripcion) VALUES
('Clásicos', 'Patos de goma tradicionales'),
('Superhéroes', 'Patos inspirados en superhéroes'),
('Profesiones', 'Patos disfrazados con diferentes profesiones'),
('Edición Limitada', 'Colecciones exclusivas y especiales');

-- 2. Productos (patos)
INSERT INTO productos (nombre, descripcion, precio, categoria_id) VALUES
('Pato Amarillo Clásico', 'El pato de goma de toda la vida', 4.99, 1),
('Pato Superman', 'Pato de goma con capa y traje azul', 9.99, 2),
('Pato Bombero', 'Pato con casco y traje de bombero', 7.50, 3),
('Pato Edición Dragón Rojo', 'Pato edición limitada tipo dragón', 14.99, 4);

-- 3. Stock
INSERT INTO stock (producto_id, cantidad) VALUES
(1, 100),
(2, 50),
(3, 70),
(4, 20);

-- 4. Clientes
INSERT INTO clientes (nombre, email, direccion) VALUES
('Juan Pérez', 'juan@example.com', 'Calle Falsa 123'),
('María López', 'maria@example.com', 'Av. del Pato 45'),
('Carlos Ruiz', 'carlos@example.com', 'C/ Río Amarillo 78');

-- 5. Pedidos
INSERT INTO pedidos (cliente_id, fecha_pedido, estado) VALUES
(1, '2025-01-10', 'Pendiente'),
(2, '2025-01-12', 'Enviado');

-- 6. Líneas de Pedido
INSERT INTO lineas_pedido (pedido_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 2, 4.99),
(1, 3, 1, 7.50),
(2, 2, 1, 9.99),
(2, 4, 1, 14.99);


