

def is_valid(user, password):
    """
    используется для проверки корректности имени пользователя и пароля
    :input(str, str)
    :output(bool)
    """
    if user=='' or password=='':
        return False
    if not user[0].isalpha():
        return False
    if ' ' in user:
        return False
    return True