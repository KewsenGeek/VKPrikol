# Импорт нужных модулей
import os
import sys
import time
from configparser import ConfigParser

import vk_api
from colorama import Fore
from colorama import init
from banners import Banners
init()


# Основной класс
class VK:
    # Инициализирующая функция
    def __init__(self):
        # Чтение данных из config.ini
        configuration_file = 'config.ini'
        config = ConfigParser()
        config.read(configuration_file)
        self.group_id = config['Aim']['group_id']
        self.album_id = config['Aim']['album_id']
        self.upload_limit = int(config['Settings']['UploadLimit'])
        self.folder_with_photos = config['Settings']['FolderWithPhotos']
        self.autoupdate = config['Settings']['AutoCheckForUpdates']
        self.login = config['VK']['login']
        self.password = config['VK']['password']
        self.version = config['Info']['Version']
        self.python_version = config['Info']['PythonVersion']
        self.place_in_photos = 0
        self.os = sys.platform

    # Основная функция
    def main(self):
        os.system('cls')
        os.system('clear')
        Banners.vkprikol_banner(self)
        Banners.start_banner(self, version=self.version, os=self.os, login=self.login, password=self.password, album_id=self.album_id, group_id=self.group_id)
        system_python_version = sys.version[:3]
        start_or_settings = input(':')
        os.system('cls')
        os.system('clear')
        if start_or_settings == 'start':
            if self.python_version > system_python_version:
                print(Fore.RED)
                print(f'Этот скрипт написан для версии python {self.python_version}''\n'
                      f'Вы используете версию python {system_python_version}'
                      'Рекомендуется обновить версию python, в противном случае скрипт будет работать некоректно,''\n'
                      'Или не будет работать вовсе!')
            if self.group_id != None and self.album_id != None and self.upload_limit != None and self.folder_with_photos != None and self.autoupdate != None and self.login != None and self.password != None and self.version != None and self.python_version != None:
                print('Программа готова к запуску. Начать атаку? Y/N')
                start_program = input(':')
                os.system('cls')
                os.system('clear')
                if start_program == 'Y' or 'y':
                    os.system('cls')
                    os.system('clear')
                    vk_session = vk_api.VkApi(login=self.login, password=self.password)
                    try:
                        vk_session.auth(token_only=True)
                    except vk_api.AuthError as error_msg:
                        print(error_msg)
                        return
                    photos = os.listdir(self.folder_with_photos)
                    time.sleep(1)
                    Banners.banner_atack(self)
                    self.upload(vk_session, self.group_id, self.album_id, photos)
                elif start_program == 'N' or 'n':
                    print('Выход из программы, подождите...')
                    time.sleep(3)
                    exit()
                else:
                    print('Попробуйте еще раз')
        else:
            print('Попробуйте еще раз.')

    # Функция, которая загружает фото в альбом
    def upload(self, vk_session, group_id, album_id, photos):
        print("""
┏━━━┓┏┓     ┏┓
┃┏━┓┣┛┗┓   ┏┛┗┓
┃┗━━╋┓┏╋━━┳┻┓┏┛
┗━━┓┃┃┃┃┏┓┃┏┫┃
┃┗━┛┃┃┗┫┏┓┃┃┃┗┓
┗━━━┛┗━┻┛┗┻┛┗━┛.....""")
        upload = vk_api.VkUpload(vk_session)
        cycle = 1
        files = self.folder_with_photos
        if self.upload_limit == 0:
            place_in_photos = self.place_in_photos
            while True:
                try:
                    picture_to_upload = self.folder_with_photos + '/' + photos[place_in_photos]
                    photo = upload.photo(
                        photos=picture_to_upload,
                        album_id=album_id,
                        group_id=group_id
                    )
                    place_in_photos += 1
                    print(f'{Fore.GREEN}Фото №{place_in_photos} загружено успешно!')
                    if place_in_photos > len(os.listdir(files)) - 1:
                        place_in_photos = 0
                        time.sleep(0.2)
                        print(f'{Fore.YELLOW}Круг №{cycle} завершен.')
                        cycle += 1
                except:
                    print(f'{Fore.RED}Фото загрузить не удалось! Перезапуск программы...')
                    self.main()
        else:
            place_in_photos = self.place_in_photos
            upload_limit = self.upload_limit
            cycle = 1
            while True:
                try:
                    picture_to_upload = self.folder_with_photos + '/' + photos[place_in_photos]
                    photo = upload.photo(
                        photos=picture_to_upload,
                        album_id=album_id,
                        group_id=group_id
                    )
                    place_in_photos += 1
                    print(f'{Fore.GREEN}Фото №{place_in_photos} загружено успешно!')
                    if place_in_photos > len(os.listdir(files)) - 1:
                        place_in_photos = 0
                        time.sleep(0.2)
                        print(f'{Fore.YELLOW}Круг №{cycle} завершен.')
                        cycle += 1
                        if cycle == self.upload_limit:
                            print(f'{Fore.BLUE}Загрузка завершена! Выход из программы...')
                            time.sleep(0.5)
                            break
                except:
                    print(f'{Fore.RED}Фото загрузить не удалось! Перезапуск программы...')
                    self.main()

vk = VK()
print(vk.main())