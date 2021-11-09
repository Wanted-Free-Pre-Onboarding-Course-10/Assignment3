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

def createTagName(type, name):
    tagName = TagName(type=type,name=name)
    db.session.add(tagName)
    db.session.commit()
    return tagName

def createCompanyTagName(company_id, tag_id):
    companyTagName = CompanyTagName(company_id=company_id,tag_id=tag_id)
    db.session.add(companyTagName)
    db.session.commit()

    return companyTagName

# 이름으로 tag Name조회
def findTagNameByNameAndType(name, type):
    findtagNameResult = db.session.query(TagName) \
        .filter(and_(TagName.name == name, TagName.type == type)) \
        .first()

    return findtagNameResult
  
def getOneCompanyByCompanyName(companyName):
    return db.session.query(CompanyName, Company) \
        .join(Company, Company.id == CompanyName.company_id) \
        .filter(CompanyName.name.like(f"%{companyName}%")) \
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
        .join(CompanyTagName, CompanyTagName.tag_id == TagName.id).filter(
        and_(
            TagName.type == language,
            CompanyTagName.company_id == companyId
        )
    ).all()
