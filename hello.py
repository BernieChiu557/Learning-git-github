import argparse

def hello_name(name):
    print(f'hello {name}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', type=str, default='Bob')
    args = parser.parse_args()
    hello_name(args.name)