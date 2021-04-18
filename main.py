import os

from flask_app import app

from flask_app.models import Result

@app.route('/')
def hello():
    return "Hello World!"

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

@app.route('/<id>')
def hello_name(id):
    r = Result.query.get(id)
    return "Hello > {}!".format(r.url)


if __name__ == '__main__':
    app.run()