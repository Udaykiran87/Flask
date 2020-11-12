# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:25:56 2020

@author: udaykiran.patnaik
"""

from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    #name = request.args.get("name", "Page")
    return render_template('home.html',posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')
