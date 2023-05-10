from src.db import train_A_route, train_B_route
from src.bogie import Bogie


class Train:
    def __init__(self, name) -> None:
        self.name = name
        self.bogies = []
    
    
    def add_bogie(self, bogie):
        self.bogies.append(bogie)


    def get_bogies_on_arrival(self):
        bogies_on_arrival = []

        for bogie in self.bogies:
            if 'TRAIN' in bogie.code \
                or 'ENGINE' in bogie.code \
                or Train.check_valid_bogie(bogie):
                bogies_on_arrival.append(bogie.code)

        return bogies_on_arrival

    
    @staticmethod
    def check_valid_bogie(bogie):
        if bogie.train_name == 'TRAIN_A':
            return (bogie.code in train_A_route and train_A_route[bogie.code]['seq_num'] >= 5) \
                or (bogie.code in train_B_route and train_B_route[bogie.code]['seq_num'] >= 7)
        else:
            return (bogie.code in train_B_route and train_B_route[bogie.code]['seq_num'] >= 7) \
                or (bogie.code in train_A_route and train_A_route[bogie.code]['seq_num'] >= 5)

    
    
    @staticmethod
    def extract_bogie_names(train):
        return [bogie.code for bogie in train]


    def __repr__(self) -> str:
        return f'Train({self.name})'


def get_merged_bogies_on_departure(train_A_bogies, train_B_bogies):
    train_bogies_after_departure = ['TRAIN_AB', 'ENGINE', 'ENGINE']
    station_distance = []
    
    for bogie in train_A_bogies:
        if 'ENGINE' in bogie or 'TRAIN' in bogie:
            continue
        
        distance = train_A_route[bogie]['distance_from_hyb'] if bogie in train_A_route else train_B_route[bogie]['distance_from_hyb']
        station_distance.append([int(distance), bogie])
        
    for bogie in train_B_bogies:
        if 'ENGINE' in bogie or 'TRAIN' in bogie:
            continue
        
        distance = train_B_route[bogie]['distance_from_hyb'] if bogie in train_B_route else train_A_route[bogie]['distance_from_hyb']
        station_distance.append([int(distance), bogie])
    
    station_distance.sort(reverse=True)
    
    for station in station_distance:
        if station[1] != 'HYB':
            train_bogies_after_departure.append(station[1])
        
    return train_bogies_after_departure