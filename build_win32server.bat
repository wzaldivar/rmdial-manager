cx_freeze_setup_switcherd.py build
copy remote_ppp_switcherd.cfg build\exe.win32-2.6\
copy gpl.txt build\exe.win32-2.6\
mkdir remote_ppp_switcherd
move build\exe.win32-2.6\*.* remote_ppp_switcherd\
