# ZipTie

## Task Description
The goal of this task is to create a fully working API solution based on Python FastAPI and a
MySQL database.

Your project needs to meet the following requirements:
- The database needs to contain at least 2 tables connected with one-to-many
relationships (remember to create foreign key(s)).
- The tables should have at least 4 columns each and a properly defined primary key.
- All of the columns should be of the minimal possible size (and type) for their purpose.
- The tables should be mapped using SQLAlchemy ORM models.
- The API should have at least 3 endpoints defined:
    - Adding records into table 1.
    - Adding records into table 2.
    - Reading records from table 1 after joining corresponding data from table 2.
- The endpoints should have defined input and response models and basic data validation
logic.
- All of the database operations within endpoints should utilize SQLAlchemy ORM models.
- The endpoint responsible for reading the data should support pagination.
- requirements.txt should be generated.
- Docstrings are optional, but welcomed.

Please upload your solution to a public repository and send us a link to it.
Good luck!

## Requirements
Every library and its version is defined in requirements.txt. You can install required libraries using
```bash
pip install -r requirements.txt
```

On top of that you should have defined 2 environment variables:
- **DB_USER** containing username for database connection
- **DB_PASS** containing password for database connection

# Solution
I've decided to go with users and books, like in a library. Each user can have multiple books, but each book can have only 1 user. This was my initial setting for the API.

## Database tables
1. **users** - table containing users:
    - id_user - primary key
    - name - name of the user
    - email - email of the user
    - age - age of the user
2. **books** - table containing books:
    - id_book - primary key
    - id_user - foreign key
    - title - book title
    - description - book description

To handle each table I've created models:
- **User** - an instance of users table
- **Book** - an instance of books table

## CRUD operations
I've handled 2 CRUD operations:
- create - creates a new user or book record
- read - reads a book record with it's user (join)

## API
I have implemented 3 endpoints:
1. POST /create-user: Creates a new user. Requires body parameters:
    - name: str
    - age: None | int
    - email: str
    
    Returns status codes:
    - 201 if successfull
    - 422 if bad request
    - 500 if server error
2. POST /create-book: Creates a new book. Requires body parameters:
    - title: str
    - id_user: int
    - description: None | str

    Returns status codes:
    - 201 if successfull
    - 422 if bad request
    - 500 if server error
3. GET /books-and-users: Retrieves a list of books and their owners (users). Requires body parameters:
    - page: int

    Returns status codes:
    - 200 if successfull
    - 422 if bad request
    - 500 if server error


## Things to change
This code has some things that I'd personally change. Firstly some proper exception handling should be done. For now I added only key exceptions, to not spend much time, everything else is just a simple
```python
try:
    # some code
except Exception
    # some code
```

It is not optimal, because ```Exception``` has wide scope. 

The second thing I'd change if I had more free time is proper config file. For now things like database url are in consts, whereas I belive that it should be done in configuration file. It allows for simpler changes.

The last thing that is to change is to add logger. For now there is no logger to this API (except default uvicorn logger). Adding custom logger would allow for easier debuging and real time information about application state and request-response operations.

Why i didn't implement these thing? Free time is a comodity and I'd rather spend it working on my own things :D. Right now I'm starting the process of designing and building my own robot, so theres lots of things that I need to take care of. 