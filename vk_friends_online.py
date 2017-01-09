from getpass import getpass
import sys
import vk
import test_config


def get_user_login():
    return input("Введите логин: ")


def get_user_password():
    user_password = getpass('Введите пароль: ')
    if not user_password:
        sys.exit('Пароль не может быть пустым')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=test_config.app_id,
        user_login=login,
        user_password=password,
        scope=test_config.access_scope,
    )
    api = vk.API(session)
    friend_ids = api.friends.getOnline()
    return api.users.get(user_ids=friend_ids)


def output_friends_to_console(friends_online):
    for person in friends_online:
        print("Список онлайн пользователей из френд-листа: \n%s %s" % (person['last_name'], person['first_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
