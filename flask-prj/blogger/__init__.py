from flask import Flask
import os
# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return '<h1>Hello Flask!</h1>'


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return '<h1>Hello Flask!</h1>'
    
    app.config.from_mapping(
        SECRET_KEY='Bla bla bla',
        DATABASE=os.path.join(app.instance_path, 'blogger.db') 
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .import db
    db.init_app(app)
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app