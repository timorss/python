from ecommerce.customer import contact
# from ..customer import contact  # other way


def calc_tax(num):
    return num * 2


def calc_shipping(num):
    return num * 2


print(contact.__name__)
print(contact.__package__)