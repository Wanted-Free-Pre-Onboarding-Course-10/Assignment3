from marshmallow import Schema, fields
from model.models import Company


class CompanyRequestSchema(Schema):
    company_ko = fields.String(allow_none=False)
    company_en = fields.String(allow_none=False)
    company_ja = fields.String(allow_none=False)

class CompanyResponseSchema(Schema):
    class Meta:
        model = Company

    id = fields.Integer()
    company_ko = fields.String(allow_none=False)
    company_en = fields.String(allow_none=False)
    company_ja = fields.String(allow_none=False)
    created_at = fields.DateTime(allow_none=False)
    modified_at = fields.DateTime(allow_none=True)