from burgers_flask_app.models.user_model import User
from burgers_flask_app import app
from flask import render_template, redirect, request

# RUTAS DE LECTURA (READ)
@app.route('/')
def raiz():
    return render_template('login_reg.html')

# RUTAS DE CREACION (CREATE)
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data={
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
        'password': request.form['psw']
    }
    print(data, "EFECTIVAMENTE ATRAPAMOS LA INFO DEL FORMULARIO")
    User.registro(data) # Llamar al metodo registro de la clase usuario para guardar info en la bd
    return redirect('/burger')