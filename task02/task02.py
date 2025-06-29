# Задание:
# 1. Вы получили такую строку логов:
#
# 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# Совершите над ней следующие действия:
stroka = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

# 1.1. Выделите и выведите на экран дату и время.
print(stroka[0:15])

# 1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.
print(stroka[24:34])

# 1.3. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран.
print(stroka.replace('ideapad', 'PC-12092'))

# 1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
print(stroka.find('failed'))

# 1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).
print(stroka.lower().count('s'))

# 1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
print(sum([int(s) for s in (stroka[6:15].split(':'))]))

# 2. Вы получили такую строку логов:
# 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
# Нужно сформировать и вывести сообщение в таком формате:
#
# The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>" at <дата, время>
stroka2='May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
print(f'The PC "{stroka2[16:23]}" receive message from service "{stroka2[24:35]}" what says "{stroka2[71:93]}" because "{stroka2[37:58]}" at {stroka2[0:15]}')


