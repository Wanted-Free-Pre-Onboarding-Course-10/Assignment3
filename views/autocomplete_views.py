from flask import Blueprint, request, jsonify
from service import autocomplete_service
from flask_apispec import marshal_with, use_kwargs, doc
from serializers.company import CompanyRequestSchema, CompanyResponseSchema

from serializers.autocomplete import AutoCompleteSchema
from app import redis_cache

bp = Blueprint('autocomplete', __name__, url_prefix='/search')

@bp.route('/', methods=['GET'])
@use_kwargs(AutoCompleteSchema)
def autoComplete():
    # 회사이름 자동완성을 위한 query parameter(query)
    query = request.args.get('query')

    # 요청헤더에 담긴 언어 조회
    language = request.headers.get('x-wanted-language')

    # 입력들어온 prefix로 조회한 회사들
    result = autocomplete_service.autoComplete(query, language)

    return jsonify(result)