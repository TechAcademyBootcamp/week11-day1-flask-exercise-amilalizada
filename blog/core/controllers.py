from flask import Blueprint, render_template, request, redirect, flash, send_from_directory
from flask_login import login_required, current_user
from blog import db
from blog.core.models import Contact, Blog
from blog.core.utils import save_file
import math
core = Blueprint(__name__, 'core', static_url_path='idris/')

@core.route('/')
def home():
    page = int(request.args.get('page', 1))
    print(page)
    blogs = Blog.query.filter_by().order_by(Blog.created_at.desc()).limit(2).offset((page-1)*2)
    print(blogs)
    page_count = math.ceil(Blog.query.filter_by().count()/2)
    page_range = range(1, page_count+1)
    next_page = None
    previous_page = None

@login_required
def create():
    form = BlogForm()
    if request.method == 'POST' and form.validate_on_submit():
        f = form.image.data
        file_path = save_file(f)
        blog = Blog(title=form.title.data, description=form.description.data, image=file_path, user_id=current_user.id)
        db.session.add(blog)
        db.session.commit()
        flash('Melumat elave edildi')
        return redirect('/')
    context = {
        'form': form
    }
    return render_template('core/create.html', **context)

@core.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact_info = Contact(username=form.username.data, email=form.email.data, subject=form.subject.data, message=form.message.data)
        db.session.add(contact_info)
        db.session.commit()
        flash('Mesajiniz gonderildi')
        return redirect('/')
    context = {
        'form': form
    }
    return render_template('core/contact.html', **context)
@core.route('/faqs')
def faqs():
    questions = Contact.query.all()
    print(questions)
    context = {
        'questions': questions
    }
    return render_template('core/faqs.html', **context)




    




