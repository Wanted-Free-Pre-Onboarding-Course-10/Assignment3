from flask import Blueprint
from service import company_service
from flask_apispec import marshal_with, use_kwargs, doc
from serializers.company import CompanyRequestSchema, CompanyResponseSchema

bp = Blueprint('company', __name__, url_prefix='/company')

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
    return companies;

@bp.route('/find', methods=['POST'])
@use_kwargs(CompanyRequestSchema)
def findCompanies(company_ko, company_en, company_ja):
    companies = company_service.createCompany(company_ko, company_en, company_ja)
    return companies;