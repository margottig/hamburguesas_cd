from burgers_flask_app.models.burger_model import Burger
from burgers_flask_app.models.topping_model import Topping
from burgers_flask_app import app
from flask import render_template, redirect, request, session

@app.route('/burger')
def index():
    # validar si el usaurio se encuentra registrado
    if 'id_usuario' not in session:
        return redirect('/')
    return render_template("index.html")

@app.route('/create',methods=['POST'])
def create():
    # si hay errores:
    # llamamos al método estático en el modelo Burger para validar
    if not Burger.validate_burger(request.form):
        # redirigir a la ruta donde se renderiza el formulario de burger
        return redirect('/burger')
    # de lo contrario, no hay errores:
    data = {

        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "user_id":request.form['id_usuario']
    }
    Burger.save(data)
    return redirect('/burgers')


@app.route('/burgers')
def burgers():
        # validar si el usaurio se encuentra registrado
    if 'id_usuario' not in session:
        return redirect('/')
    return render_template("results.html",all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html",burger=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    # diccionario para modelo hamburguesa
    data_hamburguesa = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],

    }
    # diccionario para modelo hamburguesa
    data_topping={
        "burguer_id":request.form['burger_id'],
        "topping_one":request.form['topping_one']
    }
    Burger.update(data_hamburguesa)
    id_toppping = Topping.save(data_topping)
    data_muchos_muchos = {
        'id_topping':id_toppping,
        'id_hamburguesa':burger_id
    }
    Topping.agregar_topping_a_hamburguesa(data_muchos_muchos)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')