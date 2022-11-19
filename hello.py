import argparse

def hello_name(name):
    print(f'hello {name}')

def hello_to_family(name_list):
    speaker = name_list[0]
    for i in range(len(name_list)-1):
        print(f'{speaker} say hi to {name_list[i+1]}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ns', '--names',nargs='+', type=str, default='Bob')
    args = parser.parse_args()
    hello_to_family(args.names)