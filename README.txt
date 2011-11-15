Server
======

remote_ppp_switcherd.exe/py install
add remote_ppp_switcherd to Windows startup

remote_ppp_switcherd.exe/py remove
remove remote_ppp_switcherd from Windows startup

remote_ppp_switcherd.exe/py
start server

config file: remote_ppp_switcherd.cfg

values

ip = IP to listen on, default 192.168.0.1
port = port to listen on, default 1551
cxn = dialup connection name
user = dialup connection user
pass = dialup connection password

Client
======

remote_ppp_switcher.exe/py start
command server to connect dialup connection

remote_ppp_switcher.exe/py stop
command server to disconnect dialup connection

config file: remote_ppp_switcher.cfg

values

ip = server IP, default 192.168.0.1
port = server port, default 1551
