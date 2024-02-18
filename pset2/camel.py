import re

def camel_to_snake(s):
    words = [x.group().lower() for x in re.finditer(r'[A-Z]?[^A-Z]*', s)]
    return '_'.join(words[:-1])

assert camel_to_snake('name') == 'name'
assert camel_to_snake('firstName') == 'first_name'
assert camel_to_snake('preferredFirstName') == 'preferred_first_name'
