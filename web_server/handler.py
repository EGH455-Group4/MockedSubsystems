'''Handler will showcase the web server endpoints'''
from flask import Flask, request
from flask_restful import Resource, Api

class AirQuality(Resource):
    '''Mocks the air-quality endpoint'''

    def post(self):
        '''The HTTP POST response'''
        data = request.json
        print(data)
        return {'status': 'OK'}

class Handler():
    '''Used to create the sample server'''
    def __init__(self, port: str):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.port = port

        self.api.add_resource(AirQuality, '/air-quality')

    def Run(self):
        '''Will actually run the sample server'''
        self.app.run(debug=False, port=self.port, host="0.0.0.0")
