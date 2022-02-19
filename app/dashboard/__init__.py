from flask import Blueprint, render_template
from .routes import article_blueprint, category_blueprint

from authorizer import Authorizer

dashboard_blueprint = Blueprint('dashboard', __name__)

dashboard_blueprint.register_blueprint(article_blueprint)
dashboard_blueprint.register_blueprint(category_blueprint)


@dashboard_blueprint.route('/dashboard')
@Authorizer.login_required
# @Authorizer.admin_only
def index():
    return render_template('dashboard/index.html', title='dashboard')
