from flask import Blueprint, make_response, jsonify, request
from flask_apispec import marshal_with, use_kwargs, doc
from service import tag_service
from serializers.tag import TagSchema, TagRequestSchema

bp = Blueprint('tag', __name__, url_prefix='/tag')

@bp.route('/create', methods=['POST'])
@use_kwargs(TagRequestSchema)
def create(current_company, tag_ko, tag_en, tag_ja):
    print(current_company)
    tag_service.create_tag(current_company,tag_ko, tag_en, tag_ja)
    return make_response(jsonify(msg='success', status_code=201), 201)

