# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12

import re


def check_passwords(str):
    password_list = str.split(",")
    final_list = []

    for password in password_list:
        if len(password) < 6 or len(password) > 12:
            continue
        if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]", password) and re.search("[$#@]", password):
            final_list.append(password)

    return final_list


print(check_passwords("aA3$$aA3, yes, ZZk99$$"))
