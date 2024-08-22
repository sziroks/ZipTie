DB_URL_PREFIX = "mysql+pymysql://"
DB_HOST = "localhost:3306"
DB_NAME = "zip_tie_schema"

ENV_DB_USER = "DB_USER"
ENV_DB_PASS = "DB_PASS"

TABLE_COLUMNS = {
    "User": ["id_user", "name", "email", "age"],
    "Book": ["id_book", "title", "id_user", "description"],
}
