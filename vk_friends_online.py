from getpass import getpass
import vk
import test_config


def get_user_login():
    return input("Введите логин: ")


def get_user_password():
    return getpass('Введите пароль: ')


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
    print("Список онлайн пользователей из френд-листа:")
    for person in friends_online:
        print("{first_name} {last_name}".format(**person))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
