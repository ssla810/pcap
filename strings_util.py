import string_utils


def halve_strings(string_list):
    to_return = []
    for string in string_list:
        to_return.append(string_utils.halve_string(string))
    return to_return
