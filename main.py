__version__ = 1.3
__author__ = 'Kewsen'

import os
import sys
import time
import vk_api
from configparser import ConfigParser

from colorama import Fore

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE


def main(login, password, groupID, albumID, folder):
    log(text=f" {blue}-|| Проверка запуска ||- \n")
    content = (
        "login",
        "password",
        "groupID",
        "albumID",
    )
    for element in content:
        time.sleep(0.5)
        if read_config()['VK'][str(element)] != '':
            log(f"{red}{element} - ")
            time.sleep(0.5)
            log(f"{green}[OK]\n")
        else:
            log(f"{red}{element}")
            time.sleep(0.5)
            log(f" - [FAIL]\n")
    log(f'{green}--|| Запуск Успешный ||--')
    clear()
    time.sleep(0.5)
    log(
        text=f"""Добро пожаловать в программу VKPrikol v{__version__}!\nИспользуемая версия python: {sys.version[:3]}.\nИспользуемая операционная система: {sys.platform}.\n""",
        delay=0.05
    )
    time.sleep(1.0)
    clear()
    log(
        f'Все готово к запуску! Если данные верны, введите y для начала атаки.\ngroupID = {groupID}\nalbumID = {albumID}')
    if input('\n: ').lower() == 'y':
        print("""
        ┏━━━┓┏┓     ┏┓
        ┃┏━┓┣┛┗┓   ┏┛┗┓
        ┃┗━━╋┓┏╋━━┳┻┓┏┛
        ┗━━┓┃┃┃┃┏┓┃┏┫┃
        ┃┗━┛┃┃┗┫┏┓┃┃┃┗┓
        ┗━━━┛┗━┻┛┗┻┛┗━┛....."""
              )
        place_in_photos = 0
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        while True:
            for i in os.listdir(folder):
                try:
                    upload_photo(photo=str(folder) + '/' + str(i), vk_session=vk_session, groupID=groupID,
                                 albumID=albumID)
                    print(f'{Fore.GREEN}Фото №{place_in_photos} загружено успешно!')
                    place_in_photos += 1
                except:
                    print(f'{Fore.RED}\nФото №{place_in_photos} загрузить не удалось!')
                    time.sleep(0.5)
                    print('Выход из программы...')
                    exit()

    else:
        log('Выход из программы...')
        exit()


def upload_photo(photo, vk_session, groupID, albumID):
    upload = vk_api.VkUpload(vk_session)
    upload.photo(photos=photo, album_id=albumID, group_id=groupID)


def log(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def clear():
    if sys.platform != 'linux':
        os.system('cls')
    else:
        os.system('clear')


def read_config():
    cfg = ConfigParser()
    cfg.read('config.ini')
    return cfg


if __name__ == '__main__':
    clear()
    try:
        main(
            login=read_config()['VK']['login'],
            password=read_config()['VK']['password'],
            groupID=read_config()['VK']['groupID'],
            albumID=read_config()['VK']['albumID'],
            folder=input(f'{green}Введите название папки, откуда будут браться фотографии: ')
        )
    except KeyboardInterrupt:
        clear()
        log(f'{red}Аварийное завершение программы, подождите...', delay=0.05)
        time.sleep(0.5)
        exit()
