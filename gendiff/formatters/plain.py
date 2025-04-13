def format_plain(diff):
    lines = _format_plain(diff)
    return '\n'.join(lines)


def _format_plain(diff, path=''):
    lines = []
    for node in diff:
        current_key = node['key']
        current_path = f"{path}.{current_key}" if path else current_key
        type_ = node['type']
        if type_ == 'nested':
            children = node['children']
            lines.extend(_format_plain(children, current_path))
        elif type_ == 'added':
            value = _stringify_value(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif type_ == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif type_ == 'changed':
            old_value = _stringify_value(node['old_value'])
            new_value = _stringify_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
    return lines


def _stringify_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)
