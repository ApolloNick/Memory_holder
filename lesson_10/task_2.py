def hide_email(email) -> str:
    splitted_email = email.split("@")
    first_part, second_part = list(splitted_email[0]), list(splitted_email[1])
    first_part[-1], first_part[-2], first_part[-3] = "*", "*", "*"
    second_part[0], second_part[1] = "*", "*"
    prepared_list = first_part + list("@") + second_part
    return "".join(prepared_list)


print(hide_email("hello@gmail.com"))
