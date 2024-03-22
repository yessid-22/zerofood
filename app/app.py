# Clase importar flask
from flask import Flask, render_template, url_for, jsonify, redirect, request, flash, session

# Para poder usar la base de datos
from flask_mysqldb import MySQL

# Iniciar aplicacion __name__ nombre de la aplicacion
app = Flask(__name__)

# Configuración de la clave secreta
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Conexion a base de datos

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'zerofood_db'

# Variable para conectarse a la base de datos
conexion = MySQL(app)

# Ruta raiz
@app.route('/')
def home():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM supers"
        cursor.execute(sql)
        ls_supers = cursor.fetchall()
        cursor.close()
    except Exception as e:
        # Mensaje de error
        print(f"Error al conectar con la base de datos: {e}")
    
        nom_pag = { 'Titulo':'Página principal','super':'supermercados','Menu':('Sobre nosotros','Iniciar sesion','Registrarse')}        
        mensaje = "No se pudo conectar con la base de datos. Por favor, intente más tarde."
        # Variables para jinja2
        return render_template('index.html', mensaje=mensaje, nom=nom_pag)
    
    # Verificar si ls_supers está vacío
    if not ls_supers:
        mensaje = "No hay datos disponibles."
        nom_pag = { 'Titulo':'Página principal','super':'supermercados','Menu':('Sobre nosotros','Iniciar sesion','Registrarse')}
        return render_template('index.html', mensaje=mensaje, nom=nom_pag)
    else:
        nom_pag = { 'Titulo':'Página principal','super':'supermercados','Menu':('Sobre nosotros','Iniciar sesion','Registrarse')}
        return render_template('index.html', supers=ls_supers, nom=nom_pag)

    #return render_template('index.html', supers=ls_supers, nom=nom_pag)
    
# Ruta para guardar usuarios en la bdd
@app.route('/', methods=['POST'])
def addUser():
    username = request.form['username']
    name = request.form['nom_user']
    password = request.form['password']

   # if username and name and password:
   #     cursor = conexion.connection.cursor()
   #     sql = "INSERT INTO users (username, nom_user, password) VALUES (%s, %s, %s)"
   #     data = (username, nom_user, password)
   #     cursor.execute(sql, data)
   #     conexion.commit()
    return render_template('login.html')
@app.route('/delete/<string:id>')
def delete(id):
    cursor = conexion.connection.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    conexion.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = conexion.connection.cursor()
        sql = "UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s"
        data = (username, name, password, id)
        cursor.execute(sql, data)
        conexion.commit()    
    return redirect(url_for('home'))

@app.route('/donar', methods=['POST','GET'])
def donar():
    # Diccionario nombre pagina, pestaña
    nom_pag = {'Titulo':'Formulario para donar'}
    # Si el metodo es POST
    if request.method == 'POST':
        # Obtener el id_producto y cantidad
        id_producto = request.form.get('id_producto')
        nueva_cantidad = request.form.get('cantidad')
        # Actualizar la cantidad del producto
        try:
            cursor = conexion.connection.cursor()
            # Suponiendo que tienes una columna para la cantidad total donada en tu tabla de productos
            sql = """
                    UPDATE cantidades cd
                        INNER JOIN productos p ON cd.id_producto = p.id_producto 
                    SET cd.cantidad = cd.cantidad + %s 
                        WHERE p.id_producto = %s
            """
            cursor.execute(sql, (nueva_cantidad, id_producto))
            # Confirmar la transacción y guardar
            conexion.connection.commit()
            # Cerrar el cursor
            cursor.close()
            # Mensaje de exito
            flash('Donación realizada con éxito', 'success')
        except Exception as e:
            # Mensaje de error
            flash(f'Error al realizar la donación: {e}', 'danger')
        return redirect(url_for('donar'))

    # Hacer la conexion a base de datos
    cursor = conexion.connection.cursor()
    # Consulta con join de dos tablas para hacer la lista de productos con su cantidad
    sql = """SELECT 
                p.*, 
                c.cantidad
            FROM productos p
            INNER JOIN cantidades c ON p.id_producto = c.id_producto"""
    # Ejecutar la consulta
    cursor.execute(sql)
    # Poner en una lista
    ls_productos = cursor.fetchall()
    cursor.close()
    # Variables para jinja2
    return render_template('donar.html', productos=ls_productos, nom=nom_pag)
# Si el programa principal esta en este script se ejecutara run()
if __name__ == '__main__':
    #ejecutar app, el debug para hacer cambios en caliente
    app.run(debug=True)
