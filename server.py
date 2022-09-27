from burgers_flask_app import app
from burgers_flask_app.controllers import burgers_controller


if __name__=="__main__":
    app.run(debug=True)