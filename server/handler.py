#
#    handler.py
#    server side handler
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

import SocketServer
import subprocess
import config
import netaddr

class PPPSwitchHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        client_ip = netaddr.IPAddress(self.client_address[0])
        
        ip_ranges = config.data['allow'].split(',')
        
        allowed = False
        
        for ip_range in ip_ranges:
            try:
                allowed = client_ip in netaddr.IPNetwork( ip_range.strip() )
            except:
                pass
            
        if allowed:
            self.data = self.request.recv(1024).strip()
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
            if self.data == 'on':
                subprocess.Popen( [ 'rasdial',
                                    config.data['cxn'],
                                    config.data['user'],
                                    config.data['pass'] ],
                                  startupinfo=startupinfo )
            elif self.data == 'off':
                subprocess.Popen( [ 'rasdial',
                                    config.data['cxn'],
                                    '/DISCONNECT' ],
                                 startupinfo=startupinfo )
