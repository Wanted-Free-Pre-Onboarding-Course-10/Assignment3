from flask import Blueprint, make_response, jsonify, request
from flask_apispec import marshal_with, use_kwargs, doc
# from service import post_service
# from serializers.post import PostSchema, CreatePostRequestSchema
# from serializers.company import CreateCompanyRequestScheme
from service import company_service

bp = Blueprint('companies', __name__, url_prefix='/companies')

@bp.route('/', methods=["POST"])
def createCompanies():
    result = request.get_json()
    requestCompanies = result['company_name'];

    requestTags = result['tags'];

    # savedId : Company id
    savedId = company_service.createCompany(requestCompanies, requestTags)

    # 요청헤더에 담긴 언어 조회 - language에 맞는
    language = request.headers.get('x-wanted-language')

    return "hi"