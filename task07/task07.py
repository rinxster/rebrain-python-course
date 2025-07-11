# Задание:
# 1. Вам дан тот самый, уже полюбившийся вам список логов из 3, 5 или 6 блока:

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


# 2. Напишите функцию, которая:

# 2.1. Получает в качестве первого аргумента список для вывода данных, а в качестве последующих - сколько угодно строк логов
# по типу тех, что есть в скопированном вами списке.
print('----2.1----')
def func21(outlist, *strings):
    print(outlist)
func21(list1)


# 2.2. Превращает вводимые вами строки логов в словари по тому же принципу, что и в пункте 2 задания для 3го блока. Напоминаю:
# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>

print('----2.2----')
def func22(list):
    listdic = []
    for number in range(len(list)):
        string1 = list[number]
        x = string1.split(" ")
        # 'time': <дата/время>
        time = ''
        for i in range(3):
            time = str(time) + x[0] + ' '
            x.pop(0)
        time = time.strip()

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
    # return listdic
    print(listdic)
    return

func22(list1)



print('----2.3----')
# 2.3. Модифицирует входной список (переданный в качестве первого аргумента), добавляя в него все созданные словари.
# Возвращать функция, соответственно, должна None

#ЗАДАНИЕ НЕПОНЯТНО! ТРЕБУЕТСЯ ПОЯСНЕНИЕ!


print('----2.4----')
# 2.4. Создайте пустой список и добавьте в него 1ю, 2ю и 4ю запись из списка логов с помощью одного вызова вашей функции.
# Выведите полученный список на экран



def task24(*linefromlogs):
    list24= []
    for n in linefromlogs:
        #print(list1[n])
        list24.append(list1[n])
    print(list24)

task24( 0, 1, 3)

print('----3----')
# 3. Скопируйте к себе этот модифицированный список из 4го блока, отображающий количество общей и занятой памяти на
# накопителях:
# [
#     {'id': 382, 'total': 999641890816, 'used': 228013805568},
#     {'id': 385, 'total': 61686008768, 'used': 52522710872},
#     {'id': 398, 'total': 149023482194, 'used': 83612310700},
#     {'id': 400, 'total': 498830397039, 'used': 459995976927},
#     {'id': 401, 'total': 93386008768, 'used': 65371350065},
#     {'id': 402, 'total': 988242468378, 'used': 892424683789},
#     {'id': 430, 'total': 49705846287, 'used': 9522710872},
# ]

# 4.  Напишите функцию, которая:
# 4.1. Получает этот список
# 4.2. Анализирует состояние памяти каждого накопителя по алгоритму из задания для 4го блока. Напоминаю:
# Если свободной памяти осталось меньше 10Гб или меньше 5%, то на накопителе критически мало свободного места;
# Если свободной памяти больше, чем в предыдущем пункте, но меньше 30Гб или меньше 10%, то на накопителе мало свободного места;
# Иначе на накопителе достаточно свободного места

print('------3/4.1/4.2-----')
list2 = [
        {'total': 999641890816, 'used': 228013805568},
        {'total': 61686008768, 'used': 52522710872},
        {'total': 149023482194, 'used': 83612310700},
        {'total': 498830397039, 'used': 459995976927},
        {'total': 93386008768, 'used': 65371350065},
        {'total': 988242468378, 'used': 892424683789},
        {'total': 49705846287, 'used': 9522710872},
    ]

def analyzelist(list):
    for number in range(len(list)):
        # print(number)
        # number = int(input())
        free_b = list[number]['total']-list[number]['used']
        free_p = ((list[number]['total']-list[number]['used'])/list[number]['total'])*100
        if ((free_b < 10737418240) or free_p < 5):
            print('на накопителе '+str(number)+' критически мало свободного места')
        elif ((free_b < 32212254720) or free_p < 10):
            print('на накопителе '+str(number)+' мало свободного места')
        else:
            print('на накопителе '+str(number)+' достаточно свободного места')

analyzelist(list2)

# 4.3. Формирует словарь, ключами которого являются: 'memory_ok', 'memory_not_enough' и 'memory_critical',
# а значениями - списки id накопителей, состояние которых относится к соответствующему ключу
# (достаточно свободного места, мало свободного места и критически мало свободного места соответственно).
# 4.4. Возвращает сформированный словарь.
# 5. Примените эту функцию к вашему списку и выведите словарь, полученный в результате ее работы, на экран.

print('----4.3/4.4/5-----')

def createdict(list):
    dictdisk={}
    for number in range(len(list)):
        # print(number)
        # number = int(input())
        free_b = list[number]['total'] - list[number]['used']
        free_p = ((list[number]['total'] - list[number]['used']) / list[number]['total']) * 100
        if ((free_b < 10737418240) or free_p < 5):
            dictdisk[number]='memory_critical'
        elif ((free_b < 32212254720) or free_p < 10):
            dictdisk[number]='memory_not_enough'
        else:
            dictdisk[number]='memory_ok'
    return dictdisk
print(createdict(list2))
