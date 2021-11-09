from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=True)

class TagName(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)

class CompanyTagName(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer ,db.ForeignKey('company.id'))
    tag_id = db.Column(db.Integer ,db.ForeignKey('tag_name.id'))

class CompanyName(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    company_id = db.Column(db.ForeignKey('company.id'))