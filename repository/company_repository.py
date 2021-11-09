# from model.models import User
from app import db
from model.models import Company

def createCompany(company_ko, company_en, company_ja, created_at):
    company = Company(
        company_ko = company_ko,
        company_en = company_en,
        company_ja = company_ja,
        created_at = created_at
    )
    db.session.add(company)
    db.session.commit()

def getAllCompanies():
    companys = Company.query.all()

    return companys