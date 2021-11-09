from flask import Blueprint, request, jsonify
from service import autocomplete_service
from flask_apispec import marshal_with, use_kwargs, doc
from serializers.company import CompanyRequestSchema, CompanyResponseSchema

from serializers.autocomplete import AutoCompleteSchema
from app import redis_cache

bp = Blueprint('autocomplete', __name__, url_prefix='/autocomplete')

@bp.route('/', methods=['GET'])
@use_kwargs(AutoCompleteSchema)
def autoComplete():
    # 회사이름 자동완성을 위한 query parameter(prefix값)
    prefix = request.args.get('prefix')

    # 입력들어온 prefix로 조회한 회사들
    result = autocomplete_service.autoComplete(prefix)

    return jsonify(result)