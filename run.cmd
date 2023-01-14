@echo off

CALL venv\Scripts\activate

flask --app src\__init__ --debug run
