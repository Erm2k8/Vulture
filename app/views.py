from flask import render_template, url_for, Blueprint
from .models import *
import os

main_bp = Blueprint('main', __name__)


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@main_bp.route('/login', methods=['GET', 'POST'])   
def login():
    return render_template('login.html')