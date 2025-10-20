# 📊 Dashboard de Ventas con Flask y MySQL

Aplicación web que muestra un **panel interactivo de ventas** con gráficos dinámicos generados a partir de datos reales en MySQL.  
El dashboard permite visualizar tendencias, categorías y cantidades vendidas de manera clara y profesional.

---

## 🚀 Características Principales

- Conexión directa a base de datos **MySQL**
- Visualización de datos mediante **Chart.js**
- Gráficos de **barras, líneas y pastel**
- Diseño responsivo con **Bootstrap 5**
- Estructura escalable y organizada con **Flask**

---

## 🛠️ Tecnologías Utilizadas

| Categoría | Herramientas |
|------------|---------------|
| Backend | Flask (Python) |
| Base de Datos | MySQL |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Visualización | Chart.js |
| Otros | Jinja2, Flask-MySQL Connector |

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/iparra-sys/dashboard_ventas.git
cd dashboard_ventas
```
### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ Configurar la base de datos MySQL
En tu servidor MySQL, crea la base y tabla:
```bash
CREATE DATABASE dashboard_ventas;
USE dashboard_ventas;

CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    fecha DATE NOT NULL
);

INSERT INTO ventas (producto, categoria, cantidad, precio_unitario, fecha) VALUES
('Pan', 'Alimentos', 30, 1500, '2025-10-01'),
('Leche', 'Bebidas', 20, 2500, '2025-10-02'),
('Queso', 'Lácteos', 15, 5000, '2025-10-02'),
('Arroz', 'Alimentos', 40, 3200, '2025-10-03'),
('Café', 'Bebidas', 25, 4500, '2025-10-03');
```
### 4️⃣ Ejecutar el servidor Flask
```bash
python app.py
```
Abre el navegador y visita 👉 http://127.0.0.1:5000

---


📸 Ejemplos Visuales

Vista Principal	 Gráfico de Barras

	
Gráfico de Líneas	Gráfico de Pastel


---


🔮 Próximas Actualizaciones

Filtros por fecha y categoría
Exportación de datos a CSV
Reporte de ventas mensual automatizado
Integración con API REST

---

👩‍💻 Autora

Iveth Parra Herrera
📎 LinkedIn

📧 Contacto: iparra-sys

💡 “El código es una herramienta para construir soluciones reales y dejar huella.”

✨ Proyecto desarrollado como parte del Portafolio 2025 - Iveth Parra Herrera ✨

