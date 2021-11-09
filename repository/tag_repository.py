from model.models import Tag, Company
from app import db


def create(current_company, tag_ko, tag_ja, tag_en):
    print(current_company)
    company = Company.query.filter_by(company_ko=current_company).first()
    if (company == None)
        company = Company.query.filter_by(company_en=current_company).first()
    tag = Tag(tag_ko = tag_ko,tag_ja = tag_ja,tag_en = tag_en,company_id = company.id)
    db.session.add(tag)
    db.session.commit()