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
import logging

ROOT = './'
path = ROOT + '/zimu_text'
logging.basicConfig(filename='clean_subtitle.log', level=logging.DEBUG)

for root, dirs, files in os.walk(path):
    for file_name in files:
        name, extension = os.path.splitext(file_name)

        if extension.lower() in ['.sub', '.txt', '.srt', '.ass']:
            old_file = root + '/' + file_name
            new_file = './zimu_cleaned/' + file_name
            os.rename(old_file, new_file)
