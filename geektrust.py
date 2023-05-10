from sys import argv
from src.train import Train
from src.bogie import Bogie
from src.main import compute_train_bogies_order, print_output

def main():
    """
    This is the starting point of the project.
    """
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    
    # Remove the endline character at the end
    lines[0] = lines[0][:-1]

    # Create object for TRAIN_A
    train_A = Train('TRAIN_A')
    for item in lines[0].split(' '):
        bogie = Bogie(train_A.name, item)
        train_A.add_bogie(bogie)
    
    # Create object for TRAIN_B
    train_B = Train('TRAIN_B')
    for item in lines[1].split(' '):
        bogie = Bogie(train_B.name, item)
        train_B.add_bogie(bogie)
    
    output_payload = compute_train_bogies_order(train_A, train_B)
    print_output(output_payload)


if __name__ == "__main__":
    main()