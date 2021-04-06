__version__ = 1.0
__author__ = 'Kewsen'

import os
import sys
import time


def main(login, password, groupID, albumID):
    with open('config.ini', 'w') as file:
        file.write(f'''
[VK]
login = {login}
password = {password}
groupID = {groupID}
albumID = {albumID}
            ''')
    print('Генерация файла конфигурации завершена. Вы всегда можете отредактировать его вручную.')
    os.system('pip3 install -r requirements.txt')


def clear():
    if sys.platform != 'linux':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    print('Добро пожаловать в программу установки программы VKPrikol!')
    time.sleep(0.5)
    print('Для того, чтобы начался процесс установки, введите ваши данные.')
    try:
        main(
            login=input('Введите логин: '),
            password=input('Введите пароль: '),
            groupID=input('Введите ID группы: '),
            albumID=input('Введите ID альбома: ')
        )
    except KeyboardInterrupt:
        print('Выход из программы установки.')
        exit()
