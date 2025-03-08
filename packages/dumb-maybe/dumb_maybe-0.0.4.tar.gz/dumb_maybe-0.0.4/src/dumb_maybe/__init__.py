def maybe(obj=None):
    """
    Returns an object implementing the Maybe interface.

    Maybe lets you continue to chain calls when they might
    fail or return None, without long if-else chains:

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

    It also allows you to act on exceptions:

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
    """
    if obj is None:
        return No
    return Some(obj)

class Maybe:
    """
    A Maybe object either contains:
    - Some value (see `.then()`)
    - No value (see `.or_else()`)
    - An Exception (see `.catch()`)

    A Maybe object can't be constructed directly:
    use the `maybe()` factory function, or the `Some`
    (or `Except`) classes. A No object is also available.

    `bool(maybe)` and `if maybe:` will return True
    if the Maybe contains a value, False otherwise.

    `.then(f)` runs `f(value)` if
    the Maybe contains a value, then returns a
    Maybe with the result. If the Maybe contains
    no value, it returns itself.

    `.or_else(f)` runs `f()` if the Maybe contains
    no value or exception, then returns a Maybe with
    the result. If the Maybe contains a value or
    exception, it returns itself.

    `.catch(exception_class, f)` runs `f(exception)`
    if the Maybe contains an exception that is an
    instance of `exception_class`, and returns a
    Maybe with the result. If the Maybe contains
    no exception, it returns itself.

    `.value(default_value)` returns the value if the Maybe contains
    one, or `default_value` otherwise.
    """

    def __init__(self):
        raise NotImplemented

    def then(self, f):
        raise NotImplemented

    def catch(self, exception_class, f):
        raise NotImplemented

    def value(self, default=None):
        raise NotImplemented

    def or_else(self, f):
        raise NotImplemented

    def __bool__(self):
        raise NotImplemented

class Some(Maybe):
    def __init__(self, obj):
        self.__obj = obj

    def then(self, f):
        try:
            return maybe(f(self.__obj))
        except Exception as e:
            return Except(e)

    def catch(self, exception_class, f):
        return self

    def value(self, default=None):
        return self.__obj

    def or_else(self, f):
        return self

    def __bool__(self):
        return True

class Except(Maybe):
    def __init__(self, e):
        self.__e = e

    def then(self, f):
        return self

    def catch(self, exception_class, f):
        # if a catch raises, just raise
        if isinstance(self.__e, exception_class):
            return maybe(f(self.__e))

    def value(self, default=None):
        return default

    def or_else(self, f):
        return self

    def __bool__(self):
        return False

class NoType(Maybe):
    def __init__(self):
        # prevents NotImplemented
        pass

    def then(self, f):
        return self

    def catch(self, exception_class, f):
        return self

    def value(self, default=None):
        return default

    def or_else(self, f):
        try:
            return maybe(f())
        except Exception as e:
            return Except(e)

    def __bool__(self):
        return False

No = NoType()

def get(key):
    """
    Takes a key and returns an object access function.

    Examples:
    >>> maybe({"name": "Jane Doe"}).then(get("name")).value()
    'Jane Doe'
    >>> get(0)([1, 2, 3])
    1
    >>> get("name")({"name": "John Doe"})
    'John Doe'
    """
    return lambda obj: obj[key]

def attr(name):
    """
    Takes an attribute name and returns an object access function.

    Examples:
    >>> class Foo:
    ...     pass
    ... 
    >>> foo = Foo()
    >>> foo.bar = "bar"
    >>> attr("bar")(foo)
    'bar'
    >>> maybe(foo).then(attr("bar")).value()
    'bar'
    >>>
    """
    return lambda obj: getattr(obj, name)

def reraise(e):
    """
    Takes an exception and raises it. Intended to be passed to maybe.catch().
    """
    raise e
