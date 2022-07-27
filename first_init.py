import sqlite3
from config import set_default_settings, open_table, get_cursor

def isTableExist(cursor, table_name):
  check_exists = f'''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{table_name}';'''
  cursor.execute(check_exists)
  check_res = cursor.fetchone()
  return check_res[0]

def first_init():

  try:
      sqlite_connection = open_table()
      cursor = get_cursor(sqlite_connection)

      table_name = 'search_settings'
      sqlite_create_table_query = f'''CREATE TABLE {table_name} (
                                  id INTEGER PRIMARY KEY,
                                  API text UNIQUE,
                                  lang TEXT NOT NULL);'''
      
      print("База данных подключена к SQLite")
      
      if not isTableExist(cursor, table_name):
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")
        set_default_settings(cursor, sqlite_connection)
        cursor.close()

  except sqlite3.Error as error:
      print("Ошибка при подключении к sqlite", error)
  finally:
      if (sqlite_connection):
          sqlite_connection.close()
          print("Соединение с SQLite закрыто")

