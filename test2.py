from faker import Faker
import random

fake = Faker()

def generate_orders(num_orders):
    orders = []
    for i in range(num_orders):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        address = fake.address()
        product = fake.random_element(elements=['Refrigerator', 'Washing Machine', 'Dryer', 'Stove', 'Dishwasher'])
        price = random.uniform(500, 2500)
        card_num = fake.credit_card_number()
        card_exp = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")

        order = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "address": address,
            "product": product,
            "price": price,
            "card_num": card_num,
            "card_exp": card_exp
        }

        orders.append(order)

    return orders

fake_orders = generate_orders(100)

print(fake_orders)
