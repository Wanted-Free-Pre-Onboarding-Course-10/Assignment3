import json

from flask import Blueprint, make_response, jsonify, request
import pprint
from service import company_service


pp = pprint.PrettyPrinter(indent=4)
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

    result = company_service.findCompanyNameAndTagsByLanguage(savedId, language)

    return jsonify(result)


@bp.route('/', methods=['GET'])
def companies():
    query = request.args.get('query')

    language = request.headers.get('x-wanted-language')
    response = company_service.getOneCompany(query, language)

    print(response)

    return jsonify(response)

@bp.route('/test', methods=['POST'])
def companies():
    result = request.get_json()

    for r in result:
        requestCompanies = r['company_name'];
        requestTags = r['tags'];
        company_service.createCompany(requestCompanies, requestTags)

    return "test데이터 잘들어갔습니다.";

