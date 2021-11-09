from flask import Blueprint, request, jsonify
from service import company_service
from flask_apispec import marshal_with, use_kwargs, doc

from app import redis_cache

bp = Blueprint('companies', __name__, url_prefix='/companies')

@bp.route('/', methods=['GET'])
def companies():
    query = request.args.get('query')

    language = request.headers.get('x-wanted-language')


    response = company_service.getOneCompany(query,language)

    return jsonify(response)