# learning-flask
Learning Flask

### Setup


Setup the environment:

`python3 -m venv .venv`

OSX / Linux:
`source .venv/bin/activate`

Windows:

`\.venv\Scripts\activate.bat`

Install dependencies:

`pip install -r requirements.txt`


### Run

If you are on Windows make sure to use `set` instead of export.

Windows:
```
set FLASK_APP=app.py
set FLASK_ENV=development
python -m flask run
```

Linux / OSX:
```
export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```



