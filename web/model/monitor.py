# -*- coding:utf-8 -*-
__author__ = 'yangtong'
from .bean import Bean
from frame.zbx import api

class Monitor(Bean):
    @classmethod
    def query(cls, hg, item_key, type, page, limit):
        where = ''
        order = ''
        if hg and item_key and type is 1:
            cls._cols = "distinct hosts.host,items.itemid," \
                        "items.name as description,FROM_UNIXTIME(history.clock, '%s') as lastclock," \
                        "history.value as lastvalue,items.units" % '%%Y-%%m-%%d %%H:%%i:%%S'
            cls._tbl = "(((history join items on items.itemid=history.itemid) join " \
                       "hosts on hosts.hostid=items.hostid) join " \
                       "hosts_groups on hosts.hostid=hosts_groups.hostid) join " \
                       "groups on hosts_groups.groupid=groups.groupid"
        elif hg and item_key and type is 2:
            cls._cols = "distinct hosts.host,items.itemid," \
                       "items.name as description,FROM_UNIXTIME(history_uint.clock, '%s') as lastclock," \
                       "history_uint.value as lastvalue,items.units" % '%%Y-%%m-%%d %%H:%%i:%%S'
            cls._tbl = "(((history_uint join items on items.itemid=history_uint.itemid) join " \
                      "hosts on hosts.hostid=items.hostid) join " \
                      "hosts_groups on hosts.hostid=hosts_groups.hostid) join " \
                      "groups on hosts_groups.groupid=groups.groupid"
        where = "key_='%s' and " \
                     "groups.name='%s' and " \
                     "unix_timestamp()-120 < clock " % (item_key, hg)
        order = "lastvalue desc"

        vs = cls.select(where=where, page=page, limit=limit, order=order)
        total = cls.total(where)
        return vs, total

    @classmethod
    def get_hostgroup(cls):
        cls._cols = "name"
        cls._tbl = "groups"
        where = 'name REGEXP "^openstack-|^(buy|cdn|pro|buy|3rd|hs|gd|own)0"'
        vs = cls.column(where=where)
        return vs

    @classmethod
    def get_issues(cls):
        issues = api.issues()
        return issues