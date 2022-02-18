from flask import Blueprint, render_template

article_blueprint = Blueprint('article', __name__)


@article_blueprint.route('/dashboard/articles')
def index():
    return render_template('dashboard/articles/index.html', title='Articles')


@article_blueprint.route('/dashboard/articles/create')
def create():
    return render_template('dashboard/articles/create.html', title='create article')


@article_blueprint.route('/dashboard/articles/edit/<record_id>')
def edit(record_id):
    return render_template('dashboard/articles/edit.html', title='edit article')


@article_blueprint.route('/dashboard/articles/delete/<record_id>')
def delete(record_id):
    return render_template('dashboard/articles/delete.html', title='delete article')
