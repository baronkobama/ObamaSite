@echo off

Rem activating the virtual environment
if exist "venv\Scripts\" (
    CALL venv\Scripts\activate
) else (
    if exist "venv\bin\" (
	CALL venv\bin\activate
    ) else (
	echo "venv not found, exiting script..."
	exit 1
    )
)

Rem making environment variables in '.env' usable
setlocal
FOR /F "tokens=*" %%i in ('type .env') do SET %%i

Rem running the app, HOSTNAME and PORT must be set in a '.env' file that follows this format:
Rem HOSTNAME=127.0.0.1
Rem PORT=5000
flask --app src\__init__ --debug run -h %HOSTNAME% -p %PORT%

endlocal

