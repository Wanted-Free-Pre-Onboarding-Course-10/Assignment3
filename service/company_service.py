from model.models import Company
from model.models import CompanyName
from app import db

def getOneCompany(query, language):

    result = db.session.query(Company,CompanyName).filter(Company.id == CompanyName.company_id).all()

    return result