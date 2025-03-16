import argparse
import json


def read_and_parse(file_path):
    with open(file_path, 'r') as result_file:
        return json.load(result_file)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        metavar='FORMAT',
        choices=['plain', 'json'],
    )
    parser.parse_args()


if __name__ == '__main__':
    main()
