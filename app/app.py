#clase importar flask
from flask import Flask, render_template, url_for, jsonify, redirect, request

#para poder usar la base de datos
from flask_mysqldb import MySQL

#iniciar aplicacion
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
    return render_template('index.html', data=insertObject, titulo="Página principal", nom="supermercados")
    
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

@app.route('/donar/')
def donar():
    nom = {'Titulo':'Formulario para donar'}
    return render_template('donar.html',data=nom)
#esta instruccion tiene que estar en la ultima posicion
if __name__ == '__main__':
    #ejecutar app, el debug para hacer cambios en caliente
    app.run(debug=True)
