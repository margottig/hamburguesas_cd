# necesitaremos importar burger.py para acceder a la clase
from burgers_flask_app.models import burger_model
from burgers_flask_app.config.mysqlconnection import connectToMySQL

class Topping:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.topping_name = db_data['topping_name']
        # necesitamos tener una lista en caso de que queramos mostrar qué hamburguesas están relacionadas con el aderezo
        self.on_burgers = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    # METODOS DE ESCRITURA/CREACION    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO toppings ( topping_name, created_at , updated_at ) VALUES (%(topping_one)s,NOW(),NOW());"
        return connectToMySQL('login_reg').query_db(query, data)
        # este método recuperará el aderezo específico junto con todas las hamburguesas asociadas a él
    
    @classmethod
    def agregar_topping_a_hamburguesa(cls, data):
        query = "INSERT INTO add_ons ( topping_id, burger_id) VALUES (%(id_topping)s, %(id_hamburguesa)s);"
        return connectToMySQL('login_reg').query_db(query, data)


    #METODOS DE LECTURA
    @classmethod
    def get_topping_with_burgers( cls , data ):
        query = "SELECT * FROM toppings LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
        results = connectToMySQL('login_reg').query_db( query , data )
        # los resultados serán una lista de objetos topping (aderezo) con la hamburguesa adjunta a cada fila 
        topping = cls( results[0] )
        for row_from_db in results:
            # ahora parseamos los datos topping para crear instancias de aderezos y agregarlas a nuestra lista
           burger_data = {
               "id" : row_from_db["burgers.id"],
               "name" : row_from_db["name"],
               "bun" : row_from_db["bun"],
               "calories" : row_from_db["calories"],
               "created_at" : row_from_db["toppings.created_at"],
               "updated_at" : row_from_db["toppings.updated_at"]
           }
           topping.on_burgers.append(burger_model.Burger( burger_data ) )
        return topping

