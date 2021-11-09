from model.models import Company, CompanyName, TagName
from app import db

def findCompanyName(query, language):
    results = CompanyName.query.filter(CompanyName.name.like('%'+ query +'%')).all()
    return results

