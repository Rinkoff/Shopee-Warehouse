import mysql.connector as conn
from DB.read_db_config import read_db_config
class DB:
    def __init__(self):

        db_config = read_db_config("../config.ini","MySQL")

        try:
            self.connector = conn.connect(
                user=db_config["user"],
                password=db_config["password"],
                database=db_config["database"],
                host=db_config["host"],
                port=db_config["port"]
            )
        except conn.Error as error:
            print(error)

        