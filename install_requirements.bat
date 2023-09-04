@echo off

rem Define el nombre del entorno virtual
set VENV_NAME=myenv

rem Crea el entorno virtual
python -m venv %VENV_NAME%

rem Activa el entorno virtual
call %VENV_NAME%\Scripts\activate

rem Instala las dependencias desde requirements.txt
pip install -r requirements.txt

rem Desactiva el entorno virtual
deactivate
