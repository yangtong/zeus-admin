# -*- coding:utf-8 -*-
__author__ = 'yangtong'

from web import app
from flask import render_template, request, g
from frame import config


@app.route('/')
def home_get():
    return render_template(
        'home/index.html',
        data={
        }
    )

@app.route('/link')
def link_get():
    return render_template(
        'link/index.html',
        data={
            #'vs': vs,
        }
    )

