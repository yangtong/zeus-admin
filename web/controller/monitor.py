# -*- coding:utf-8 -*-
__author__ = 'yangtong'
from web import app
from flask import render_template, request, g
from web.model.monitor import Monitor


hostgroups = Monitor.get_hostgroup()

item_keys = {1: ['system.cpu.util[,idle,avg1]', 1, 'cpu idle'],
             2: ['system.cpu.util[,iowait,avg1]', 1, 'cpu iowait'],
             3: ['vfs.dev.read[,ops]', 1, 'read ops'],
             4: ['system.cpu.load[,avg1]', 1, 'load 1 min'],
             5: ['system.cpu.load[,avg15]', 1, 'load 15 min'],
             6: ['system.swap.size[,pused]', 1, 'swap percent'],
             7: ['vfs.fs.inode[/var,pused]', 1, '/var percent'],
             8: ['vfs.fs.inode[/,pused]', 1, '/ percent'],
             9: ['vfs.fs.inode[/letv,pused]', 1, '/letv percent'],
             10: ['net.if.in[br-int,bytes]', 1, 'br-int traffic'],
             11: ['net.if.in[br-bond1,bytes]', 1, 'br-bond1 traffic'],
             12: ['net.if.in[br0,bytes]', 1, 'br0 traffic'],
             13: ['net.if.in[br-int,dropped]', 1, 'br-int drop'],
             14: ['net.if.in[br-bond1,dropped]', 1, 'br-bond1 drop'],
             15: ['net.if.in[br0,dropped]', 1 ,'br0 drop'],
             16: ['check.netstat.closed', 2, 'closed netstat'],
             17: ['check.netstat.estab', 2, 'estab netstat'],
             18: ['check.netstat.synrecv', 2, 'sysrecv netstat'],
             19: ['system.uptime', 2, 'uptime'],
             20: ['vm.memory.size[free]', 2, 'free memory'],
             21: ['system.swap.size[,used]', 2, 'swap used']}

@app.route('/monitor')
def monitor_home_get():
    return render_template(
        'monitor/index.html',
        data={
            'hostgroups': hostgroups,
        }
    )


@app.route('/monitor/toplist/<k_id>/<hg>')
def monitor_list_get(k_id, hg):
    tbl_name = ['ip', 'itemid', 'key', 'time', 'data', 'unit']
    page = int(request.args.get('p', 1))
    limit = int(request.args.get('limit', 10))
    k_id = int(k_id)
    hg = hg
    item_key = item_keys[k_id][0]
    type = item_keys[k_id][1]
    item_kv = zip()
    vs, total = Monitor.query(hg, item_key, type, page, limit)
    return render_template(
        'monitor/list.html',
        data={
            'hostgroups': hostgroups,
            'hg': hg,
            'tbl_name': tbl_name,
            'k_id': str(k_id),
            'item_kv': [(i[0], i[1][2]) for i in item_keys.items()],
            'item_key': item_key,
            'vs': vs,
            'total': total,
            'limit': limit,
            'page': page,
        }
    )