
from fake_values import fake_names, email_providers, bc_cities, fake_street_names, bank_names, debit_credit, visa_mastercard
from random import randint,choice
import string
from handlers import register_user

def generate_fake_zip():
    zip = choice(string.ascii_letters) + str(randint(0,9)) + choice(string.ascii_letters) + str(randint(0,9)) + choice(string.ascii_letters) + str(randint(0,9))
    return zip.upper()

def get_random_item(item_list):
    return item_list[randint(0, len(item_list)-1)]

def populate_register_user():
    """
    insert 10 random user data
    """
    for i in range(10):
        [first_name, last_name] = get_random_item(fake_names)
        fake_user_details = {
            "first_name": first_name,
            "last_name": last_name,
            "email": f"{first_name}{last_name}{randint(0,9)}@{get_random_item(email_providers)}.com",
            "phone": randint(1000000000,9999999999),
            "type": 0,
            "zip": generate_fake_zip(),
            "city": get_random_item(bc_cities),
            "province": "BC",
            "building_number": randint(0, 99999),
            "unit_number": randint(0,1000),
            "street_name": get_random_item(fake_street_names),
            "card_number": str(randint(1000000000000000, 9999999999999999)),
            "expiration_date": randint(1000,5000),
            "bank_name": get_random_item(bank_names),
            "card_type": get_random_item(debit_credit),
            "payment_system": get_random_item(visa_mastercard)
        }
        register_user(fake_user_details)

if __name__ == "__main__":
    populate_register_user()