# -*- coding:utf-8 -*-
__author__ = 'yangtong'

from flask_script import Manager
from web inmport app

@manager.command
def hello():
    print "hello world"

if __name__ == "__mian__":
    manager.run()