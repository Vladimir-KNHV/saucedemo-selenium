import random
import string


RUS_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUS_UPPER = RUS_LOWER.upper()

ENG_LOWER = string.ascii_lowercase
ENG_UPPER = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION = string.punctuation


def generate_username() -> str:
    length = random.randint(3, 31)

    alphabet = (
        RUS_LOWER +
        RUS_UPPER +
        ENG_LOWER +
        ENG_UPPER +
        DIGITS
    )

    return "".join(random.choice(alphabet) for _ in range(length))


def generate_password() -> str:
    length = random.randint(10, 20)

    alphabet = (
            RUS_LOWER +
            RUS_UPPER +
            ENG_LOWER +
            ENG_UPPER +
            DIGITS +
            PUNCTUATION
    )

    return "".join(random.choice(alphabet) for _ in range(length))

def generate_postal_code() -> str:
    length = random.randint(5, 10)
    return "".join(random.choice(string.digits) for _ in range(length))