@echo off

CALL ..\venv\Scripts\activate

set FLASK_APP=main
set FLASK_ENV=development

flask run
