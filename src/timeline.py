from flask import request
from flask_restful import Resource
from src import db


class Timeline(Resource):
    def get(self):
        args = request.args.to_dict()
        try:
            events = self.get_results(**args)
            return events, 200
        except:
            return {'message': 'Bad Request'}, 400

    def get_results(self,
                    startDate,
                    endDate,
                    Type,
                    Grouping,
                    **args):
        if args:
            args_str = ' and ' + ' and '.join(["%s = '%s'" % (arg, args[arg]) for arg in args])
            args_select = ', ' + ', '.join(["%s" % arg for arg in args])
        else:
            args_str = args_select = ''
        periods = {'weekly': 'strftime("%W", timestamp)',
                   'bi-weekly': 'strftime("%W", timestamp) / 2',
                   'monthly': 'strftime("%m", timestamp)'
                   }
        period = periods[Grouping]
        with db.engine.connect() as con:
            res = con.execute('''
                SELECT count(id_code), date(timestamp) AS date_time, %s AS grouper, strftime("%%Y", timestamp) AS date_year %s
                FROM events
                WHERE date_time between '%s' and '%s' %s
                GROUP BY date_year, grouper
                ORDER BY date_time;
                ''' % (period, args_select, startDate, endDate, args_str))
            rez = res.fetchall()
        if Type == 'cumulative':
            x = 0
            return {'timeline': [{'date': d, 'value': (x := x + c)} for c, d, *_ in rez]}
        elif Type == 'usual':
            return {'timeline': [{'date': d, 'value': c} for c, d, *_ in rez]}
        else:
            raise SyntaxError
