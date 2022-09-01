from flask_app import app
from flask_app.models.users import User
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt


@app.route('/wall')
def r_wall():
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id':session.get('user_id')
    }
    user = User.find_by_id(data)
    posts = User.get_all_posts_with_users()

    return render_template('wall.html', user=user, posts=posts)


@app.route('/post', methods=['POST'])
def f_post():
    inbound = request.form
    data = {
        'id':session.get('user_id'),
        'content': inbound.get('post_content')
    }
    User.create_post(data)
    return redirect('/wall')