'''Handler will showcase the Sample endpoints'''
from flask import Flask
from flask_restful import Resource, Api

class Sample(Resource):
    '''Mocks the sample POST endpoint'''

    def post(self):
        '''The HTTP GET response'''
        return {'status': 'OK'}

class Handler():
    '''Used to create the sample server'''
    def __init__(self, port: str):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.port = port

        self.api.add_resource(Sample, '/sample')

    def Run(self):
        '''Will actually run the sample server'''
        self.app.run(debug=False, port=self.port, host="0.0.0.0")
