@echo off

CALL ..\venv\Scripts\activate

flask --app __init__ --debug run
