from burgers_flask_app.models.user_model import User
from burgers_flask_app import app
from flask import render_template, redirect, request, session

# RUTAS DE LECTURA (READ)
@app.route('/')
def raiz():
    return render_template('login_reg.html')

# RUTAS DE CREACION (CREATE)
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    #validar si el correo electronico cumple con un patron especifico
    if not User.validate_user(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
    data={
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
        'password': request.form['psw']
    }
    print(data, "EFECTIVAMENTE ATRAPAMOS LA INFO DEL FORMULARIO")
    id_usuario = User.registro(data) # Llamar al metodo registro de la clase usuario para guardar info en la bd
    print(id_usuario, "QUE RETORNO EL HABER REGISTRADO UN USUARIO NUEVO?")
    session['id_usuario'] = id_usuario #Estoy almacenando el id del usuario en la session
    return redirect('/burger')


@app.route('/clearsession')
def limpiar_session():
    session.clear()
    return redirect('/')