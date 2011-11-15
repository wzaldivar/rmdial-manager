#! /usr/bin/python

#
#    remote_ppp_switcher.py
#    client side application
#
#    Copyright (C) 2011 Walber Zaldivar <walber.zaldivar@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import client.client
import sys

def send(data):
    client.client.send(data)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            send('on')
        elif sys.argv[1] == 'stop':
            send('off')

