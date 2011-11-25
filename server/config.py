#
#    config.py
#    server side config
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

import ConfigParser
import os.path
import sys

data = {
        'ip'    : '192.168.0.1',
        'port'  : 1551,
        'cxn'   : 'MyISP',
        'user'  : 'MyUserName',
        'pass'  : 'MyPassword',
        'allow' : '127.0.0.1, 192.168.0.0/24'
        }

config_path = os.path.join( os.path.dirname( os.path.abspath( sys.argv[0] ) ),
                            'remote_ppp_switcherd.cfg' )

def read():
    parser = ConfigParser.ConfigParser(data)
    parser.read( [config_path] )
    data['ip'] = parser.get('data', 'ip')
    data['port'] = parser.getint('data', 'port')
    data['cxn'] = parser.get('data', 'cxn')
    data['user'] = parser.get('data', 'user')
    data['pass'] = parser.get('data', 'pass')
    data['allow'] = parser.get('data', 'allow')

