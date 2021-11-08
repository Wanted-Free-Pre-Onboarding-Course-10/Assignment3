from flask import Blueprint
from service import company_service
from flask_apispec import marshal_with, use_kwargs, doc
from serializers.company import CompanyRequestSchema

bp = Blueprint('company', __name__, url_prefix='/company')

@bp.route('/', methods=['GET'])
@marshal_with(CompanyRequestSchema)
def getAllCompanies():
    result = company_service.getAllCompanies()

    return result;

@bp.route('/', methods=['POST'])
@use_kwargs(CompanyRequestSchema)
def createCompany(name_ko, name_en, name_ja):
    companies = company_service.createCompany(name_ko, name_en, name_ja)

    return companies;

# @doc(tags=['auth'], description='회원정보를 저장한다.')
# @bp.route('/signup/', methods=['POST'])
# @use_kwargs(AuthRequestSchema)
# def signup(username, password):
#     auth_service.signup(username, password)
#     return make_response(jsonify(msg='{} signup success'.format(username), status_code=201), 201)
#
#
# @doc(tags=['auth'], description='회원정보를 받아 accesstoken을 반환한다.')
# @bp.route('/login/', methods=['POST'])
# @use_kwargs(AuthRequestSchema)
# @marshal_with(TokenSchema, code=200)
# def login(username, password):
#     is_login_success = auth_service.login(username, password)
#     if is_login_success:
#         return jsonify(access_token=is_login_success, status_code=200)
#     else:
#         return  make_response(jsonify(msg='잘못된 로그인 정보입니다.', status_code=404), 404)
