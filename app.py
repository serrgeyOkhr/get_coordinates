from config import cls as clean_console
from modules.search import search_module
from modules.settings import setting_module

def run_app():
  clean_console()
  print("Добро пожаловать в поисковик адрессов!")

  while True:
    print(f"Выберите действие и введите число: \n 1. Перейти в настройки \n 2. Перейти в поиск \n для выхода введите 'выход, exit или 0'")
    user_input = input()

    if (user_input == 'выход') or (user_input == 'exit') or (user_input == '0'):
      return True

    if (user_input == '1'):
      clean_console()
      setting_module()
      clean_console()
      continue

    if user_input == '2':
      clean_console()
      search_module()
      clean_console()
      continue

    else: 
      clean_console()
      print("Не верный ввод! Попробуйте еще раз.")
      # input()
      continue
  