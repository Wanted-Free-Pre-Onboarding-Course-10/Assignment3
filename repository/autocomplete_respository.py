from model.models import Company, CompanyName, TagName
from app import db

def findCompanyName(query, language):
    results = CompanyName.query.filter(CompanyName.name.like('%'+ query +'%'), \
    CompanyName.type == language).all()
    # results.filter(CompanyName.type == language).all()
    return results

