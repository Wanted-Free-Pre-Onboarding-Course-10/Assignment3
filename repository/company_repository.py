from model.models import Company, CompanyName, TagName
from app import db

def createCompany():
    company = Company()
    db.session.add(company)
    db.session.commit()

    return company

def createCompanyName(id, type, name):
    companyName = CompanyName(type=type,name=name,company_id=id)
    db.session.add(companyName)
    db.session.commit()

def createTagName(id, type, name):
    tagName = TagName(type=type,name=name,company_id=id)
    db.session.add(tagName)
    db.session.commit()

