import getpass

import vk_requests

APP_ID = 7081621


def main():
    login = get_user_login()
    password = get_user_password()
    vk_api = connect_vk_api(login=login,
                            password=password)
    friends_online = get_online_friends(vk_api)
    output_friends_to_console(friends_online)


def get_user_login():
    user_login = input('Please enter your VK login:')
    assert user_login != '', 'Login should not be empty string.'
    return user_login


def get_user_password():
    user_password = getpass.getpass("Please enter your password for check "
                                    "and press Enter:")
    assert user_password != '', 'Password should not be empty string.'
    return user_password


def connect_vk_api(login, password):
    api = vk_requests.create_api(
        app_id=APP_ID,
        login=login,
        password=password,
        api_version='5.101',
        scope='friends',
    )
    return api


def get_online_friends(api):
    online_friends_ids = api.friends.getOnline()
    online_friends_info = api.users.get(user_ids=online_friends_ids)

    return online_friends_info


def output_friends_to_console(friends_online):
    friends_online_number = len(friends_online)
    print('Number of friends online : {}'.format(friends_online_number))

    if friends_online_number > 0:
        for index, friend in enumerate(friends_online, start=1):
            print('{}: {} {}'.format(index,
                                     friend['first_name'],
                                     friend['last_name']))


if __name__ == '__main__':
    main()
