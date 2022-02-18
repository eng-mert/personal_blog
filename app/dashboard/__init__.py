from flask import Blueprint,render_template
from .routes import article_blueprint, category_blueprint

dashboard_blueprint = Blueprint('dashboard', __name__)

dashboard_blueprint.register_blueprint(article_blueprint)
dashboard_blueprint.register_blueprint(category_blueprint)


@dashboard_blueprint.route('/dashboard')
def index():
    return render_template('dashboard/index.html',title='dashboard')
