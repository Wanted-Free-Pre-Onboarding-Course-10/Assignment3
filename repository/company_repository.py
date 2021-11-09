# from model.models import User
from app import db
from model.models import Company

def createCompany(company_ko, company_en, company_ja, created_at):
    company = Company(
        company_ko=company_ko,
        company_en=company_en,
        company_ja=company_ja,
    )

    db.session.add(company)
    db.session.commit()

def getAllCompanies():
    companys = Company.query.all()

    return companys

# def signup(username, hashed_password):
#     user = User(username=username, password=hashed_password)
#     db.session.add(user)
#     db.session.commit()
#
#
# def login(username, password):
#     user = User.query.filter_by(username=username).first()
#     if not user:
#         return 0
#     else:
#         if check_password_hash(user.password, password):
#             return user.id
#         else:
#             return 0
