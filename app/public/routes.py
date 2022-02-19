from flask import Blueprint, render_template

public_blueprint = Blueprint('public', __name__)


@public_blueprint.route('/index')
@public_blueprint.route('/')
def index():
    return render_template('public/index.html',title='Home')


@public_blueprint.route('/blog')
def blog():
    return render_template('public/blog.html',title='Home')


@public_blueprint.route('/blog/<article_id>')
def article(article_id):
    return render_template('public/article.html',title='Home')


@public_blueprint.route('/projects')
def projects():
    return render_template('public/projects.html',title='Home')


@public_blueprint.route('/projects/<project_id>')
def project(project_id):
    return render_template('public/project.html',title='Home')


@public_blueprint.route('/about')
def about():
    return render_template('public/about.html',title='Home')
