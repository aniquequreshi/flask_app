from flask import render_template, redirect, request, url_for
from app.posts import bp
from app.extensions import db
from app.models.post import Post

@bp.route('/', methods=('GET', 'POST'))
def index():
    posts = Post.query.all()
    if request.method == 'POST':
        new_post = Post(content=request.form['content'], title=request.form['title'])
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')