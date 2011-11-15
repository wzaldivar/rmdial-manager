cx_freeze_setup_switcher.py build
copy remote_ppp_switcher.cfg build\exe.win32-2.6\
copy gpl.txt build\exe.win32-2.6\
mkdir remote_ppp_switcher
move build\exe.win32-2.6\*.* remote_ppp_switcher\
