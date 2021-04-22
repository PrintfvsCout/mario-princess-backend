# Mario finds princess backend

## How to run the project
All of the project external modules and their versions are in the file
1. Install the `requirements.txt` file with `pip install -r requirements.txt` and `pip install pipenv`
2. Run `pipenv shell` in the root directory of the project
3. Add ` export FLASK_APP=solution` then ` export FLASK_ENV=development` in the console
4. Type `flask run` or `python run.py` to start the project

## API documentation
### Sending the grid to the backend
POST http://localhost:5000/sendinput

Endpoint:`/sendinput`

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
### Getting game results 
GET http://localhost:5000/getresults

Endpoint:`/getresults`

Response example
```
[
    {
        "grid": "[\n  \"mx-\",\n  \"-xp\",\n  \"---\"\n]",
        "id": 1,
        "n": 3,
        "path": "DOWN,DOWN,RIGHT,RIGHT,UP",
        "req_date": "2021-04-21T00:00:19.292756"
    },
    {
        "grid": "[\n  \"mx-\",\n  \"-xp\",\n  \"---\"\n]",
        "id": 2,
        "n": 3,
        "path": "DOWN,DOWN,RIGHT,RIGHT,UP",
        "req_date": "2021-04-21T00:00:37.537108"
    }
]
```

### Deleting result by id
DELETE http://localhost:5000/getresults/1

Endpoint `getresults/1`
This endpoint is only used for deleting undesired results 
```
{
    "error_flag": false
}

```


