#!/bin/bash

# activating the virtual environment
if [ -d "venv/bin" ]; then
    source venv/bin/activate
elif [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
else
    echo "venv not found, exiting script..."
    exit 1
fi

# making environment variables in '.env' usable
set -a
source .env
set +a

# running the app, $HOSTNAME and $PORT must be set in a '.env' file that follows this format:
# HOSTNAME=127.0.0.1
# PORT=5000
flask --app src/__init__ --debug run -h $HOSTNAME -p $PORT

