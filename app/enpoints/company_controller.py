from flask import Response, request
import json
from sqlalchemy.orm import Session

from . import rest
from .. import db
from ..utils import query_to_list, dict_to_obj, obj_to_dict

from app.models import Company

@rest.route('/api/company', methods=['GET'])
def list():
    queryResult = Company.query.order_by(Company.company_name).all()
    jsonstr = json.dumps(query_to_list(queryResult), ensure_ascii=False)
    return Response(jsonstr, mimetype='application/json', status=200)

@rest.route('/api/company/<id>', methods=['GET'])
def get(id):
    currentCompany = Company.query.get(id)
    jsonstr = json.dumps(obj_to_dict(currentCompany), ensure_ascii=False)
    return Response(jsonstr, mimetype='application/json', status=200)

@rest.route('/api/company/<id>', methods=['DELETE'])
def delete(id):
    currentCompany = Company.query.get(id)
    db.session.delete(currentCompany)
    db.session.commit()
    return Response(None, mimetype='application/json', status=204)

@rest.route('/api/company', methods=['POST'])
def save():
    json_dict = request.get_json(silent=True, force=True)
    # company = Company(json_dict['company_name'])
    newCompany = dict_to_obj(dict=json_dict, obj=Company())
    print(newCompany)
    if newCompany.id:
        currentCompany = Company.query.get(json_dict['id'])
        currentCompany.company_name = newCompany.company_name
    else:
        db.session.add(newCompany)
    db.session.commit()
    print(newCompany.id)
    jsonstr = json.dumps(obj_to_dict(newCompany), ensure_ascii=False)
    return Response(jsonstr, mimetype='application/json', status=201)


