from colorama import Fore, Style

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "Ad13n@23t":
    print(Fore.LIGHTCYAN_EX + "Welcome, admin" + Style.RESET_ALL)
else:
    print(Fore.RED + "You are not admin" + Style.RESET_ALL)
