from flask_app import app
from flask_app.controllers import controller_dojos, controller_ninjas, controller_routes
DATABASE = 'dojos_and_ninjas_schema'


if __name__=="__main__":
    app.run(debug=True)