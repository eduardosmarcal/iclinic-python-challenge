import flask
import pytest

import sys
sys.path.append('../src')

from flask_restful_api import app

def test_endpoint_endpoints():
    with app.test_client() as c:
        rv = c.get('/endpoints')
        json_data = rv.get_json()
        assert json_data == {
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

def test_find():
    with app.test_request_context('/find/?q=abby bates'):
        assert flask.request.path == '/find/'
        assert flask.request.args['q'] == 'abby bates'

def test_autocomplete():
    with app.test_request_context('/autocomplete/?q=ras'):
        assert flask.request.path == '/autocomplete/'
        assert flask.request.args['q'] == 'ras'
    
    with app.test_request_context('/autocomplete/?q=rasmus po'):
        assert flask.request.path == '/autocomplete/'
        assert flask.request.args['q'] == 'rasmus po'