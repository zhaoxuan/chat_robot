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

import chardet
import os
import commands
import logging

logging.basicConfig(filename='character.log', level=logging.DEBUG)

ROOT = './zimu_cleaned'

INDEX = 0

for root, dirs, files in os.walk(ROOT):
    for file_name in files:
        file_path = root + "/" + file_name
        out_path = './zimu_utf8/' + file_name
        f = open(file_path, 'r')
        data = f.read()
        encoding = chardet.detect(data)["encoding"]
        f.close()

        code, msg = commands.getstatusoutput('iconv -f %s -t UTF-8 -o \'%s\' \'%s\'' % (encoding, out_path, file_path))

        if code != 0:
            print 'Except: %s' % (file_path)
            logging.error(msg)
