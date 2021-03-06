
from flask import Blueprint, render_template, request, redirect, session, flash
from blog.auth.forms import RegisterForm, LogInForm
from flask_login import login_user  
from wtforms import ValidationError
from blog.auth.models import db, User

auth = Blueprint(__name__, 'auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    next_page = request.args.get('next', '/')
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.check_password(form.password.data):
        login_user(user)
        flash('Logged in successfully.')if request.method == 'POST' and form.validate_on_submit():
        return redirect(next_page)
    else:
        # form_error_message = 'User not found'
        flash('User not found')
    context = {
        'form': form,
        }
    return render_template('auth/login.html', **context)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        create_user(**form.data)
        user = User(username=form.username.data, email=form.email.data, first_name= form.first_name.data, last_name=form.surname.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User created')
        return redirect('/')
    context = {
        'form': form
        }
    return render_template('auth/register.html', **context)