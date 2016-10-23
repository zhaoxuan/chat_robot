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
import pipes

"""
解压目录里面的字幕
"""

ROOT = '/mnt/sdd1/chat_robot'
OUT_PUT = ROOT + '/zimu_text/'
logging.basicConfig(filename='uncompress.log', level=logging.DEBUG)
COUNTER = 1


def uncompress(file_name):
    name, extension = os.path.splitext(file_name)

    file_path = pipes.quote(ROOT + '/result/' + file_name)

    if extension.lower() == '.zip':
        code, msg = commands.getstatusoutput('7z x %s -yo%s' % (file_path, OUT_PUT))
        if code != 0:
            print file_path
            logging.error(msg)
        else:
            print 'success'
    elif extension.lower() == '.rar':
        code, msg = commands.getstatusoutput('7z x %s -yo%s' % (file_path, OUT_PUT))
        if code != 0:
            print file_path
            logging.error(msg)
        else:
            print 'success'
    else:
        print file_path
        pass


for root, dirs, files in os.walk(ROOT + '/result'):
    for file_name in files:
        uncompress(file_name)
