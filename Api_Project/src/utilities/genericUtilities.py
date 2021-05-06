import logging as logger
import random
import string


def generate_random_email_password(domain=None, email_prefix=None):
    logger.info("generating random email and password")

    if not domain:
        domain = 'qa.com'

    if not email_prefix:
        email_prefix = 'test'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain

    random_password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=random_password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"randomly generated email and password :{random_info}")

    return random_info


def generate_random_string(length=10, prefix=None, suffix=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    if prefix:
        random_string=prefix+random_string

    if suffix:
        random_string=suffix+random_string

    return random_string

