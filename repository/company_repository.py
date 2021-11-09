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
