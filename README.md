# Mario finds princess backend

## How to run the project
All of the project external modules and their versions are in the file
1. Run `pipenv shell` in the root directory of the project
2. Install the `requirements.txt` file with `pip install -r requirements.txt`
3. Add ` export FLASK_APP=solution` then ` export FLASK_ENV=development` in the console
4. Type `flask run` or `python run.py` to start the project

## API documentation
Sending grid to the backend
POST http://localhost:5000/sendinput

Request
```
Body:{
    "n":"3",
    "grid":"['--m', '-x-', '-p-']"
}
```
Succesful Response
```
{
    "error_flag": false,
    "paths": [
        "RIGHT",
        "DOWN",
        "DOWN"
    ]
}
```
Request
```
Body:{
    "n":"3",
    "grid":"['---', '-x-', '-p-']"
}

```
Failed Response
```
{
    "error_flag": true
}
```
