# Задание:
# У вас есть несколько строк лога:
#
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


# 1. Скопируйте их к себе и создайте из них список (список строк).

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

# for pr in list1:
#     print(pr.count(" "))

# 2.1. Создайте алгоритм заполнения словаря, подходящий для любой строчки лога. Словарь должен содержать в себе такую информацию:
#
# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>
# Еще раз обращаю ваше внимание на то, что алгоритм заполнения должен быть универсальным для всех данных строк.
print('------------------2.1-------------------')

number = int(input())
string1=list1[number]
x = string1.split(" ")
print(x)
# 'time': <дата/время>
time2=''
for i in range(3):
    time2 = str(time2) + x[0] +' '
    x.pop(0)
print(time2)

# 'pc_name': <имя компьютера>
pc_name = x[0]
x.pop(0)
print(pc_name)

# 'service_name': <имя сервиса>
service_name = x[0][:-1]
x.pop(0)
print(service_name)

# 'message': <сообщение лога>
separator = ' '
message = separator.join(x)
print(message)

my_information = dict({'time': time2  ,'pc_name': pc_name,'service_name':service_name, 'message': message})
print(my_information)



# 2.2. Заполните словарь для одной из строк лога с помощью данного алгоритма, запросив у пользователя номер строки с помощью input().
# Выведите на экран информацию из текущего словаря в таком виде:
# <имя компьютера>: <сообщение>

print('------------------2.2-------------------')

number2 = int(input())
string2=list1[number2]
x = string2.split(" ")
# 'time': <дата/время>
time2=''
for i in range(3):
    time2 = str(time2) + x[0] +' '
    x.pop(0)

# 'pc_name': <имя компьютера>
pc_name = x[0]
x.pop(0)

# 'service_name': <имя сервиса>
service_name = x[0][:-1]
x.pop(0)

# 'message': <сообщение лога>
separator = ' '
message = separator.join(x)

my_information2 = dict({'time': time2  ,'pc_name': pc_name,'service_name':service_name, 'message': message})
print('----# <имя компьютера>: <сообщение>---------')
print(my_information2['pc_name'] +' : '+  my_information2['message'])

# 3.1. Скопируйте к себе литерал списка:

# ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

var31 = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

# 3.2. Создайте список ключей из пункта 2.1
var32 = ['time', 'pc_name', 'service_name', 'message']

# 3.3. Используя функцию zip(), создайте словарь из этих двух списков
print('------------------3.3-------------------')
dict_1 = dict(zip(var32, var31))
print(dict_1)

# 4. Создайте список словарей: из словаря, который вы получили в пункте 2 и
# словаря из пункта 3 (в итоге у вас должен получиться список, состоящий из двух словарей). Выведите полученный список на экран
print('------------------4-------------------')

data = [ my_information2 , dict_1]
print(data)

# 5. Используя преобразование во множество, выведите список совпадающих значений полученных словарей.
print('------------------5-------------------')

print(set(my_information2.values()) & set(dict_1.values()))
