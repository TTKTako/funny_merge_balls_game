from SetUp import SetUp

while True:
    username = input("Enter your username: ")
    if len(username) == 0:
        print("Username cannot be empty string.")
    else:
        ans = input("Is this your username '{}' ? [Y/N]: ".format(username)).lower()
        if ans == 'y' or ans == 'yes' or ans == '1':
            break

setting_app = SetUp(username)