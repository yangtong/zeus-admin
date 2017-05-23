zeus portal
============


## Install dependency

    # yum install -y python-virtualenv

    $ cd /letv/zeus
    $ virtualenv ./env

    # use douban pypi
    $ ./env/bin/pip install -r pip_requirements.txt -i http://pypi.douban.com/simple


## Init database and config

- database schema: scripts/schema.sql
- database config: frame/config.py

## Start

    $ ./env/bin/python wsgi.py

    --> goto http://127.0.0.1:5051


## Run with gunicorn

    $ . env/bin/activate
    $ bash run.sh
    
    --> goto http://127.0.0.1:5051


