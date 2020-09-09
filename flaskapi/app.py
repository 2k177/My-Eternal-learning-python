import werkzeug
from flask import Flask
from flask_restful import fields
from flask_restplus import Api, Resource, reqparse

werkzeug.cached_property = werkzeug.utils.cached_property
APP = Flask(__name__)

API = Api(app=APP,
          version="1.0",
          title="Name Recorder",
          description = "Manage names of various users of the application")
name_space = API.namespace('main', description='Main APIs')
config_parser = reqparse.RequestParser()
config_parser.add_argument('tws_path', help='Specify TWS path', type=str, required=True)

@API.route('/autoflow/configure')
@API.expect(config_parser, validate=True)
class ExecutionConfigure(Resource):
    def get(self):
        return {
            'status': 'Success',
            'message': 'Config file updated successfully'
        }



@API.route('/my-resource/<id>', endpoint='my-resource')
@API.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @API.doc(responses={403: 'Not Authorized'})
    def post(self, id):
        API.abort(403)

@API.route("/<num>")
class MainClass(Resource):
    def get(self,num):
        return {
            "status": "Got new data"
        }
    @API.doc(param={'add': 'Number'})
    def post(self,num):
        return {
            "status": "Posted new data"
        }

if __name__ == "__main__":
    APP.run(debug=True)