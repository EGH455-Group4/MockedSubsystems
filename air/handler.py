'''Handler will showcase the Air Quality endpoints'''
import logging
from flask import Flask, request
from flask_restful import Resource, Api

from air.helper import ACCEPTABLE_LCD_DISPLAYS

class LcdScreen(Resource):
    '''Used to alter the LCD screen on the sensor'''

    def post(self):
        '''The HTTP POST response'''
        json_data = request.get_json(force=True)

        display_option = json_data['display']

        if display_option not in ACCEPTABLE_LCD_DISPLAYS:
            return {'status': 'NOT_AN_OPTION'}, 400

        return {'status': 'OK'}

class Handler():
    '''Used to create the air quality server'''
    def __init__(self, port: str):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.port = port

        self.api.add_resource(LcdScreen, '/lcd-screen')

        logging.info("Handler was setup.")

    def Run(self):
        '''Will actually run the air quality server'''
        self.app.run(debug=False, port=self.port, host="0.0.0.0")
