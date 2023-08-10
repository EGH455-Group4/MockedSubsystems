'''Handler will showcase the target detection endpoints'''
from flask import Flask, request
from flask_restful import Resource, Api, marshal

class TargetDetection(Resource):
    '''Mocks the sample POST endpoint'''

    def post(self):
        '''The HTTP GET response'''
        return {'status': 'OK'}

class Handler():
    '''Used to create the target detection server'''
    def __init__(self, port: str):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.port = port

        self.api.add_resource(TargetDetection, '/target-detection')

    def Run(self):
        '''Will actually run the target detection server'''
        self.app.run(debug=False, port=self.port, host="0.0.0.0")
