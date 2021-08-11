import re


def check_tel_number(tel_number="380502852124"):
    match = re.search(r'(\d{2})(\d{3})(\d{3})(\d{2})(\d{2})', tel_number)
    if match:
        print(re.sub(r'(\d{2})(\d{3})(\d{3})(\d{2})(\d{2})', r'(+\1) \2-\3-\4', tel_number))
    else:
        print('Failed to recognize number')


check_tel_number()


