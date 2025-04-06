import argparse

from gendiff.scripts.diff_builder import build_diff
from gendiff.scripts.json import format_json
from gendiff.scripts.parser import parse_file
from gendiff.scripts.plain import format_plain
from gendiff.scripts.stylish import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    elif format_name == 'stylish':
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
        choices=['stylish', 'plain', 'json'],
        default='stylish'
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)
