


def spl_chars(str):
    special_chars_tuple = ("$", "_", "#", "@","!")

    found_spl_chars = []

    for item in special_chars_tuple:
        if item in str:
            found_spl_chars.append(item)

    return found_spl_chars





print(spl_chars("Dont take like this $# hello!  "))