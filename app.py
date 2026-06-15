from flask import Flask
import psycopg2

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def inicio():
    try:
        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )

        cursor = conexion.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        cursor.close()
        conexion.close()

        return f"""
        <h1>Aplicación Flask</h1>
        <h2>Versión {VERSION}</h2>
        <p>Conexión exitosa a PostgreSQL</p>
        <p>{version}</p>
        <h3>Sistema funcionando correctamente</h3>
        """

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)