from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import redis
import os

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config ==None:
        app.config.from_object(config)
    else:
        app.config.from_object(config.Testing)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from model import models

    # 블루프린트
    from views import tag_views, company_views, autocomplete_views
    app.register_blueprint(company_views.bp)
    app.register_blueprint(tag_views.bp)
    app.register_blueprint(autocomplete_views.bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return make_response(jsonify(msg="없는 페이지 입니다. 아마 존재하지 않는 게시글 id로 요청을 보내셨을 가능성이 높습니다.", status_code=404),404)

    return app

redis_cache = redis.Redis(host=os.getenv('MYSQL_HOST'), port=os.getenv('REDIS_PORT'), db=0)

app = create_app()

if __name__ == '__main__':
    app.run()
