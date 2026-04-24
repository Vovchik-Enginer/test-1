# Тестирование командной работы в ГИТ

import random

def greeting():
   print('\nПривет, команда! Сегодня будем работать вместе!')

def motivation_quote():
   quotes = [
      'Команда - это сила!',
      'Каждый коммит приближает нас к успеху!',
      'Git сохраняет все, что мы делаем',
      'Вместе мы - команда мечты'
   ]

   print('Цитата дня:', random.choice(quotes))   

def coin_flip():
   coin = random.randint(0, 1)
   if coin == 0:
      print('Выпала РЕШКА')
   else:
      print('Выпал ОРЕЛ')      

def gess_number():
   secret = random.randint(1, 10)
   print('Угадай число от 1 до 10')
   if gess_number == secret:
      print('Круто! Ты угадал.')
   else:      
      print(f'Не угадал! Было число {secret}')


