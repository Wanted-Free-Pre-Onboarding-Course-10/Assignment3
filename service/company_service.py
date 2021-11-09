from datetime import datetime
from repository import company_repository

def createCompany(company_ko, company_en, company_ja):
    date = datetime.now()
    company_repository.createCompany(company_ko, company_en, company_ja, date)
    return "회사 생성 성공";

def getAllCompanies():
    return company_repository.getAllCompanies()