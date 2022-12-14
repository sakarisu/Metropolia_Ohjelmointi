import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3000,
            database='ekolento',
            user='root',
            password='',
            autocommit=True
        )

    def get_conn(self):
        return self.conn
