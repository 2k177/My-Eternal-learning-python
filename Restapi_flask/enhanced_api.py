from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
# api = Api(app=app,
#           version="1.0",
#           title="Movie tub",
#           description="Manage movies information")
# movie_api = api.namespace('Movie tub', description='Contains the movies information')

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
initialize_routes(api)


# app.register_blueprint(movies)

if __name__ == '__main__':
    app.debug = True
    app.run(port=7000)