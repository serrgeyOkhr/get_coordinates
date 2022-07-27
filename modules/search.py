from config import cls, get_API, get_user_suggestion, get_clean_address

def suggest_search(user_input):
  if user_input.strip() == '': return 0

  suggestion_list = get_user_suggestion(user_input)
  if suggestion_list:
    print("Возможно вы ищите один из этих адресов:")
    for (index, address) in enumerate(suggestion_list, start=1):
      print(f"{index}. {address['value']}")
    print('\nДля получения точных координат адреса введите число, указанное рядом с ним. \n Если искомого адреса нет, уточните поиск')
    return suggestion_list
  else: 
    print("Ошибка связи с сервером")

def final_search(address_data):
  all_data = get_clean_address(address_data['value'])
  print("Координаты места:")
  print(f"Широта: {all_data['data']['geo_lat']}; Долгота: {all_data['data']['geo_lon']}")
  return 1

def search_module ():
  user_API = get_API()
  if user_API == '': 
    print("Вы не задали API ключ. Вы не сможете пользоваться поиском")
    input('Для возврата нажмите любую клавишу...')
    return 0
  while True:
    cls()
    print("Поиск точных координат по адресу.")
    print("Что бы вернуться, введите 0. \nДля поиска введите адрес:")
    user_input = input()
    if user_input.strip() == '0': return 0

    while True:
      if user_input.strip() == '0': break

      delail_addresses = suggest_search(user_input)
      user_input = input()

      if (user_input.isnumeric()) and ((int(user_input) > 0) and (int(user_input) < 11)):
        final_search(delail_addresses[int(user_input)-1])
        input('Нажмите любую клавишу, чтобы продолжить...')
        break