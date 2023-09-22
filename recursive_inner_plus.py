def recursive_inner_plus(input_list):
    if not any(isinstance(item, list) for item in input_list):
        return [i + 1 for i in input_list]
    for item in input_list:
        if isinstance(item, list):
            return find_innermost(item)
