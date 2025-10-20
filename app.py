from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# 🔌 Conexión a MySQL
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="iveth_user",        # Cambia si tu usuario es distinto
        password="Angel1308.",        # Si tienes contraseña, escríbela aquí
        database="dashboard_ventas_db"
    )

@app.route('/')
def index():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ventas")
    ventas = cursor.fetchall()
    conexion.close()

    return render_template("index.html", ventas=ventas)

if __name__ == '__main__':
    app.run(debug=True)
