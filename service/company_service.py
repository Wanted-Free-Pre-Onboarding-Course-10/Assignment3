from datetime import datetime
from repository import company_repository
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from app import redis_cache

def createCompany(company_ko, company_en, company_ja):
    date = datetime.now()
    company_repository.createCompany(company_ko, company_en, company_ja, date)

    # 회사 생성시 레디스에도 회사이름 데이터 추가 (key: 회사이름, value: 언어)
    redis_cache.set(company_ko, "ko")
    redis_cache.set(company_en, "en")
    redis_cache.set(company_ja, "ja")

    return "회사 생성 성공";

def getAllCompanies():
    return company_repository.getAllCompanies()
