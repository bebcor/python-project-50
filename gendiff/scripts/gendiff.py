import argparse

from gendiff.scripts.parser import parse_file


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return str(value)  


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff_lines = []
    
    for key in keys:
        in_data1 = key in data1
        in_data2 = key in data2
        
        if in_data1 and not in_data2:
            formatted_value = format_value(data1[key])
            diff_line = f'    - {key}: {formatted_value}'
        elif in_data2 and not in_data1:
            formatted_value = format_value(data2[key])
            diff_line = f'    + {key}: {formatted_value}'
        else:
            value1 = data1[key]
            value2 = data2[key]
            if value1 == value2:
                formatted_value = format_value(value1)
                diff_line = f'      {key}: {formatted_value}'
            else:
                formatted1 = format_value(value1)
                formatted2 = format_value(value2)
                diff_lines.append(f'    - {key}: {formatted1}')
                diff_line = f'    + {key}: {formatted2}'
        
        diff_lines.append(diff_line)
    
    return '{\n' + '\n'.join(diff_lines) + '\n}'  


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
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
