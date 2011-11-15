#
#    register.py
#    add/remove server to windows start
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

import _winreg
import sys
import os.path

sub_key = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
sub_value = 'RemotePPPSwitcher'



def add():
    try:
        key = _winreg.OpenKey( _winreg.HKEY_LOCAL_MACHINE,
                               sub_key,
                               0,
                               _winreg.KEY_SET_VALUE )
        _winreg.SetValueEx( key,
                            sub_value,
                            0,
                            _winreg.REG_SZ,
                            '"%s"' %os.path.abspath( sys.argv[0] ))
    except:
        pass
                     

def remove():
    try:
        key = _winreg.OpenKey( _winreg.HKEY_LOCAL_MACHINE,
                               sub_key,
                               0,
                               _winreg.KEY_SET_VALUE )
        _winreg.DeleteValue( key,
                             sub_value )
    except:
        pass
