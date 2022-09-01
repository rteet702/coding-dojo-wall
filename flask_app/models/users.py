import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.password = data.get('password')

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}> Object | ID: {self.id}'

    @staticmethod
    def validate_login(data):
        is_valid = True
        all_data = [data.get('email'),
                    data.get('password')]
        if not all(all_data):
            is_valid = False
        return is_valid

    @staticmethod
    def validate_registration(data):
        is_valid = True
        all_data = [data.get('first_name'), 
                    data.get('last_name'), 
                    data.get('email'), 
                    data.get('password'), 
                    data.get('confirm_password')]
        if not all(all_data):
            is_valid = False
            flash('* Please enter all information.', 'error')
        if len(all_data[0]) < 2:
            is_valid = False
            flash('* First name must be at least 2 characters long.', 'first_name')
        if len(all_data[1]) < 2:
            is_valid = False
            flash('* Last name must be at least 2 characters long.', 'last_name')
        if not EMAIL_REGEX.match(all_data[2]):
            is_valid = False
            flash('* Please enter a valid email.', 'email')
        if all_data[3] != all_data[4]:
            is_valid = False
            flash('* Passwords do not match.', 'password')

        email_data = {
            'email': all_data[2]
        }

        if User.find_by_email(email_data):
            is_valid = False
            flash('* Email address is already in use.', 'email')

        return is_valid

    @staticmethod
    def validate_post(data):
        is_valid = True
        if not data.get('content') or len(data.get('content')) < 3:
            flash('* Post content is too short.')
            is_valid = False
        return is_valid

    @classmethod
    def find_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        result = connectToMySQL('coding-dojo-wall').query_db(query, data)
        if result == ():
            return False
        else:
            return cls(result[0])

    @classmethod
    def find_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('coding-dojo-wall').query_db(query, data)
        return cls(result[0])

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        result = connectToMySQL('coding-dojo-wall').query_db(query, data)
        return result

    @classmethod
    def create_post(cls, data):
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(id)s);"
        return connectToMySQL('coding-dojo-wall').query_db(query, data)

    @classmethod
    def get_all_posts_with_users(cls):
        query = "SELECT CONCAT_WS(' ',first_name, last_name) as author, content, posts.created_at FROM posts JOIN users ON user_id = users.id ORDER BY posts.created_at DESC;"
        results = connectToMySQL('coding-dojo-wall').query_db(query)
        posts = []
        for post in results:
            posts.append(post)

        return posts