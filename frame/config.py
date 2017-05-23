# -*- coding:utf-8 -*-
__author__ = 'yangtong'

# -- app config --
DEBUG = True

# -- db config --
DB_HOST = "10.180.92.226"
DB_PORT = 3306
DB_USER = "openstack_zabbix"
DB_PASS = "MTlmMTAwODZmYWM"
DB_NAME = "zabbix"

# -- zabbix api config --
ZABBIX_SERVER = "http://115.182.93.59/zabbix/"
ZABBIX_USER = "zabbix_api_noc"
ZABBIX_PASSWORD = "mJbhyhPlb9zR"

# -- zabbix db config --
ZABBIX_DB_HOST = "10.180.92.226"
ZABBIX_DB_PORT = 3306
ZABBIX_DB_USER = "openstack_zabbix"
ZABBIX_DB_PASS = "MTlmMTAwODZmYWM"
ZABBIX_DB_NAME = "zabbix"

# -- cookie config --
SECRET_KEY = "4e.5tyg8-u9ioj"
SESSION_COOKIE_NAME = "falcon-portal"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

UIC_ADDRESS = {
    'internal': 'http://10.154.249.12:8080',
    'external': 'http://11.11.11.11:8080',
}

UIC_TOKEN = ''

MAINTAINERS = ['root']
CONTACT = ''

COMMUNITY = True

try:
    from frame.local_config import *
except Exception, e:
    print "[warning] %s" % e
