#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (C) 2016 John Zhao
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import commands
import logging

"""
解压目录里面的字幕
"""

ROOT = '/Users/john/workspaces/python/zimuku_crawl'
OUT_PUT = ROOT + '/zimu_text/'
logging.basicConfig(filename='uncompress.log', level=logging.DEBUG)
status, output = commands.getstatusoutput('ls result/')


def uncompress(file_name):
    name, extension = os.path.splitext(file_name)

    file_path = ROOT + '/result/' + file_name

    if extension.lower() == '.zip':
        code, msg = commands.getstatusoutput('unzip -o \'%s\' -d %s' % (file_path, OUT_PUT))
        if code != 0:
            logging.info(file_name)
        pass
    elif extension.lower() == '.rar':
        code, msg = commands.getstatusoutput('unrar x -y \'%s\' %s' % (file_path, OUT_PUT))
        if code != 0:
            logging.info(file_name)
        pass
    else:
        pass


for file_name in output.split('\n'):
    uncompress(file_name)