@echo off

f:
cd F:\PythonProject

rem git init
rem git remote add gitee https://gitee.com/Cacho/PythonProject.git
rem git remote add github https://github.com/Cachozeng/PythonProject.git

REM git pull github master
git add .
git commit -m "add PythonProject folder"
git push gitee master
git push github master

pause