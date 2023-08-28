from customer import Customer
from restaurant import Restaurant
from review import Review

def find_by_name(name):
    for customer in Customer.all():
        if customer.full_name() == name:
            return customer
    return None

def find_all_by_given_name(name):
    return [customer for customer in Customer.all() if customer.given_name == name]


