from flask import Blueprint
from service import company_service
from flask_apispec import marshal_with, use_kwargs, doc
from serializers.company import CompanyRequestSchema, CompanyResponseSchema
# from app import redis_client
from app import redis_cache
# import redis

bp = Blueprint('company', __name__, url_prefix='/company')

# redis_cache = redis.Redis(host='localhost', port=6379, db=0, password="redis_password")
#

@bp.route('/', methods=['GET'])
@marshal_with(CompanyResponseSchema(many=True))
def getAllCompanies():
    result = company_service.getAllCompanies()
    print("회사 데이터")
    print(result)
    return result;

@bp.route('/', methods=['POST'])
@use_kwargs(CompanyRequestSchema)
def createCompany(company_ko, company_en, company_ja):
    companies = company_service.createCompany(company_ko, company_en, company_ja)

    redis_cache.set(company_ko, company_en)
    print(company_ko + " " + company_en)
    print("레디스에 저장")
    return companies;

@bp.route('/find', methods=['POST'])
@use_kwargs(CompanyRequestSchema)
def findCompanies(company_ko, company_en, company_ja):
    companies = company_service.createCompany(company_ko, company_en, company_ja)

    if redis_cache.exists(company_ko):
        print(redis_cache.get(company_ko))
    else:
        print("해당 키의 값 없음")
    # print(redis_cache.get())

    return companies;