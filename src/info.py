from flask_restful import Resource


class Info(Resource):
    def get(self):
        return {'Parameters':
                    {'startDate': 'startDate',
                     'endDate': 'endDate',
                     'Type': ('cumulative', 'usual'),
                     'Grouping': ('weekly', 'bi-weekly', 'monthly'),
                     'Filters': ('attributes', 'values'), }
                }, 200
