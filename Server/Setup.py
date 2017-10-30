import sys
from cx_Freeze import setup, Executable

#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

application_title = "chat app"
main_python_file = "ServerGUIMain.py"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit", "re"]

setup(name = application_title,
      version = "1.0",
      description = "My application!",
      options = {"build_exe": {"includes": includes}},
      executables = [Executable(main_python_file, base = base)])