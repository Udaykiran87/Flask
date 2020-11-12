# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:37:24 2020

@author: udaykiran.patnaik
"""
import os
class Config:
    SECRET_KEY = '05902d13136b7781cfa49817560e26f0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # https://youtu.be/IolxqkL7cD8   follow this video to do following changes
    # SECRET_KEY = os.environ.get('SECRET_KEY') # SECRET_KEY = 05902d13136b7781cfa49817560e26f0, set this in environment variable
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') # SQLALCHEMY_DATABASE_URI = sqlite:///site.db, set this in environment variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False   # to remove warning, not included in the tutorial
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # https://youtu.be/IolxqkL7cD8   follow this video to do following changes    
    MAIL_USERNAME = os.environ.get('EMAIL_USER') # EMAIL_USER = set as your from email id for password reset, set this in environment variable
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS') # EMAIL_PASS = set the corresponding password  for above email id  
