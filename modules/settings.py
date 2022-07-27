from config import cls, set_API, set_lang, get_API, get_lang


def isNewAPICorrect(API):

  print(f"Подтвердите запись API ключа: {API} (y/n)")
  user_input = input()

  if user_input == "y": return True
  else:                 return False

def setting_module ():
  while True:
    cls()
    print("Настройки:")
    print("1. Ввод API key")
    print("2. Просмотр текущего API key")
    print("3. Выбор языка (en/ru)")
    print("0. Назад")
    user_input = input()

    if user_input == '0': return 0

    if user_input == '1':
      print("Введите новый API ключ:")
      new_API = input()
      if isNewAPICorrect(new_API):
        set_API(new_API)

    if user_input == '2':
      print("Текущий API ключ:")
      print(get_API())
      input()

    if user_input == '3':
      print("Выбран язык:")
      print(get_lang())
      print("Сменить язык? (y/n | д/н)")
      change_lang_input = input()
      if change_lang_input == 'y' or change_lang_input == 'д':
        set_lang()