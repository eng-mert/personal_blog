from flask import Blueprint, render_template

from app.models import Category

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/dashboard/categories', methods=['GET'])
def index():
    categories = [category.to_json() for category in Category.get_all()]
    return render_template('dashboard/categories/index.html',title='categories')
