# -*- coding:utf-8 -*-
import ConfigParser
import glob
import os
import zest.releaser.utils

SECTION = 'build_sphinx'

def upload(context):
    ''' Upload sphinx doc'''
    config = ConfigParser.ConfigParser()
    config.read(os.path.join(context['workingdir'], 'setup.cfg'))
    if SECTION not in config.sections():
        return None
    
    build_command = 'build_sphinx'
    upload_command = 'upload_sphinx'
    if not zest.releaser.utils.ask('Upload documentation to http://packages.python.org'):
        return
    # build documentation
    shell_command = utils.setup_py(build_command)
    result = zest.releaser.utils.system(shell_command)
    
    # upload documentation
    shell_command = utils.setup_py(upload_command)
    result = zest.releaser.utils.system(shell_command)
    
