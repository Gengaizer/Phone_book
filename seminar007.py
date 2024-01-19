
def Delete(data, Search, printing, lens):
    SearchForFile(data, Search, printing, lens)
    with open('Phonebook.txt', 'r+', encoding='utf-8') as data:
        if len(printing) > 1:
            print('were found''\n', *printing,
                  '\n''Multiple values were found, please enter another non-repeating value')
            Search = input()
            printing = []
            SearchForFile(data, Search, printing, lens)
            print('was found', *printing)
            check = input(
                'Do you want to delete your data?''\n''yes:Y''\n''no:N''\n')
            if check.upper() == 'Y':
                print('OK')
                Delete_Value(printing)
            elif check.upper() == 'N':
                print('no')
            else:
                print('you are imbecile')

        else:
            print('was found', *printing)
            check = input(
                'What do you want to remove?''\n''yes:Y''\n''no:N''\n')
            if check.upper() == 'Y':
                print('OK')
                Delete_Value(printing)


def Delete_Value(printing):
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
        print(printing)
        printing = printing[0].split(' ')

        Name = printing[0]

        Surname = printing[2]

        Phone_number = printing[4]

        old_value = (f"{Name} {'|'} {Surname} {'|'} {Phone_number}")

        data = file.readlines()

        test = [old_value]

        with open('Phonebook.txt', 'w', encoding='utf-8') as file:
            for line in data:

                if line.strip("") != old_value:
                    file.write(line)

        Restart()


def replacement(data, Search, printing, lens):
    SearchForFile(data, Search, printing, lens)
    with open('Phonebook.txt', 'r+', encoding='utf-8') as data:
        if len(printing) > 1:
            print('were found''\n', *printing,
                  '\n''Multiple values were found, please enter another non-repeating value')
            Search = input()
            printing = []
            SearchForFile(data, Search, printing, lens)
            print('was found', *printing)
            check = input(
                'Would you like to replace a value?''\n''yes:Y''\n''no:N''\n')
            if check.upper() == 'Y':
                replace = input(
                    'What do you want to replace?''\n1-''name''\n2-''phone number''\n3-''surname''\n')
                if replace.upper() == '1':
                    replace = 'name'
                    replaceValue(printing, replace)
                elif replace.upper() == '2':
                    replace = 'phone number'
                    replaceValue(printing, replace)
                elif replace.upper() == '3':
                    replace = 'surname'
                    replaceValue(printing, replace)

            elif check.upper() == 'N':
                Return = input(
                    'Do you want to continue working?''\n''yes:Y''\n''no:N''\n')
                if Return.upper() == 'Y':
                    Restart()
                elif Return.upper() == 'N':
                    print('goodbye')
                    exit()
                else:

                    Restart()
            else:
                Restart()

        elif len(printing) == 1:
            print('was found', *printing)
            check = input(
                'Would you like to replace a value?''\n''yes:Y''\n''no:N''\n')
            if check.upper() == 'Y':
                replace = input(
                    'What do you want to replace?''\n1-''name''\n2-''phone number''\n3-''surname''\n')
                if replace.upper() == '1':
                    replace = 'name'
                    replaceValue(printing, replace)
                elif replace.upper() == '2':
                    replace = 'phone number'
                    replaceValue(printing, replace)
                elif replace.upper() == '3':
                    replace = 'surname'
                    replaceValue(printing, replace)
        elif len(printing) < 1:
            print('No values found')
            Restart()
        else:
            Restart()


