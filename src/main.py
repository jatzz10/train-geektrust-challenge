from src.train import Train, get_merged_bogies_on_departure
from src.db import train_A_route, train_B_route


def compute_train_bogies_order(train_A, train_B):
    train_A_bogies = train_A.get_bogies_on_arrival()
    train_B_bogies = train_B.get_bogies_on_arrival()
    merged_bogies_at_departure = get_merged_bogies_on_departure(train_A_bogies, train_B_bogies)

    return {
        'train_A_bogies': train_A_bogies, 
        'train_B_bogies': train_B_bogies, 
        'merged_bogies_at_departure': merged_bogies_at_departure
    }


def print_output(payload):
    print('ARRIVAL', end=' ')
    for itm in payload['train_A_bogies']:
        print(itm, end=' ')
    print()
    
    print('ARRIVAL', end=' ')
    for itm in payload['train_B_bogies']:
        print(itm, end=' ')
    print()
    
    print('DEPARTURE', end=' ')
    for itm in payload['merged_bogies_at_departure']:
        print(itm, end=' ')