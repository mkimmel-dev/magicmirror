import flask
from flask import request, jsonify
from flask_restx import Api, Resource, fields, reqparse
import json
import magmodules

app = flask.Flask(__name__)
app.config['DEBUG'] = True

api = Api(app = app,
          version = '1.0',
          title = 'MagicMirrorAPI',
          description = "API that runs the magic mirror")
ns = api.namespace('api', description = 'API to run magic mirror')




@ns.route('/home', methods = ['GET'])
class homepage(Resource):
    def get(self):

        print('home')


@ns.route('/modules/compliments', methods = ['GET'])
class moduleCompliments(Resource):
    def get(self):
        return jsonify(magmodules.get_compliment())

@ns.route('/modules/weather', methods = ['GET'])
class moduleWeather(Resource):
    def get(self):
        return jsonify(magmodules.get_weather())

@ns.route('/modules/forecast', methods = ['GET'])
class moduleForecast(Resource):
    def get(self):
        return jsonify(magmodules.get_forecast())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 1407, threaded = True)
