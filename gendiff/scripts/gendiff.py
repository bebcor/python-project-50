import argparse

from gendiff.scripts.diff_builder import build_diff
from gendiff.scripts.parser import parse_file
from gendiff.scripts.stylish import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    return format_stylish(diff)


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
        default='stylish'
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
