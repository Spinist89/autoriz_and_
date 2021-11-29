user = int(input("Вы хотите зарегистрироваться, введите 1. Если авторизоваться , введите 2"))
class Autorizeichn():

    def registration(self):
        if user == 1:
            with open ("книга регистраций", "a", encoding="utf-8") as f:
                a = input("Введите свой логин:")
                s = len(a)
                if s < 3 or s > 20:
                    a = input("Введите свой логин:")
                a = f'\n{a}'
                b = input("Введите свой пароль:")
                d = len(b)
                if d < 3 or d > 20:
                    b = input("Введите свой пароль:")
                x = f"\n{a} {b}"
                f.write(x)
                print("Вы успешно зарегистрированны")
                return a, b
    def autoriz(self):
        if user == 2:
            with open ("книга регистраций", "r", encoding="utf-8") as f:
                name = input("Введите свои логин и пароль")
                if name in f:
                    print("Вы успешно вошли в систему.")
                else:
                    print("Неверный логин или пароль.")
                return name
        else:
            print("Вы ввели не подходящее значение")
