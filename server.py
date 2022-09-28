from burgers_flask_app import app
from burgers_flask_app.controllers import burgers_controller, users_controller
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)