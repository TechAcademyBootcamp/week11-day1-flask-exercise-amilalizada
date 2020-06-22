from flask import Blueprint, render_template, request, redirect, flash
from blog.core.models import create_blog, all_blogs ,sql_blog_detail , update_blog_sql , search_data , delete_blog_sql

core = Blueprint(__name__, 'core', static_url_path='idris/')

@core.route('/')
def home():
    print(request.args.get('search'))
    word = request.args.get('search')
    blogs_var = all_blogs()

    if word:
        blogs_var = search_data(word)

    context = {
        'blogs_all': blogs_var
    }
    return render_template('core/index.html', **context)


@core.route('/create', methods=['GET', 'POST'])
def create():
    print(request.form)
    print(request.method)
    if request.method == 'POST':
        # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
        create_blog(**request.form, image='')
        flash('Blog successfully created')
        return redirect('/')
    return render_template('core/create.html')

@core.route('/blog/<int:id_blog>')
def blog_detail(id_blog):
    blog = sql_blog_detail(id_blog)
    context = {
        'blog':blog
    }
    
    return render_template('core/blog_detail.html',**context)

@core.route('/update/<int:id_blog>' , methods = ['GET' , 'POST'])
def update_blog(id_blog):
    blog = sql_blog_detail(id_blog)
    
    context = {
        'blog':blog
    }
    if request.method == 'POST':
        update_blog_sql(**request.form,blog_id=id_blog)
        flash('succesfully updated')
        return redirect(f'/blog/{id_blog}')
    return render_template('core/blog_update.html' , **context)

@core.route('/delete/<int:id_blog>')
def delete(id_blog):
    blog = delete_blog_sql(id_blog)
    return redirect('/')



    




