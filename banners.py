# Импорт модулей
import colorama
from colorama import Fore, init
import sys
import time
import os
init()

# Переменные
message = "\033[94m \n -|| Проверка запуска ||- \033[0m"

# Основной класс
class Banners:
    # Баннер, который отображается при запуске программы
    def start_banner(self, version, os, login, password, album_id, group_id):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        Banners.check_files(self, login, password, album_id, group_id)
        print(Fore.BLUE)
        Banners.vkprikol_banner(self)
        print(Fore.GREEN)
        start_message = f"""
Добро пожаловать в программу VKPrikol v{version}!
Перед началом работы с программой, пожалуйста, ознакомьтесь с README.md.
Используемая версия python: {sys.version[:3]}.
Используемая операционная система: {os}.
Для того, чтобы продожить, введите start.
"""
        for char in start_message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

    # Баннер, который отображается при запуске атаки
    def banner_atack(self):
        print(Fore.YELLOW)
        print(""" 
         ____  _             _   _             
        / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
        \___ \| __/ _` | '__| __| | '_ \ / _` |
         ___) | || (_| | |  | |_| | | | | (_| |
        |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                          |___/...""")
        time.sleep(1)
        print("[                    ] \033[94m5%\033[0m")
        time.sleep(0.1)
        print("[=====               ] \033[94m35%\033[0m")
        time.sleep(1)
        print("[==========          ] \033[94m52%\033[0m")
        time.sleep(1)
        print("[====================] \033[94m100%\033[0m")
        time.sleep(2)
        print(Fore.RED)

    def vkprikol_banner(self):
        print(Fore.BLUE)
        print("""
                             \ \   / / | _|  _ \ _ __(_) | _____ | |
                              \ \ / /| |/ / |_) | '__| | |/ / _ \| |
                               \ V / |   <|  __/| |  | |   < (_) | |
                                \_/  |_|\_\_|   |_|  |_|_|\_\___/|_|""")


    def check_files(self, login, password, album_id, group_id):
        green = Fore.GREEN
        red = Fore.RED
        successful = f'{Fore.GREEN}--|| Запуск Успешный ||--'
        if os.path.exists('config.ini') == True:
            print('''
                    ''')
            config = f'{Fore.RED}Config' + ' - ' + f'{Fore.GREEN}[OK]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            time.sleep(2.5)
            if login != None:
                print(f'{red}.login' + f'{green} - [OK]')
                time.sleep(1)
            else:
                print(f'{red}.login' + f'{red} - [FAIL]')
                exit()
            if password != None:
                print(f'{red}.password' + f'{green} - [OK]')
                time.sleep(1)
            else:
                print(f'{red}.password' + f'{red} - [FAIL]')
                exit()
            if group_id != None:
                print(f'{red}.groupID' + f'{green} - [OK]')
                time.sleep(1)
            else:
                print(f'{red}.groupID' + f'{red} - [FAIL]')
                exit()
            if album_id != None:
                print(f'{red}.albumID' + f'{green} - [OK]')
                time.sleep(1)
            else:
                print(f'{red}.albumID' + f'{red} - [FAIL]')
                exit()
        else:
            print('''
                                ''')
            config = f'{Fore.RED}Config' + ' - ' + f'{Fore.RED}[FAIL]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            exit()
        if os.path.exists('requirements.txt') == True:
            print("""""")
            config = f'{Fore.RED}Requirements' + ' - ' + f'{Fore.GREEN}[OK]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
        else:
            print("""""")
            config = f'{Fore.RED}Requirements' + ' - ' + f'{Fore.RED}[FAIL]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            exit()
        print("""
        """)
        for char in successful:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(3)
        os.system('cls')
        os.system('clear')
