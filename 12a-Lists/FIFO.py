invoer = input('invoer: ')
list = []

while invoer != 'STOP':

    if invoer != '?':
        list.append(invoer)

    elif len(list) > 0:
        print(list.pop(0))

    invoer = input('invoer: ')