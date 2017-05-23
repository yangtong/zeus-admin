# -*- coding:utf-8 -*-
__author__ = 'yangtong'
from web import app
from flask import request, jsonify, render_template
from frame.store import db
from web.model.template import Template
from web.model.action import Action
from frame import utils


@app.route('/api/version')
def api_version():
    return '2.0.0'


@app.route('/api/health')
def api_health():
    return 'ok'


@app.route('/api/uic/group')
def api_query_uic_group():
    q = request.args.get('query', '').strip()
    limit = int(request.args.get('limit', '10'))
    return jsonify(data=uic.query_group(q, limit))


@app.route('/api/template/query')
def api_template_query():
    q = request.args.get('query', '').strip()
    limit = int(request.args.get('limit', '10'))
    ts, _ = Template.query(1, limit, q)
    ts = [t.to_json() for t in ts]
    return jsonify(data=ts)


@app.route('/api/template/<tpl_id>')
def api_template_get(tpl_id):
    tpl_id = int(tpl_id)
    t = Template.get(tpl_id)
    if not t:
        return jsonify(msg='no such tpl')

    return jsonify(msg='', data=t.to_json())


@app.route('/api/action/<action_id>')
def api_action_get(action_id):
    action_id = int(action_id)
    a = Action.get(action_id)
    if not a:
        return jsonify(msg="no such action")

    return jsonify(msg='', data=a.to_json())


@app.route('/api/metric/query')
def api_metric_query():
    q = request.args.get('query', '').strip()
    limit = int(request.args.get('limit', '10'))
    names = utils.metric_query(q, limit)
    names.append(q)
    return jsonify(data=[{'name': name} for name in names])


@app.route('/api/pings')
def api_pings_get():
    names = db.query_column("select hostname from host")
    return jsonify(hosts=names)


@app.route('/api/debug')
def api_debug():
    return render_template('debug/list.html')
