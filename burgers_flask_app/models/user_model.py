from burgers_flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re # el módulo regex
# crea un objeto de expresión regular que usaremos más adelante
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #METODOS DE CREACION (CREATE)
    @classmethod
    def registro(cls, data):
        consulta = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())"""
        return connectToMySQL('login_reg').query_db(consulta, data)

    #METODOS DE LECTURA


    #METODOS ESTATICOS - VALIDACION
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # prueba si un campo coincide con el patrón
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['fname']) < 2:
            flash(" Por favor tu nombre debe ser mayor a 2 letras ")
            is_valid = False
        return is_valid