@echo off

rem Establece la ruta al entorno virtual de Python
set VENV_PATH=SoundEmotionVenv

rem Activa el entorno virtual
call %VENV_PATH%\Scripts\activate

rem Ejecuta el programa deseado
python main.py


rem Desactiva el entorno virtual (opcional)
deactivate
