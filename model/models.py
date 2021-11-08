from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_ko = db.Column(db.String(100), nullable=True)
    name_en = db.Column(db.String(100), nullable=True)
    name_ja = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=True)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    company_id = db.Column(db.ForeignKey('company.id'))