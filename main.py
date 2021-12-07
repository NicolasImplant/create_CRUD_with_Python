import sys  

clients = ['Nicolás', 'Isabella', 'Diego', 'Ana María', 'Mateo', 'Serafina', 'Chocolate']


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in client\'s list')
    return clients


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client}')


def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in clients list')


def search_client(client_name):
    for client in clients:
        if client != client_name:
            print(client)
            continue
        else:
            return True

            
def _print_welcome():
    print('Welcome to my store')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate a client')
    print('[L]ist of clients')
    print('[R]ead a client')
    print('[U]pdate a client')
    print('[D]elete a client')
    print('[S]earch client')


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name?   ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name


if __name__ == '__main__':
    _print_welcome()
    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name?  ')
        update_client(client_name, updated_client_name)
        list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'S':
        list_clients()
        client_name = _get_client_name()
        found = search_client(client_name)
        if found == True:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} not in client\'s list')
            list_clients()

    else:
        print('Invalid command')