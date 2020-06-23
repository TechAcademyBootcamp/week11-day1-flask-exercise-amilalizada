from flask import Blueprint, render_template, request, redirect, flash
from blog.core.models import create_blog, all_blogs ,sql_blog_detail , update_blog_sql , search_data , delete_blog_sql
from blog.core.forms import BlogForm
core = Blueprint(__name__, 'core', static_url_path='idris/')

@core.route('/')
def home():
    print(request.args.get('search'))
    word = request.args.get('search')
 
    if word:
        blogs_var = search_data(word)
    else:
        blogs_var = all_blogs()
    context = {
        'blogs_all': blogs_var
    }
    
    return render_template('core/index.html', **context)

@core.route('/create', methods=['GET', 'POST'])
def create():
    form = BlogForm()
    if form.validate_on_submit():
        print(form.data)
        create_blog(**form.data, image='')

    context = {
        'form': form
    }
    return render_template('core/create.html', **context)

@core.route('/blog/<int:id_blog>')
def blog_detail(id_blog):
    blog = sql_blog_detail(id_blog)
    context = {
        'blog':blog
    }
    return render_template('core/blog_detail.html',**context)

@core.route('/update/<int:id_blog>' , methods = ['GET' , 'POST'])
def update_blog(id_blog):

    if request.method == 'POST':
        form = BlogForm()
        print(form.data)
        if form.validate_on_submit():
            print(form.data)
            update_blog_sql(**form.data,blog_id=id_blog)
            flash('succesfully updated')
            return redirect(f'/blog/{id_blog}')
    else:
        blog = sql_blog_detail(id_blog)
        form = BlogForm(data=blog)
    context = {
        'form':form
    }
    return render_template('core/blog_update.html' , **context)

@core.route('/delete/<int:id_blog>')
def delete(id_blog):
    blog = delete_blog_sql(id_blog)
    flash('deleted')
    return redirect('/')



    




