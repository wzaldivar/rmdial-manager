#
#    cx_freeze_setup_switcherd.py
#    cx_Freeze setup for remote_ppp_switcherd
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

from cx_Freeze import setup, Executable

setup(
        name = "remote_ppp_switcherd",
        version = "0.2.2",
        description = "remote ppp switcher server",
        executables = [Executable('remote_ppp_switcherd.py',
                                   base = 'Win32GUI')])

