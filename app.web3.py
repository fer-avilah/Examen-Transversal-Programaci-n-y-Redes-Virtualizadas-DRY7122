from flask import Flask, request
import sqlite3
import hashlib

# Crear base de datos y tabla si no existen
def crear_base_datos():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insertar usuarios con contraseñas hasheadas
def insertar_usuarios():
    usuarios = {
        "Fernanda": "examen123",
        "Carlos": "examen012",
        "Nicolas": "examen234"
    }

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    for nombre, clave in usuarios.items():
        hash_clave = hashlib.sha256(clave.encode()).hexdigest()
        cursor.execute("INSERT INTO usuarios (nombre, hash) VALUES (?, ?)", (nombre, hash_clave))
    conn.commit()
    conn.close()

# Iniciar la aplicación Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h2>Validación de Usuario - Examen Transversal</h2>
    <form method="POST" action="/login">
        Usuario: <input type="text" name="usuario"><br>
        Contraseña: <input type="password" name="clave"><br>
        <input type="submit" value="Ingresar">
    </form>
    '''

@app.route("/login", methods=["POST"])
def login():
    nombre = request.form.get("usuario")
    clave = request.form.get("clave")
    hash_clave = hashlib.sha256(clave.encode()).hexdigest()

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND hash=?", (nombre, hash_clave))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return f"<h3>✅ Bienvenido/a, {nombre}</h3>"
    else:
        return "<h3>❌ Usuario o clave incorrecta</h3>"

# Ejecutar todo
if __name__ == "__main__":
    crear_base_datos()
    insertar_usuarios()
    app.run(host="0.0.0.0", port=5800)
