'''
Practice Project 02: Strong Password

Implemented by: Benjamin Lazaro III
Date: 03/31/2018

Objective(s):
- Write a function that uses regular expression to make sure that the password string is strong.
    - At least 8 characters long
    - Contains both uppercase & lowercase characters
    - At least 1 digit
'''
import re

def passwordCheck(userPasswd):

    passwdLengthChk = re.compile(r'[a-zA-Z0-9]{8,}')                # check if the password string is NOT less than 8 characters
    try:
        matchObj = passwdLengthChk.search(userPasswd).group()
        if matchObj != None:
            print('Minimum Password Length: Passed!')

            passwdDigitChk = re.compile(r'\d{1,}')                  # check if the password string has at least 1 digit
            try:
                matchObj = passwdDigitChk.search(userPasswd).group()
                if matchObj != None:
                    print('Minimum 1 Digit Present: Passed!')

                    passwdUpCaseChk = re.compile(r'[A-Z]+')         # check if the password string has at least 1 uppercase character
                    try:
                        matchObj = passwdUpCaseChk.search(userPasswd).group()
                        if matchObj != None:
                            print('Mixed Case Present: Passed!')
                            print('The string "' + userPasswd + '" is a strong password!')

                    except AttributeError:
                        print('Mixed Case Present: Failed!')

            except AttributeError:
                print('Minimum 1 Digit Present: Failed!')

    except AttributeError:
        print('Minimum Password Length: Failed!')



print('Enter Password to be checked: ')
userInput = input()                                                 # accepts user-defined password string
passwordCheck(userInput)                                            # calls passwordCheck() & passes the user-defined password as argument
