# parse the input string & create a nested object
def parse_string(puzzle):
    stack = []
    object = {}
    key = ''
    stack.append(object)

    for char in puzzle:
        if char == '(':
            stack.append({})
            # current key gets new object
            object[key] = stack[-1]
            key = ''
            # update current object
            object = stack[-1]
        elif char == ')':
            if key:
                object[key] = None
                key = ''
            # pop back to previous object in stack
            stack.pop()
            object = stack[-1]
        elif char == ',':
            if key:
                object[key] = None
                key = ''
        else:
            # add characters to form key
            key += char

    if key:
        object[key] = None

    # return the root of nested objects
    return stack[0]  

def print_nested_dict_unsorted(obj, tab_level=0):
    # avoids printing '-' at root level
    is_root = tab_level == 0
    for prop, value in obj.items():
        if isinstance(value, dict):
            if not is_root:
                print(" " * tab_level + "- " + prop)
            print_nested_dict_unsorted(value, tab_level + 2)
        else:
            print(" " * tab_level + "- " + prop)

def print_nested_dict_sorted(obj, tab_level=0):
    is_root = tab_level == 0
    for prop, value in sorted(obj.items()):
        if isinstance(value, dict):
            if not is_root:
                print(" " * tab_level + "- " + prop)
            print_nested_dict_sorted(value, tab_level + 2)
        else:
            print(" " * tab_level + "- " + prop)


puzzle = "(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)"
parsed_data = parse_string(puzzle)

print_nested_dict_sorted(parsed_data)
print('\n')
print_nested_dict_unsorted(parsed_data)