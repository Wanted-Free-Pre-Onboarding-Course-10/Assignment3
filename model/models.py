from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_ko = db.Column(db.String(100), nullable=True)
    company_en = db.Column(db.String(100), nullable=True)
    company_ja = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=True)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_ko = db.Column(db.String(100), nullable=True)
    tag_en = db.Column(db.String(100), nullable=True)
    tag_ja = db.Column(db.String(100), nullable=True)
    company_id = db.Column(db.ForeignKey('company.id'))