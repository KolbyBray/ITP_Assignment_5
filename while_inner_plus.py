def while_inner_plus(input_list):
    lists_to_check = [input_list]
    while lists_to_check:
        current_list = lists_to_check.pop()
        new_lists = []
        for item in current_list:
            if isinstance(item, list):
                new_lists.append(item)
        if not new_lists:
            return [x + 1 for x in current_list]
        else:
            lists_to_check.extend(new_lists)
