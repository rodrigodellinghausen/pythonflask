from flask import Response, request
import json
from sqlalchemy.orm import Session

from . import rest
from .. import db

from app.models import Company

@rest.route('/api/company', methods=['GET'])
def list():
    list = Company.query.all()
    print(list)
    jsonobj = {'content': []}
    jsonstr = json.dumps(jsonobj, ensure_ascii=False)
    return Response(jsonstr, mimetype='application/json', status=200)

@rest.route('/api/company', methods=['POST'])
def save():
    json_dict = request.get_json(silent=True, force=True)
    print(json_dict)
    print("Type:", type(json_dict))
    company = Company(json_dict['company_name'])
    if 'id' in json_dict:
        currentCompany = Company.query.get(json_dict['id'])
        currentCompany.company_name = company.company_name
    else:
        db.session.add(company)
    db.session.commit()
    jsonstr = json.dumps({'content': {}}, ensure_ascii=False)
    return Response(jsonstr, mimetype='application/json', status=201)


