# -*- coding:utf-8 -*-
__author__ = 'yangtong'

import logging
from pyzabbix import ZabbixAPI
from frame import config

def connect_zabbix_api(cfg):
    try:
        conn = ZabbixAPI(zabbix_server)
        conn.timeout = 5
        conn.login(zabbix_user,zabbix_passwd)
        return conn
    except Exception, e:
        logging.getLogger().critical('connect zabbix api: %s' % e)
        return None

class API(object):
    def __init__(self, cfg):
        self.config = cfg
        self.conn = None

    # Get a list of all issues (AKA tripped triggers)
    def issues(self, *a, **kw):
        cursor = connect_zabbix_api(self.config)
        cursor.trigger.get(only_true=1,
            skipDependent=1,
            monitored=1,
            active=1,
            output='extend',
            expandDescription=1,
            expandData='host',
        )
        # Do another query to find out which issues are Unacknowledged
        return triggers

api = API(config)