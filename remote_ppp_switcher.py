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

import sys
import socket
import ConfigParser
import os.path

class client:
    """
    Remote ppp switcher client class
    """

    __config_data = {
                     'ip'   : '192.168.0.1',
                     'port' : 1551
                     }


    def __init__(self, file_path=None, command=None):
        self.config(file_path)

        if command:
            self.do(command)


    def config(self, file_path=None):
        """
        Read configuration file
        """

        if not file_path:
            file_path = os.path.join( os.path.dirname(__file__),
                                      'remote_ppp_switcher.cfg' )

        my_parser = ConfigParser.ConfigParser(self.__config_data)
        my_parser.read( [file_path] )

        self.__config_data['ip'] = my_parser.get('data', 'ip')
        self.__config_data['port'] = my_parser.getint('data', 'port')


    def do(self, command):
        """
        Send command to the server
        """

        command_data = {
                        'start' : 'on',
                        'stop'  : 'off'
                        }

        if command in command_data.keys():
            server_address = ( self.__config_data['ip'],
                               self.__config_data['port'] )
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_socket.connect(server_address)
            my_socket.send(command_data[command])
            my_socket.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        client( command=sys.argv[1] )
