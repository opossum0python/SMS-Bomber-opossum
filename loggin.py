from Attack_Services import Attack_Services
from datetime import datetime


class Loggin(Attack_Services):
    """

    Класс логирования запросов юзера

    """

    def loggin(self):
        """

        Функция Записываеи в файл Loggin.txt код страны и номер телефона, вводимый пользователем, а так же
        дату и время, в которое был запущен скрипт
        :return: None

        """
        with open('Loggin.txt', 'a') as f:
            f.write(self.phone + ' ' + self.code_country + ' ' + datetime.now().strftime("%d-%m-%Y|%H:%M") + '\n')


if __name__ == "__main__":
    Loggin('7', '98774455321').loggin()