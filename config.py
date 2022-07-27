import os
import sqlite3
from dadata import Dadata

DATABASE_NAME = 'find_address.db'
TABLE_NAME = 'search_settings'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def set_default_settings(this_cursor, connection):
  default_value = f'''INSERT INTO {TABLE_NAME}
                  (id, API, lang)
                  VALUES
                  (1, "", "ru")'''
  this_cursor.execute(default_value)
  connection.commit()

def open_table():
  return sqlite3.connect(DATABASE_NAME)

def get_cursor(connect):
  return connect.cursor()

def get_API():
  SQL_BODY = f''' SELECT API FROM {TABLE_NAME}; '''

  table_connection = open_table()
  cursor = get_cursor(table_connection)
  cursor.execute(SQL_BODY)
  output = cursor.fetchone()
  cursor.close()
  table_connection.close()
  return output[0]

def get_lang():
  SQL_BODY = f''' SELECT lang FROM {TABLE_NAME}; '''

  table_connection = open_table()
  cursor = get_cursor(table_connection)
  cursor.execute(SQL_BODY)
  output = cursor.fetchone()
  cursor.close()
  table_connection.close()
  return output[0]

def set_API(new_API):
  SQL_BODY = f''' UPDATE {TABLE_NAME}
                SET API = '{new_API}'
                WHERE id = 1; '''
                
  table_connection = open_table()
  cursor = get_cursor(table_connection)
  cursor.execute(SQL_BODY)
  table_connection.commit()
  cursor.close()
  table_connection.close()

def set_lang():
  cur_lang = get_lang()
  if cur_lang == 'ru' : new_lang = 'en'
  else                : new_lang = 'ru'

  SQL_BODY = f''' UPDATE {TABLE_NAME}
                SET lang = '{new_lang}'
                WHERE id = 1; '''
                
  table_connection = open_table()
  cursor = get_cursor(table_connection)
  cursor.execute(SQL_BODY)
  table_connection.commit()
  cursor.close()
  table_connection.close()

def get_database():
  token = get_API()
  dadata = Dadata(token)
  return dadata

def get_user_suggestion(input):
  try:
    api_database = get_database()
    language = get_lang()

    return api_database.suggest(name="address", query=input, language=language)
  except:
    return False
def get_clean_address(input):
  api_database = get_database()
  language = get_lang()

  return api_database.suggest(name="address", query=input,language=language, count=1)[0]