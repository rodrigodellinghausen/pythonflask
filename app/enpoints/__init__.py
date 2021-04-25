from flask import Blueprint

rest = Blueprint('rest', __name__)

from . import result_controller, company_controller