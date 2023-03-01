contacts = []



name = input('Enter name: ')
surname = input('Enter surname: ')
number = input('Enter number: ')

while(True):
    response = input('N - add new, P - print, E - exit: ')
    if response == 'N':
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        number = input('Enter number: ')
        
        contact = {
            'name': name, 
            'surname': surname,
            'number': number
        }

        contacts.append(contact)
        print(contacts)
    elif response == 'P':
        for contact in contacts:
            print(f"{contact[name]} {contact[surname]} {contact[number]}")
    elif response == 'E':
        break