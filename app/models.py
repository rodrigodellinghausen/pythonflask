from sqlalchemy.dialects.postgresql import JSON

from . import db

class Company(db.Model):
    __tablename__ = 'carm_companies'

    id = db.Column(db.BigInteger(), primary_key=True)
    company_name = db.Column(db.String())

    def __init__(self, company_name):
        self.company_name = company_name

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Project(db.Model):
    __tablename__ = 'carm_projects'

    id = db.Column(db.BigInteger(), primary_key=True)
    project_name = db.Column(db.String())
    company_id = db.Column(db.BigInteger())
    project_desciption = db.Column(db.String())

    def __init__(self, project_name, company_id, project_desciption):
        self.project_name = project_name
        self.company_id = company_id
        self.project_desciption = project_desciption

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words
    
    def __repr__(self):
        return '<id {}>'.format(self.id)