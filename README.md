<h1 align="center">📊 Dashboard de Ventas con Flask y MySQL</h1>

<p align="center">
  <strong>Aplicación web interactiva</strong> para visualizar y analizar datos de ventas.<br>
  Desarrollada con <b>Flask</b>, <b>MySQL</b>, <b>Chart.js</b> y <b>Bootstrap 5</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-2.3-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/Chart.js-Data%20Viz-ff6384?style=for-the-badge&logo=chartdotjs">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap">
</p>

---

🌟 Este proyecto muestra datos reales de ventas en un **gráfico dinámico y una tabla conectada directamente a MySQL**.  
Ideal para practicar integración **backend + frontend** y visualización de datos.


---

## 🚀 Características principales

<div align="center">

| 💡 Funcionalidad | 🧩 Descripción |
|------------------|----------------|
| 📊 **Gráfico dinámico** | Visualiza las ventas por producto en tiempo real usando **Chart.js**. |
| 💾 **Conexión MySQL** | Obtiene los datos directamente desde una base de datos MySQL local. |
| 🧮 **Datos estructurados** | Cada registro contiene producto, categoría, cantidad, precio y fecha. |
| 🎨 **Diseño responsivo** | Interfaz moderna desarrollada con **Bootstrap 5** para adaptarse a cualquier pantalla. |
| ⚙️ **Flask Backend** | Controlador en Python que conecta el frontend con la base de datos. |
| 🔍 **Código limpio y modular** | Arquitectura clara y fácil de mantener para futuras mejoras. |

</div>

---

## 💻 Tecnologías utilizadas

<div align="center">

| 🧩 Tecnología | 💡 Descripción | 🌐 Uso principal |
|:--------------|:----------------|:----------------|
| 🐍 **Python 3** | Lenguaje principal del proyecto | Lógica backend con Flask |
| ⚙️ **Flask** | Framework ligero para desarrollo web | Creación del servidor y rutas |
| 🧮 **MySQL** | Sistema de gestión de base de datos | Almacenamiento de ventas |
| 🎨 **Bootstrap 5** | Librería CSS responsive | Estilo y estructura visual |
| 📊 **Chart.js** | Librería JavaScript para gráficos | Visualización interactiva de datos |
| 🌤️ **HTML5 + CSS3** | Lenguajes base del frontend | Diseño y maquetación del dashboard |

</div>


---
## 🗂️ Estructura del proyecto

<div align="left">

```bash
dashboard_ventas/
│
├── 📁 static/                # Archivos estáticos (CSS, JS, imágenes)
│
├── 📁 templates/             # Plantillas HTML
│   └── index.html            # Página principal del dashboard
│
├── ⚙️ app.py                 # Archivo principal de Flask
│
├── 🧾 requirements.txt       # Librerías necesarias para el proyecto
│
└── 🧠 README.md              # Documentación del proyecto
```
</div>

---

## ⚙️ Instalación y ejecución del proyecto

Sigue estos pasos para ejecutar el **Dashboard de Ventas** en tu entorno local 🧠👇

### 🪄 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/iparra-sys/dashboard_ventas.git
cd dashboard_ventas
```
### 🧰 2️⃣ Crear y activar entorno virtual
```bash
python -m venv venv
# Activar entorno (Windows)
venv\Scripts\activate
# Activar entorno (Linux/Mac)
source venv/bin/activate

```
### 📦 3️⃣ Instalar dependencias necesarias
```bash
pip install -r requirements.txt
```
### 🗄️ 4️⃣ Configurar base de datos MySQL
1. Crear una base de datos llamada ventas_db
2. Ejecutar el script SQL incluido (db/ventas.sql) para crear la tabla y cargar los datos iniciales

### 🚀 5️⃣ Ejecutar el servidor Flask
```bash
python app.py
```
Abre el navegador y visita 👉 http://127.0.0.1:5000

---

## 🖼️ Vista previa del Dashboard

💡 A continuación puedes ver cómo se visualiza la aplicación en funcionamiento.  
El gráfico muestra las **cantidades vendidas por producto**, y la tabla presenta el detalle de las ventas almacenadas en MySQL.

<p align="center">
  <img src="https://github.com/iparra-sys/dashboard_ventas/blob/main/static/captura_dashboard.png?raw=true" alt="Vista del Dashboard de Ventas" width="80%">
</p>

---

## 🔮 Próximas actualizaciones

Estas son algunas mejoras planificadas para futuras versiones del proyecto:

- 📈 Agregar filtros dinámicos por **rango de fechas** y **categorías**.  
- 🧮 Implementar **cálculo automático de totales y promedios**.  
- 💡 Integrar **gráficos adicionales** (líneas y pastel) para comparar ventas por día.  
- 💾 Conexión con una base de datos externa para simular un entorno de producción.  
- 🧰 Optimización del diseño con **Bootstrap 5 y componentes responsivos**.

---

## 👩‍💻 Autora

**Iveth Parra Herrera**  
Desarrolladora en formación | Backend & Frontend Junior  
📍 Colombia  
🔗 [LinkedIn](https://www.linkedin.com/in/iveth-parra-herrera-351a6a235)  
💻 [GitHub](https://github.com/iparra-sys)

💡 *“El código es una herramienta para construir soluciones reales y dejar huella.”*

✨ Proyecto desarrollado como parte del Portafolio 2025 - Iveth Parra Herrera ✨


