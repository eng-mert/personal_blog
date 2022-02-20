from flask import Blueprint, render_template, request, redirect, url_for

from file_uploads import upload_image_to_s3
from app.models import Category, Article

article_blueprint = Blueprint('article', __name__)


@article_blueprint.route('/dashboard/articles')
def index():
    articles = [article for article in Article.get_all()]
    return render_template('dashboard/articles/index.html', title='Articles', articles=articles)


@article_blueprint.route('/dashboard/articles/<record_id>', methods=['GET'])
def get_one(record_id):
    selected_record = Article.find_one(_id=record_id)
    return render_template('dashboard/articles/article.html', title=selected_record.title, article=selected_record)


@article_blueprint.route('/dashboard/articles/publish/<record_id>')
def publish(record_id):
    selected_record = Article.find_one(_id=record_id)
    selected_record.update(state=None)
    return redirect(url_for('dashboard.article.index'))


@article_blueprint.route('/dashboard/articles/create', methods=['GET', 'POST'])
def create():
    categories = [category for category in Category.get_all() if category.parent_id == '']

    if request.method == "POST":
        title = request.form.get('title')
        category_id = request.form.get('category')
        cover = request.files.get('cover')
        draft = request.form.get('draft')
        content = request.form.get('content')
        tags = request.form.get('tags')

        new_article = Article(title=title, content=content, category_id=category_id,
                              state=draft, tags=tags, cover=upload_image_to_s3(cover))
        new_article.save_to_db()
        return redirect(url_for('dashboard.article.index'))
    return render_template('dashboard/articles/create.html', title='create article',
                           categories=categories)


@article_blueprint.route('/dashboard/articles/edit/<record_id>',methods = ['GET','POST'])
def edit(record_id):
    categories = [category for category in Category.get_all() if category.parent_id == '']
    selected_record = Article.find_one(_id=record_id)
    if request.method == "POST":
        title = request.form.get('title')
        category_id = request.form.get('category')
        cover = request.files.get('cover')
        draft = request.form.get('draft')
        content = request.form.get('content')
        tags = request.form.get('tags')
        selected_record.update(title=title,category_id=category_id,
                               state=draft,content=content,tags=tags)
        if cover.filename:
            selected_record.update(cover=save_image(cover))
        return redirect(url_for('dashboard.article.get_one',record_id=selected_record._id))
    return render_template('dashboard/articles/edit.html', title='edit article', categories=categories,
                           article=selected_record)


@article_blueprint.route('/dashboard/articles/delete/<record_id>')
def delete(record_id):
    selected_record = Article.find_one(_id=record_id)
    selected_record.delete()
    return redirect(url_for('dashboard.article.index'))
