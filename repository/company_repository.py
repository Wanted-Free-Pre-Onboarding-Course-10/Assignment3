from sqlalchemy import and_

from model.models import Company, CompanyName, TagName, CompanyTagName
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

def getOneCompanyByCompanyName(query):
    return db.session.query(CompanyName, Company) \
        .join(Company, Company.id == CompanyName.company_id) \
        .filter(CompanyName.name.like(f"%{query}%")) \
        .all()

def getOneCompanyByCompanyIdAndLanguageType(companyId, language):
    return db.session.query(CompanyName) \
        .filter(
        and_(
            CompanyName.company_id == companyId,
            CompanyName.type == language
        )) \
        .first()

def getTagsByCompanyIdAndTagName(companyId, language):
    return db.session.query(TagName) \
        .join(CompanyTagName, CompanyTagName.company_id == TagName.company_id).filter(
        and_(
            TagName.type == language,
            CompanyTagName.company_id == companyId
        )
    ).all()