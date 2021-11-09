from marshmallow import Schema, fields
from model.models import Company

class AutoCompleteResponseSchema(Schema):
    key = "company_name"
    value = fields.String(allow_none=False)
