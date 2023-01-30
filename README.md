# ObamaSite

This website is made for the purpose of displaying information about myself, etc.

## Usage

---

You must create a .env file that follows the structure below:

```dotenv
HOSTNAME=127.0.0.1 # set this to the private/public IP address to host the site on
PORT=5000 # set this to whatever port you want to utilize for accessing the site
```

---

### Directory Structure Outline:

```
- src: holds all website files
  - pages: holds all HTML pages
  - static: holds all other files (css, fonts, imgs, js, scss, etc.)
  - \_\_init__.py: all code responsible for running the website
- run.cmd: runs the flask server [Windows] (RECOMMENDED)
- run.sh: runs the flask server [Linux] (RECOMMENDED)
- run.py: runs the flask server (NOT RECOMMENDED)
```

