from flask import Blueprint, render_template, redirect, url_for, request, flash

from app.models import Category

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/dashboard/categories', methods=['GET'])
def index():
    categories = [category.to_json() for category in Category.get_all() if category.parent_id == ""]
    return render_template('dashboard/categories/index.html', title='categories', categories=categories)


@category_blueprint.route('/dashboard/categories/<record_id>', methods=['GET'])
def get_one(record_id):
    selected_record = Category.find_one(_id=record_id)
    print(selected_record.children)
    return render_template('dashboard/categories/category.html', title=selected_record.title, parent=selected_record)


@category_blueprint.route('/dashboard/categories/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        title = request.form.get('category')
        parent_id = request.form.get('parent_id')
        if Category.find_one(title=title):
            flash('This category already in your list', 'warning')
            return redirect(url_for('dashboard.category.index'))
        else:
            new_category = Category(title=title, parent_id=parent_id)
            new_category.save_to_db()
    return redirect(url_for('dashboard.category.index'))


@category_blueprint.route('/dashboard/categories/delete/<record_id>', methods=['GET', 'POST'])
def delete(record_id):
    selected_record = Category.find_one(_id=record_id)
    parent_id = selected_record.parent_id
    if selected_record.articles or selected_record.children:
        flash('Category Must be empty', 'warning')
        return redirect(url_for('dashboard.category.index'))
    else:
        if parent_id:
            selected_record.delete()
            return redirect(url_for('dashboard.category.get_one', record_id=parent_id))
        else:

            selected_record.delete()
            return redirect(url_for('dashboard.category.index'))
