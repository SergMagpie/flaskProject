from flask import request
from flask_restful import Resource
from src import api


class Info(Resource):
    def get(self):
        return {'Parameters':
                    {'startDate': 'startDate',
                     'endDate': 'endDate',
                     'Type': ('cumulative', 'usual'),
                     'Grouping': ('weekly', 'bi-weekly', 'monthly'),
                     'Filters': ('attributes', 'values'), }
                }, 200

class Timeline(Resource):
    def get(self):
        args = request.args
        return {'Parameters':
                    {'startDate': 'startDate',
                     'endDate': 'endDate',
                     'Type': ('cumulative', 'usual'),
                     'Grouping': ('weekly', 'bi-weekly', 'monthly'),
                     'Filters': ('attributes', 'values'), }
                }, 200

api.add_resource(Info, '/api/info', strict_slashes=False)
api.add_resource(Timeline, '/api/timeline', strict_slashes=False)
