#!/usr/bin/python3

from datetime import datetime
from fabric.operations import local

"""
packs everything inside the web_static folder
"""


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
