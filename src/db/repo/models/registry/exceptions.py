""" Exceptions for registry tables. """

class RegistryTablesBaseError(Exception):
    """ Base for Registry table errors. """

class AttributesMissingError(RegistryTablesBaseError):
    """ At least one of the attributes must be infromed. """

__all__ = [
    "RegistryTablesBaseError", 
    "AttributesMissingError"
]
