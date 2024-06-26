from .StockServices import StockServices

import pymysql
"""
    In this script we are going to call
    the sql sentences for the db
"""
class StockCrud(StockServices):
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self._connection_db = None

    def init_connection_db(self) -> None:
        self._connection_db = pymysql.connect(host='localhost', port=3309, user='root', passwd='', database=self._db_name, cursorclass=pymysql.cursors.DictCursor)

    def close_connection_db(self) -> None:
        self._connection_db.commit()
        self._connection_db.close()