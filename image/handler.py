'''Handler will showcase the image processing endpoints'''
import os, random

from flask import Flask, send_file
from flask_restful import Resource, Api

class CurrentImage(Resource):
    '''Mocks the image endpoint'''

    def post(self):
        '''The HTTP POST response'''
        choice = random.choice(os.listdir("./image/images"))
        return send_file("./images/"+choice, mimetype="image/jpg")

class Handler():
    '''Used to create the image processing server'''
    def __init__(self, port: str):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.port = port

        self.api.add_resource(CurrentImage, '/image')

    def Run(self):
        '''Will actually run the target detection server'''
        self.app.run(debug=False, port=self.port, host="0.0.0.0")
