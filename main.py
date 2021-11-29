import hashlib
user = int(input("Вы хотите зарегистрироваться, введите 1. Если авторизоваться , введите 2"))

class Autorizeichen:

    def main(self):
        if user == 1:
            self.__check_login()
            self.__write_login_and_password()
            print("Вы успешно зарегистрированны")
        elif user == 2:
            self.__authorization()
        else:
            raise ValueError("Вы лузер)))")


    def __check_registration(self):
        log = input("Введите свой логин: ")
        log_len = len(log)
        if log_len < 3 or log_len > 20:
            log = input(f"Вы ввели неверное количество символов {log_len}:")
        log = f'{log}'
        pasword = input("Введите свой пароль: ")
        pas_len = len(pasword)
        if pas_len < 4 or pas_len > 32:
            pasword = input(f"Вы ввели неверное количество символов {pas_len}:")
        pasword = pasword.encode('utf-8')
        pasword = hashlib.sha512(pasword).digest()
        return log, pasword

    def __check_login(self):
        while True:
            login = input("Введите логин для проверки: ")
            with open("книга регистраций", "r", encoding="utf-8") as f:
                if login in f.read():
                    print("Данный логин занят")
                else:
                    break

    def __write_login_and_password(self):
        with open("книга регистраций", "a", encoding="utf-8") as f:
            f.write(f'\n{str(self.__check_registration())}')


    def __authorization(self):
        name = input("Введите свои логин1: ")
        name2 = input("Введите пароль1: ")
        name3 = name2.encode('utf-8')
        name3 = hashlib.sha512(name3).digest()
        with open("книга регистраций", "r", encoding="utf-8") as f:
            if name and str(name3) in f.read():
                print("Вы успешно вошли в систему.")
            else:
                print("Неверный логин или пароль.")

luser = Autorizeichen()
luser.main()

import hashlib
