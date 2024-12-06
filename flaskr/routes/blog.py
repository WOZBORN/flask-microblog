import os
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from flaskr.models import db, Post
from flaskr.forms import PostForm

bp = Blueprint('blog', __name__)

UPLOAD_FOLDER = 'flaskr/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created.desc()).all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            form.image.data.save(filepath)

        post = Post(title=form.title.data, body=form.body.data, image=filename, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully.')
        return redirect(url_for('blog.index'))
    return render_template('blog/create.html', form=form)

@bp.route('/article/<int:id>')
def article(id):
    post = Post.query.get_or_404(id)
    return render_template('blog/article.html', post=post)