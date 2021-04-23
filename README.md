# Mario finds princess backend

## How to run the project
**NOTE**: there is no need to create a database, the database is already created `db.game`

The project also contains unit tests to algorithms and utility functions

**All of the project external modules and their versions are in the file `requirements.txt`**
1. Install the `requirements.txt` file with `pip install -r requirements.txt` and `pip install pipenv`
2. Run `pipenv shell` in the root directory of the project
3. Add ` export FLASK_APP=solution` then ` export FLASK_ENV=development` in the console
4. Type `flask run` to start the project

OR

1. Install the `requirements.txt` file with `pip install -r requirements.txt` 
2. Run `python run.py`


## API documentation
### Sending the grid to the backend

**The API is not secured**

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
## Algorithms documentation

`def find_princess(grid,n,start_row, start_column):`

The function takes in `grid` as a 2d array, `n` as integer the size of the grid and the `start_row` and `start_column` as integers
The function returns an array of string `['DOWN','UP','RIGHT']` filled with directions to the shortest path

## Utils documentation

`def route_to_letters(found_route):`

Takes in an array of tuples and returns an string array of taken paths, if empty array is provided the function returns and empty array

`def find_marion_position(matrix):`

Takes in a 2d array and returns a tuple of which row and column Mario is located. Used to get the start position for the `def find_princess(grid,n,start_row, start_column):` function

`def validate_grid(n,grid):`

Takes in `n` integer and `grid` 2d array. It validates the grid if it has only one Mario and only one Princess and returns a bool value

`def to_matrix(array):`

Takes in an array and returns a 2d array






