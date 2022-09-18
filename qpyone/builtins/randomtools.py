import random

from faker import Faker


faker = Faker(["en_US", "zh_CN"])


def random_unicode():
    val = random.randint(0x4E00, 0x9FBF)
    return chr(val)


def random_GBK2312():
    head = random.randint(0xB0, 0xF7)
    body = random.randint(0xA1, 0xFE)
    val = f"{head:x} {body:x}"
    str = bytes.fromhex(val).decode("gb2312")
    return str


def random_str(length=4):
    result = []
    for i in range(length):
        result.append(random.choice([random_unicode])())
    return "".join(result)
