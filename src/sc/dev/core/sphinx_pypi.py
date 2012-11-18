# -*- coding:utf-8 -*-
from zest.releaser import utils as zutils

import ConfigParser
import os


SECTION = 'build_sphinx'


def upload(context):
    ''' Upload sphinx doc'''
    config = ConfigParser.ConfigParser()
    config.read(os.path.join(context['workingdir'], 'setup.cfg'))
    if SECTION not in config.sections():
        return None

    build_command = 'build_sphinx'
    upload_command = 'upload_sphinx'
    if not zutils.ask('Upload documentation to http://packages.python.org'):
        return
    # build documentation
    shell_command = zutils.setup_py(build_command)
    zutils.system(shell_command)

    # upload documentation
    shell_command = zutils.setup_py(upload_command)
    zutils.system(shell_command)
