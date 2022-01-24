import re

def email_parse(email_adress):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email_adress)
    if not result:
        raise ValueError(f'Wrong email: {email_adress}')
    return result.groupdict()


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))