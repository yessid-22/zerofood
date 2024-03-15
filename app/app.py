#clase importar flask
from flask import Flask, render_template, url_for, jsonify, redirect, request, flash

#para poder usar la base de datos
from flask_mysqldb import MySQL

#iniciar aplicacion __name__ nombre de la aplicacion
app = Flask(__name__)

#conexion a base de datos

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'zerofood_db'

#variable para conectarse a la base de datos
conexion = MySQL(app)

#ruta raiz
@app.route('/')
def home():    
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM supers"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    #data, titulo, nom son variavles
    nom_pag = { 'Titulo':'Página principal','super':'supermercados','Menu':('Sobre nosotros','Iniciar sesion','Registrarse')}
    return render_template('index.html', data=insertObject, nom=nom_pag)
    
#Ruta para guardar usuarios en la bdd
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
    nom_pag = {'Titulo':'Formulario para donar'}
    cursor = conexion.connection.cursor()
    sql = "SELECT productos.*, cantidad_disponible.cantidad_id FROM productos INNER JOIN cantidad_disponible ON productos.cantidad_id = cantidad_disponible.cantidad_id"
    cursor.execute(sql)
    ls_productos = cursor.fetchall()
    
    insert_product = []
    columnNames = [column[0] for column in cursor.description]
    for record in ls_productos:
        insert_product.append(dict(zip(columnNames, record)))
    cursor.close()

    return render_template('donar.html', data=insert_product, nom=nom_pag)
        
    #if request.method == 'POST':
    #    nueva_cantidad = request.form.get('cantidad')
        # Actualiza la base de datos con la nueva cantidad
        # (debes implementar esta parte según tu modelo de datos)
        # ...
    #    return "Cantidad actualizada correctamente"
    #return render_template('donar.html', nom=nom_pag)

#esta instruccion tiene que estar en la ultima posicion
# Si el programa principal esta en este script se ejecutara run()
if __name__ == '__main__':
    #ejecutar app, el debug para hacer cambios en caliente
    app.run(debug=True)
