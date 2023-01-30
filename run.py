# Website Python Run Script
import os

import dotenv

from src import app

if __name__ == "__main__":
    dotenv.load_dotenv()
    app.run(debug=True, host=str(os.environ['HOSTNAME']), port=int(os.environ['PORT']))