def replaceValue(printing, replace):
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
        if replace == 'name':

            printing = printing[0].split(' ')

            Name = printing[0]

            Surname = printing[2]

            Phone_number = printing[4]

            New_Name = input(
                'Under what name would you like to continue the current one?''\n')
            New_value = (f"{New_Name} {'|'} {Surname} {'|'} {Phone_number}")
            old_value = (f"{Name} {'|'} {Surname} {'|'} {Phone_number}")
            New_value = str(New_value)

            data = file.read()
            data = data.replace(old_value[0:45], New_value[0:45])

            print(data)

            with open('Phonebook.txt', 'w', encoding='utf-8') as file:
                file.write(data)
            Restart()
        elif replace == 'surname':

            printing = printing[0].split(' ')

            Name = printing[0]

            Surname = printing[2]

            Phone_number = printing[4]

            New_surname = input(
                'Under what name would you like to continue the current one?''\n')
            New_value = (f"{Name} {'|'} {New_surname} {'|'} {Phone_number}")
            old_value = (f"{Name} {'|'} {Surname} {'|'} {Phone_number}")
            New_value = str(New_value)

            data = file.read()
            data = data.replace(old_value[0:45], New_value[0:45])

            print(data)

            with open('Phonebook.txt', 'w', encoding='utf-8') as file:
                file.write(data)
            Restart()
        elif replace == 'phone number':

            printing = printing[0].split(' ')

            Name = printing[0]

            Surname = printing[2]

            Phone_number = printing[4]

            New_Phone_number = input(
                'Under what name would you like to continue the current one?''\n')
            New_value = (f"{Name} {'|'} {Surname} {'|'} {New_Phone_number}")
            old_value = (f"{Name} {'|'} {Surname} {'|'} {Phone_number}")
            New_value = str(New_value)

            data = file.read()
            data = data.replace(old_value[0:45], New_value[0:45])

            print(data)

            with open('Phonebook.txt', 'w', encoding='utf-8') as file:
                file.write(data)
            Restart()


def SearchForFile(data, Search, printing, lens):
    with open('Phonebook.txt', 'r+', encoding='utf-8') as data:
        countSpisok = 0
        countLens = 0
        for line in data:
            countLens += 1
            searchvalue = line.split(' ')

            for i in searchvalue:
                if i.lower() == Search.lower():
                    printing.append(line)
                    countSpisok += 1
                elif i.rstrip() == Search.rstrip():
                    printing.append(line)
                    countSpisok += 1
        if (countLens == lens and len(printing) == 0):
            print('the required value was not found')
    return (data, Search, printing, lens)


def Add_value():
    Quest = input('you want to add a new value''\n''yes:Y''\n''no:N''\n')
    if Quest.upper() == 'Y':
        with open('Phonebook.txt', 'a', encoding='utf-8') as data:
            print(
                'Enter data in the format''\n1-''Surname''\n2-''Name''\n3-''Phone Number *(***)*******''\n')
            surname = input('Surname:')
            Name = input('Name:')
            phone = input('Phone Number:')
            data.write(f"{Name} {'|'} {surname} {'|'} {phone}\n")
            print(Name, surname, phone)
            Restart()

    elif Quest.upper() == 'N':
        Return = input(
            'Do you want to continue working?''\n''yes:Y''\n''no:N''\n')
        if Return.upper() == 'Y':
            import Pokaz
            Pokaz.actionRequest(Start=False)
        elif Return.upper() == 'N':
            print('goodbye')
            exit()
        else:
            print('Invalid value entered''\n''goodbye')
            exit()
    else:
        Restart()


def directory_display(data):
    with open('Phonebook.txt', 'r+', encoding='utf-8') as data:
        for line in data:
            print(line)
        Restart()


def namePhoneNumberSurname(data, Search, printing, lens):
    print(data, Search, printing, lens)
    with open('Phonebook.txt', 'r+', encoding='utf-8') as data:
        countSpisok = 0
        countLens = 0
        for line in data:
            countLens += 1
            searchvalue = line.split(' ')
            for i in searchvalue:
                if i.lower() == Search.lower():
                    printing.append(line)
                    countSpisok += 1
                elif i.rstrip() == Search.rstrip():
                    printing.append(line)
                    countSpisok += 1
        if (countLens == lens and len(printing) == 0):
            print('the required value was not found')
    print(*printing)
    Restart()


def Restart():
    Return = input('Do you want to continue working?''\n''yes:Y''\n''no:N''\n')
    if Return.upper() == 'Y':
        import Pokaz
        Pokaz.actionRequest(Start=False)
    elif Return.upper() == 'N':
        print('goodbye')
        exit()
    else:
        print('Invalid value entered')
        Restart()
