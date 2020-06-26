import pymysql.cursors
from datetime import datetime
from blog.auth.models import create_blog_table

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='blogs_project',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_blog_table():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """create table if not exists blogs(
            id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
            title varchar(255) NOT NULL,
            description text NOT NULL,
            owner_name varchar(50) NOT NULL,
            image varchar(500),
            auth_id int(11) unsigned NOT NULL , 
            created_at datetime NOT NULL,
            is_published tinyint(1) default 1 ,
            FOREIGN KEY (auth_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
            INDEX(id , title)
            ); 
            """
        cursor.execute(sql)
    connection.commit()

def create_blog(title, description, owner_name, image,auth_id, is_published=True ,**kwargs):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """insert into blogs_project.blogs(title, description, owner_name, image, created_at, is_published ,auth_id )
            values(%s, %s, %s, %s, %s, %s, %s) 
            """
        now = datetime.now()
        created_ad = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (title, description, owner_name, image, created_ad, is_published,auth_id))
    connection.commit()

def all_blogs():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select * from blogs_project.blogs order by created_at desc;"""
        cursor.execute(sql,)
    return cursor.fetchall()

def sql_blog_detail(blog_id):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select * from blogs_project.blogs where id=%s;"""
        cursor.execute(sql,blog_id)
    return cursor.fetchone()

def update_blog_sql(title,description,owner_name,blog_id,**kwargs):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """Update blogs_project.blogs Set title=%s , description=%s , owner_name=%s where id=%s"""
        time = datetime.now()
        create_at = time.strftime('%Y-%m-%d %H:%m:%s')
        cursor.execute(sql,(title,description,owner_name,blog_id))
    connection.commit()
    return cursor.fetchone()

def delete_blog_sql(blog_id):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """delete from blogs_project.blogs where id=%s"""
        cursor.execute(sql, blog_id)
    connection.commit()


    return cursor.fetchone()


def search_data(keyword):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """SELECT * from blogs_project.blogs WHERE title LIKE %s"""
        cursor.execute(sql, ("%" + keyword + "%"))

    return cursor.fetchall()





create_blog_table()