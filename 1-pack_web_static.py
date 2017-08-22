#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from contents of web_static
"""
from datetime import datetime
from fabric import operations


def do_pack():
    """
    Function do_pack to generate the .tgz archive
    """
    # Create versions/ if it doesn't exist
    operations.local("mkdir -p ./versions")

    # format of file to be made:
    # web_static_<year><month><day><hour><minute><second>.tgz
    format = "%Y%m%d%H%M%S"
    file_time = datetime.utcnow().strftime(format)
    file_name = "web_static_"
    file_name += file_time
    file_name += ".tgz"

    # Create the .tgz archive
    result = operations.local(
        "tar --create --verbose -z --file='./versions/{}' web_static".format(
            file_name))

    # If archive was made, return. If not, return None
    if result is not None:
        return result
    else:
        return None
