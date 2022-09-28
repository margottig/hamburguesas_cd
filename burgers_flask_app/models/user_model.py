from burgers_flask_app.config.mysqlconnection import connectToMySQL

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
