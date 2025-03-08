# A Very Dumb Maybe Type

## What Makes It Dumb?

I does, stupid.

## How Do I Use It?

Please don't.

## OK, But Like, Suppose I Wanted to

Maybe lets you continue to chain calls when they might
fail or return None, without long if-else chains:

```python
>>> from maybe import maybe, get, attr
>>> class Order:
...     def __init__(self, customer):
...         self.customer = customer
... 
>>> order_no_contacts = Order({"fullname": "John Doe"})
>>> order_empty_contacts = Order({"contacts": []})
>>> correct_order = Order({"contacts": [{"type": "email", "address": "user@example.com"}]})
>>> 
>>> def get_contact_address(order):
...     return (
...             maybe(order)
...             .then(attr("customer"))
...             .then(get("contacts"))
...             .then(get(0))
...             .then(get("address"))
...             .value()
...         )
... 
>>> print(get_contact_address(None))
None
>>> print(get_contact_address(order_no_contacts))
None
>>> print(get_contact_address(order_empty_contacts))
None
>>> print(get_contact_address(correct_order))
user@example.com
>>> 
```

It also allows you to act on exceptions:

```python
>>> def get_contact_address(order):
...     return (
...         maybe(order)
...         .then(attr("customer"))
...         # If the order doesn't have .customer, try treating
...         # the order as a customer
...         .catch(AttributeError, lambda e: order)
...         .then(get("contacts"))
...         .then(get(0))
...         .then(get("address"))
...         .value()
...     )
... 
>>> print(get_contact_address({"contacts": [{"type": "email", "address": "second-user@example.com"}]}))
second-user@example.com
>>> print(get_contact_address(correct_order))
user@example.com
>>> 
```

Or on null values:

```python
>>> def get_contact_address(order):
...     return (
...         maybe(order)
...         .then(attr("customer"))
...         .catch(AttributeError, lambda e: order)
...         .then(get("contacts"))
...         .then(get(0))
...         .then(get("address"))
...         .or_else(lambda: "default-address@example.com")
...         .value()
...     )
... 
>>> order_none_contact = Order({"contacts": [{"type": "email", "address": None}]})
>>> print(get_contact_address(None))
default-address@example.com
>>> print(get_contact_address(order_none_contact))
default-address@example.com
>>> print(get_contact_address(correct_order))
user@example.com
```
