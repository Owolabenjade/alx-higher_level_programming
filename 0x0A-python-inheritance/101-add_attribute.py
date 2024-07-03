#!/usr/bin/python3
"""
Module for add_attribute function.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        error_message = "can't add new attribute"
        error_class = TypeError
        raise error_class(error_message)


if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    class AnotherClass:
        __slots__ = ["data"]

    ac = AnotherClass()
    add_attribute(ac, "data", 42)
    print(ac.data)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
