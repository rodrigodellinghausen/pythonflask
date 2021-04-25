from . import rest

from app.models import Result

@rest.route('/api/result', methods=['GET', 'POST'])
def hello():
    r = Result.query.get(1)
    return "Hello result > {}!".format(r.url)

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

# @app.route('/result/<id>')
# def hello_name(id):
#     r = Result.query.get(id)
#     return "Hello result > {}!".format(r.url)