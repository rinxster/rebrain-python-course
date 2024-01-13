# Задание:
# 1. Вспомним список логов из третьего урока
# May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated
# May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
# May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...
# May 20 11:01:12 PC-00102 PackageKit: daemon start
# May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...
# May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00
# May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"
# May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device
# May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio
# May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.
# May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.
list1 = [
'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
'May 20 11:01:12 PC-00102 PackageKit: daemon start',
'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'
]
print('---5.1---')
print(list1)

# 2. Создайте из него список словарей, используя ключи из того же задания. Напоминаю:
# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>

print('---5.2---')


listdic = []
for number in range(len(list1)):
    string1 = list1[number]
    x = string1.split(" ")
    # 'time': <дата/время>
    time = ''
    for i in range(3):
        time = str(time) + x[0] + ' '
        x.pop(0)
    time=time.strip()

    # 'pc_name': <имя компьютера>
    pc_name = x[0]
    x.pop(0)

    # 'service_name': <имя сервиса>
    service_name = x[0][:-1]
    x.pop(0)

    # 'message': <сообщение лога>
    separator = ' '
    message = separator.join(x)

    my_information = dict({'time': time, 'pc_name': pc_name, 'service_name': service_name, 'message': message})
    listdic.append(my_information)
print(listdic)

# 3. Выведите на экран список значений <дата/время> всех словарей. Воспользуйтесь списковым включением.
print('---5.3---')
print(*[i['time']for i in listdic])

# 4. Измените словари в списке: создайте новый ключ 'date', перенеся в его значение дату из поля 'time'.
# В поле 'time' оставьте только время.
# Выведите значения для поля 'time' всех словарей в списке.
# Пример May 20 12:48:18 -> "'May 20', '12:48:18'"
# //TODO XXX

print('---5.4---')

# запускаем цикл по словарю
# добавляем ключ дата
# берём значение и тайм2, разрезаем его, часть вставляем в дату, в оставшееся отрезаем и вставляем в 'time'

for date in listdic:
    string1 = list1[number]
    x = string1.split(" ")
    time2 = ''
    for i in range(2):
        time = str(time2) + x[0] + ' '
        x.pop(0)
    time2 = time2.strip()

print(date)



# 5. Выведите список значений поля 'message' для всех логов, которые записал ПК с именем 'PC0078'. Воспользуйтесь списковым включением.
print('---5.5---')
print(*[i['message'] for i in listdic if i['pc_name']=='PC0078'])

# 6. Превратите список словарей логов (который вы сделали в задании 2) в словарь. Ключами в нем будут целые числа от 100 до 110, а значениями - словари логов.
print('---5.6---')

iter=99
new_dict = {}
for item in listdic:
   message = item.pop('message')
   iter=iter+1
   new_dict[iter] = message

print(new_dict)

# 7. Выведите на экран словарь лога под ключом 104.
print('---5.7---')
print({key: value for key, value in new_dict.items() if key == 104})