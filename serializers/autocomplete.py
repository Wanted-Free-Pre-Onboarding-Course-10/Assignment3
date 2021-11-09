from marshmallow import Schema, fields
from model.models import Company

class AutoCompleteSchema(Schema):
    query = fields.String(allow_none=False)
