from dumb_maybe_the_madman import maybe, get, attr

class Order:
    def __init__(self, customer):
        self.customer = customer

order_no_contacts = Order({"fullname": "John Doe"})
order_empty_contacts = Order({"contacts": []})
correct_order = Order({"contacts": [{"type": "email", "address": "user@example.com"}]})

def get_contact_address(order):
    return (
            maybe(order)
            .then(attr("customer"))
            .then(get("contacts"))
            .then(get(0))
            .then(get("address"))
            .value()
        )

print(get_contact_address(None)) # None
print(get_contact_address(order_no_contacts)) # None
print(get_contact_address(order_empty_contacts)) # None
print(get_contact_address(correct_order)) # "user@example.com"

def get_contact_address(order):
    return (
        maybe(order)
        .then(attr("customer"))
        # If the order doesn't have .customer, try treating
        # the order as a customer
        .catch(AttributeError, lambda e: order)
        .then(get("contacts"))
        .then(get(0))
        .then(get("address"))
        .value()
    )

print(get_contact_address({"contacts": [{"type": "email", "address": "second-user@example.com"}]}))

def get_contact_address(order):
    return (
        maybe(order)
        .then(attr("customer"))
        .catch(AttributeError, lambda e: order)
        .then(get("contacts"))
        .then(get(0))
        .then(get("address"))
        .or_else(lambda: "default-address@example.com")
        .value()
    )

order_none_contact = Order({"contacts": [{"type": "email", "address": None}]})
print(get_contact_address(None))
print(get_contact_address(order_none_contact))
print(get_contact_address(correct_order))

class Foo:
    pass

foo = Foo()
foo.bar = "bar"
attr("bar")(foo)
maybe(foo).then(attr("bar")).value()
