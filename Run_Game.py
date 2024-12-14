"""Run this code to play the game."""

from set_up import SetUp

while True:
    username = input("Enter your username: ")
    if len(username) == 0:
        print("Username cannot be empty string.")
    else:
        ans = input(f"Is this your username '{username}' ? [Y/N]: ").lower().strip()
        fold = ['y', 'ye', '1', 'yes', 'yep', 'right']
        if ans in fold:
            print("Starting game....")
            break

setting_app = SetUp(username)
setting_app.run()
