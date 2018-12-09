from flask import Flask, request
from flask_restful import Resource, Api
from dataset import Dataset

app = Flask(__name__)
api = Api(app)

class Autocomplete(Resource):
    def get(self):
        if 'q' in request.args:
            names, qty = patients.find_nodes(request.args['q'])
            return { 'found': qty, 'patients': names }

class Endpoints(Resource):
    def get(self):
        return {
            'endpoints': [
                {
                    'endpoint': '/autocomplete/?q=[PARTIAL_OR_FULL_NAME]',
                    'about:': 'Lists all the names found that starts with the given text.',
                    'warning': 'For searches containing blank spaces, replace them for: "%20".',
                    'examples': [
                        'rasm',
                        'rasmus%20po'
                    ]
                },
                {
                    'endpoint': '/endpoints',
                    'about': 'Lists all available endpoints.' 
                },
                {
                    'endpoint': '/find/?q=[NAME]',
                    'about': 'Checks if the given name exists in the dataset.'
                }
            ]
        }

class Find(Resource):
    def get(self):
        if 'q' in request.args:
            return { 'found': patients.find_node(request.args['q']) }

api.add_resource(Autocomplete, '/autocomplete/')
api.add_resource(Endpoints, '/endpoints')
api.add_resource(Find, '/find/')

if __name__ == '__main__':
    dataset = Dataset()
    dataset.load('datasets/patients.csv')
    patients = dataset.as_binary_search_tree()
    app.run()