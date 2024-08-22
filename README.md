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
