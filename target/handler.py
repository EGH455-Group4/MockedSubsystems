'''Handler will showcase the target detection endpoints'''
import os, random

from flask import Flask, send_file
from flask_restful import Resource, Api

class TargetDetection(Resource):
    '''Mocks the sample POST endpoint'''

    def post(self):
        '''The HTTP GET response'''
        choice = random.choice(os.listdir("./target/images"))
        return send_file("./images/"+choice, mimetype="image/jpg")

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
