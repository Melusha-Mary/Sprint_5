import random
import string

names = ['Mary', 'Egor', 'Mike', 'Sara', 'July', 'Ksenia', 'Timofey']  # Глобальная переменная


class Generators:
    @staticmethod
    def generate_name():
        chosen_name = random.choice(names)

        return f'{chosen_name}'

    @staticmethod
    def generate_email():
        chosen_name = random.choice(names)
        surnames = ['Kurochkin', 'Ivanov', 'Sidorov', 'Petrov', 'Kapitanov']
        chosen_surname = random.choice(surnames)
        domains = ['@yandex.ru', 'gmail.com', '@rambler.ru', '@mail.ru']
        chosen_domain = random.choice(domains)
        number = random.randint(100, 900)

        return f'{chosen_name}_{chosen_surname}{number}{chosen_domain}'

    @staticmethod
    def generate_correct_password(length=6):
        characters = string.ascii_letters + string.digits
        correct_password = ''.join(random.choice(characters) for _ in range(length))

        return f'{correct_password}'

    @staticmethod
    def generate_wrong_password():
        wrong_password = random.randint(100, 900)

        return f'{wrong_password}'
