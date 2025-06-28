"""
Практическое задание
1. Создайте новый проект, а в нем создайте виртуальное окружение. Задействуйте это окружение.
"""
#python -m venv venv 
"""
2. С помощью пакетного менеджера установите пакет psutil.
"""
#pip install psutil
"""
3. Создайте файл с зависимостями с именем requirements.txt
"""
#PS C:\Users\SadykovR\Documents\rebrain-python-course\task09> more .\requirements.txt
#psutil==7.0.0

#PS C:\Users\SadykovR\Documents\rebrain-python-course\task09>
"""
4. Создайте файл-модуль. Используя модуль os и функцию getlogin, а также модуль psutil и функцию virtual_memory, создайте словарь 
со следующими полями: 'user_name', 'memory_total', 'memory_used' и 'memory_percent' и заполните эти поля данными, полученными из функций.
"""
from os import getlogin
from psutil import virtual_memory
dict1 ={ 'user_name':getlogin(), 'memory_total':virtual_memory().total, 'memory_used':virtual_memory().used, 'memory_percent':virtual_memory().percent}
"""
5. Создайте основной файл проекта. Импортируйте из него ваш созданный
"""
# см файл main.py