from marshmallow import Schema, fields
from model.models import Tag


class TagSchema(Schema):
    class Meta:
        model = Tag

    id = fields.Integer()
    tag_ko = fields.String(allow_none=True)
    tag_ja = fields.String(allow_none=True)
    tag_en = fields.String(allow_none=True)


class TagRequestSchema(Schema):
    current_company = fields.String(allow_none=False)
    tag_ko = fields.String(allow_none=True)
    tag_ja = fields.String(allow_none=True)
    tag_en = fields.String(allow_none=True)
