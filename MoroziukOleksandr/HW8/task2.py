import re

def check_password(password):
    """
    Перевіряє введений пароль на ряд вимог.

    Параметри:
        password: Введений пароль.

    Повертає:
        True, якщо пароль відповідає вимогам, False в іншому випадку.
    """

    # Перевірка довжини пароля.
    if len(password) < 6 or len(password) > 16:
        return False

    # Перевірка наявності великих і маленьких букв.
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False

    # Перевірка наявності цифр.
    if not re.search(r"\d", password):
        return False

    # Перевірка наявності символів.
    if not re.search(r"[$#@]", password):
        return False

    return True


def main():
  password = input("Введіть пароль: ")

  if check_password(password):
    print("Пароль відповідає вимогам.")
  else:
    print("Пароль не відповідає вимогам.")


if __name__ == "__main__":
  main()