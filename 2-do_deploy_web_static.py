#!/usr/bin/python3
from os.path import exists
from fabric.operations import put, run
from fabric.api import env
"""
deploy to web server
"""

env.hosts = [
            '34.74.29.106',
            '35.237.30.103'
        ]


def do_pack():
    """
    packs web_static content into a
    .tgz file """
    time = datetime.now()
    str_date = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        return local("tar -cvzf versions/web_static_{}.tgz web_static"
                     .format(str_date))
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """ deploy to web server """
    if not exists(archive_path):
        return False
    new_dir = '/data/web_static/releases/{}'.format(archive_path.split(".")[0])
    f = archive_path.split('/')[-1]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.
             format(new_dir))
        run('tar -xzf /tmp/{} -C {}'.
            format(f, new_dir))
        run('rm /tmp/{}'.format(f))
        run('mv {}/web_static/* {}{}/'.format(new_dir, new_dir))
        run('rm -rf {}/web_static'.format(new_dir))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(new_dir))
    except Exception:
        return False
    return True
