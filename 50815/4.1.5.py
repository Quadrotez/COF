USERS = {
    "admin": "admin",
    "Doberman": "derparol",
    "BabValya": "12345",
}

def check_pass(username, password):
    return (True if USERS[username] == password else (lambda: (print("НЕВЕРНЫЙ ПАРОЛЬ!"), False))()[1]) if username in USERS else (lambda: (print("ПОЛЬЗОВАТЕЛЬ НЕ ОБНАРУЖЕН!"), False))()[1]

def authorize():
    while True:
        if len(user_input := input().split(' ')) != 2:
            print("ОШИБКА АВТОРИЗАЦИИ!")
            continue

        if check_pass(user_input[0], user_input[1]):
            print("УСПЕШНО")
            return True