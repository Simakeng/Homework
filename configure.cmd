@echo off

REM if Python is installed
python -V > NUL
IF not %ERRORLEVEL% == 0 GOTO PYTHON_NOT_INSTALL

REM execute configure file
cd %~dp0
python tools\configure.py %1 %2 %3 %4 %5 %6

REM check configure status
IF not %ERRORLEVEL% == 0 GOTO FAIL

REM finished
GOTO LB_EXIT

:PYTHON_NOT_INSTALL
ECHO Python is not installed.
ECHO Please install python to continue

:FAIL
echo Makefile not created.

:LB_EXIT