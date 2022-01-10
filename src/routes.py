from src import api, app
from src.info import Info
from src.timeline import Timeline

api.add_resource(Info, '/api/info', strict_slashes=False)
api.add_resource(Timeline, '/api/timeline', strict_slashes=False)


@app.route('/')
def home():
    return '''<h1>Hello</h1>
    <p><a href="/api/info">Api Info</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=weekly">Api Timeline cumulative weekly</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=usual&Grouping=weekly">Api Timeline usual weekly</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=bi-weekly">Api Timeline cumulative bi-weekly</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=usual&Grouping=bi-weekly">Api Timeline usual bi-weekly</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=monthly">Api Timeline cumulative monthly</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=usual&Grouping=monthly">Api Timeline usual monthly</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=monthly&brand=Downy&source=amazon">Api Timeline cumulative monthly with attrs</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=usual&Grouping=monthly&asin=B0014D3N0Q&source=amazon&stars=5&brand=Downy">Api Timeline usual monthly with attrs</a></p>
    '''
