# from model.models import User
from app import db
from model.models import Company

def createCompany(name_ko, name_en, name_ja, created_at):
    company = Company(
        name_ko=name_ko,
        name_en=name_en,
        name_ja=name_ja,
        created_at=created_at
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
