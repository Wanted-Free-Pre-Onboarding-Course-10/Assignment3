from marshmallow import Schema, fields
from model.models import Company

class AutoCompleteSchema(Schema):
    prefix = fields.String(allow_none=False)
