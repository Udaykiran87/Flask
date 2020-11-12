# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:21:22 2020

@author: Uday
"""
from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)