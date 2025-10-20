CREATE DATABASE IF NOT EXISTS dashboard_ventas_db;
USE dashboard_ventas_db;

CREATE TABLE IF NOT EXISTS ventas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  producto VARCHAR(100) NOT NULL,
  categoria VARCHAR(50),
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  fecha DATE NOT NULL
);


