def format_stylish(diff, level=0):
    indent = ' ' * (level * 4)
    lines = []

    sorted_nodes = sorted(diff, key=lambda x: x['key'])

    for node in sorted_nodes:
        key = node['key']
        type_ = node['type']

        if type_ == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], level + 1))
            lines.append(f"{indent}    }}")
        elif type_ == 'added':
            value = _format_value(node['value'], level + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif type_ == 'removed':
            value = _format_value(node['value'], level + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif type_ == 'unchanged':
            value = _format_value(node['value'], level + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif type_ == 'changed':
            old = _format_value(node['old_value'], level + 1)
            new = _format_value(node['new_value'], level + 1)
            lines.append(f"{indent}  - {key}: {old}")
            lines.append(f"{indent}  + {key}: {new}")

    if level == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    return '\n'.join(lines)


def _format_value(value, level):
    if isinstance(value, dict):
        indent = ' ' * (level * 4)
        lines = ['{']
        for k in sorted(value.keys()): 
            lines.append(
                f"{indent}    {k}: {_format_value(value[k], level + 1)}"
            )
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if value == "": 
        return ''
    return str(value)
