# from model.models import User
from app import db
from model.models import Company

def createCompany(company_ko, company_en, company_ja, created_at):
    company = Company(
<<<<<<< HEAD
        company_ko = company_ko,
        company_en = company_en,
        company_ja = company_ja,
        created_at = created_at
=======
        company_ko=company_ko,
        company_en=company_en,
        company_ja=company_ja,
>>>>>>> 67ff408f1b6fa84f3f159be090c152a926e70778
    )
    db.session.add(company)
    db.session.commit()

def getAllCompanies():
    companys = Company.query.all()

    return companys