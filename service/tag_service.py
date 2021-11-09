from repository import tag_repository
from datetime import datetime


# def get_post_list(page):
#     return post_repository.post_list(page)


# def get_detail(post_id):
#     return post_repository.detail(post_id)


def create_tag(current_company, tag_ko, tag_ja, tag_en):
    return tag_repository.create(current_company,tag_ko, tag_ja, tag_en)

