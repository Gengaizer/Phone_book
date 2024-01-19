from seminar007 import *


def actionRequest(Start):
    request = input(
        'What do you want to do''\n1-''Search''\n2-''add''\n3-''delete''\n4-''directory display''\n5-''replacing value''\n')
    if request == '1':
        Search = input(
            'plees enter one of the required values: name,phone-number,surname''\n')
        printing = []
        lens = 0
        data = open('Phonebook.txt', 'r+', encoding='utf-8')
        for line in data:
            lens += 1
        data.close()
        namePhoneNumberSurname(data, Search, printing, lens)

    elif request == '2':
        Add_value()
    elif request == '3':
        Search = input(
            'enter one of the values, first name, last name, phone number''\n')
        printing = []
        lens = 0
        data = open('Phonebook.txt', 'r+', encoding='utf-8', errors="ignore")
        for line in data:
            lens += 1
        data.close()
        Delete(data, Search, printing, lens)

    elif request == '4':
        with open('Phonebook.txt', 'r', encoding='utf-8') as data:
            directory_display(data)
    elif request == '5':
        Search = input(
            'plees enter one of the required values: name,phone-number,surname''\n')
        printing = []
        lens = 0
        data = open('Phonebook.txt', 'r+', encoding='utf-8')
        for line in data:
            lens += 1
        data.close()
        replacement(data, Search, printing, lens)
    elif request != '1' or request != '2' or request != '3':
        restart = input(
            'Invalid value entered. would you like to repeat it?''\n''yes:Y''\n''no:N''\n')
        if restart.upper() == 'Y':
            actionRequest(Start)
        elif restart.upper() == 'N':
            exit()
        else:
            Restart()
    elif request != 1 and request != 2 and request != 3 and request != 4 and request != 5:
        question = input('do you want to try again?''\n''yes:Y''\n''no:N''\n')
        if question.upper() == 'Y':
            actionRequest(Start)
        elif question.upper() == 'N':
            exit()


def Hello():
    hello = input(
        'Welcome to Phone Book''\n''version 0.397(beta)''\n''Would you like to start working?''\n''yes:Y''\n''no:N''\n')
    if hello.upper() == 'Y':
        Start = False
        actionRequest(Start)

    elif hello.upper() == 'N':
        print('Goodbye')
        exit()
    else:
        Restart()


if '__main__' == __name__:
    Hello()
