import sqlite3, sys

def connect_to_db(path):
  if not path:
    print('DB path is required')
    sys.exit()
  db_connect = sqlite3.connect(path, check_same_thread=False)
  return db_connect.cursor()

