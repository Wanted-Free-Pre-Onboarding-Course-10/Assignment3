from marshmallow import Schema, fields
from model.models import Company


class CompanyRequestSchema(Schema):
    name_ko = fields.String(allow_none=False)
    name_en = fields.String(allow_none=False)
    name_ja = fields.String(allow_none=False)

class CompanyResponseSchema(Schema):
    class Meta:
        model = Company

    id = fields.Integer()
    name_ko = fields.String(allow_none=False)
    name_en = fields.String(allow_none=False)
    name_ja = fields.String(allow_none=False)
    created_at = fields.DateTime(allow_none=False)
    modified_at = fields.DateTime(allow_none=True)