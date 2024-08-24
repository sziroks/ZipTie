# Database configuration
DB_URL_PREFIX = "mysql+pymysql://"
DB_HOST = "localhost:3306"
DB_NAME = "zip_tie_schema"

# Environment variable names for database credentials
ENV_DB_USER = "DB_USER"
ENV_DB_PASS = "DB_PASS"

# Not the perfect solution. More info in *crud_handler.py* line 30
TABLE_COLUMNS = {
    "User": ["name", "email", "age"],
    "Book": ["title", "id_user", "description"],
}

# Pagination page configuration
ROWS_PER_PAGE = 10
