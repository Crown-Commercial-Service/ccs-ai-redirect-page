# CCS AI Redirect Page

A simple Flask application that serves a UI to redirect users from an old app version to a new URL.

## Configuration

The app requires a `.env` file in the root directory with the following variable:

`REDIRECT_LINK`: The destination URL where users will be sent.



**Example `.env`:**
```env
REDIRECT_LINK=www.google.com
```
## Installation
In your command prompt type the commands below:
```
1. git clone <your-repo-url>
2. cd <repo-name>
```

Once repo has been cloned you will need to install all the packages:
```
pip install -r requirements.txt
```
## Run application 
```
python redirect.py
```