from flask import render_template, url_for, redirect, Blueprint, request
from .models import *
from .models.user import create_users_table, insert_user, get_user_by_email, User, user_already_exists
import os
import json 

main_bp = Blueprint('main', __name__)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(name, username, email, password)
       
        insert_user(user.name, user.username, user.email, user.password)

        if not user_already_exists(email):
            return redirect(url_for(''))
        else:
            return redirect(url_for('main.login', ))

    else:
        return render_template('register.html')


@main_bp.route('/login', methods=['GET', 'POST'])   
def login():
    return render_template('login.html')


@main_bp.route("/homepage", methods=['GET', 'POST'])
def home():
    return render_template('home.html')