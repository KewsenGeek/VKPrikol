# Импорт модулей
import colorama
from colorama import Fore, init
from tqdm import tqdm
import sys
import time
import os
import vk_api
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
        time.sleep(3)
        print('')
        print('Фотографии подготавливаются к загрузке...')
        time.sleep(0.2)
        for i in tqdm(range(int(9e7))):
            pass
        os.system('cls')
        os.system('clear')

    def vkprikol_banner(self):
        print(Fore.BLUE)
        print("""
\ \   / / | _|  _ \ _ __(_) | _____ | |
 \ \ / /| |/ / |_) | '__| | |/ / _ \| |
  \ V / |   <|  __/| |  | |   < (_) | |
   \_/  |_|\_\_|   |_|  |_|_|\_\___/|_|
   """)


    def check_files(self, login, password, album_id, group_id):
        green = Fore.GREEN
        red = Fore.RED
        white = Fore.WHITE
        successful = f'{Fore.GREEN}--|| Запуск Успешный ||--'
        if os.path.exists('config.ini') == True:
            print('''
                    ''')
            config = f'{Fore.RED}Config' + f'{white} - ' + f'{Fore.GREEN}[OK]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            time.sleep(2.5)
            if login != '':
                print(f'{red}.login' + f'{white} - ' + f'{green}[OK]')
                time.sleep(1)
            else:
                print(f'{red}.login' + f'{white} - ' + f'{red}[FAIL]')
                exit()
            if password != '':
                print(f'{red}.password' + f'{white} - ' + f'{green}[OK]')
                time.sleep(1)
            else:
                print(f'{red}.password' + f'{white} - ' + f'{red}[FAIL]')
                exit()
            if group_id != '':
                print(f'{red}.groupID' + f'{white} - ' + f'{green}[OK]')
                time.sleep(1)
            else:
                print(f'{red}.groupID' + f'{white} - ' + f'{red}[FAIL]')
                exit()
            if album_id != '':
                print(f'{red}.albumID' + f'{white} - ' + f'{green}[OK]')
                time.sleep(1)
            else:
                print(f'{red}.albumID' + f'{white} - ' + f'{red}[FAIL]')
                exit()
            vk_session = vk_api.VkApi(login, password)
            try:
                vk_session.auth(token_only=True)
                print(f'{red}.session' + f'{white} - ' + f'{green}[OK]')
            except vk_api.AuthError as error_msg:
                print(f'{red}.session' + f'{white} - ' + f'{red}[FAIL]')
                return
        else:
            print('''
                                ''')
            config = f'{Fore.RED}Config' + f'{white} - ' + f'{Fore.RED}[FAIL]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            exit()
        if os.path.exists('requirements.txt') == True:
            print("""""")
            config = f'{Fore.RED}Requirements' + f'{white} - ' + f'{Fore.GREEN}[OK]'
            for char in config:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
        else:
            print("""""")
            config = f'{Fore.RED}Requirements' + f'{white} - ' + f'{Fore.RED}[FAIL]'
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