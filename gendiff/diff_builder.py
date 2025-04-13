def build_diff(data1, data2):
    diff = []
    keys = sorted(data1.keys() | data2.keys())

    for key in keys:
        node = {'key': key}
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data2:
            node.update({'type': 'removed', 'value': val1})
        elif key not in data1:
            node.update({'type': 'added', 'value': val2})
        elif val1 == val2:
            node.update({'type': 'unchanged', 'value': val1})
        elif isinstance(val1, dict) and isinstance(val2, dict):
            node.update({'type': 'nested', 'children': build_diff(val1, val2)})
        else:
            node.update({
            'type': 'changed',
            'old_value': val1,
            'new_value': val2
            })
        diff.append(node)

    return diff
