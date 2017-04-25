"""A set of helper classes."""

import re


class Address(object):
    """A representation of a common address."""

    def __init__(self, street=None, city=None, region=None, postcode=None,
                 country=None, extra=None, category=None):
        """Construct an address."""
        self._category = category
        self._street = street
        self._city = city
        self._region = region
        self._postcode = postcode
        self._country = country
        self._extra = extra

    def __str__(self):
        """Return all the variables of the name in a string."""
        return 'Address({})'.format(vars(self))

    def __repr__(self):
        """Use the same string from __str__."""
        return self.__str__()


class Location(object):
    """Build an address from a set of coordinates or the other way around."""

    def __init__(self, coordinates=None, address=None):
        """Construct one with the other, or store both."""
        if coordinates is None and address is None:
            raise ValueError('Provide an address or set of coordinates.')

        if not isinstance(coordinates, tuple) and len(coordinates) != 2:
            raise TypeError('Coordinates must be a tuple of two.')
        self._coordinates = coordinates

        if not isinstance(address, Address):
            raise TypeError('Address must be an address of type Address.')
        self._address = address

    def get_coordinates(self):
        """Return the coordinates for the current location."""
        pass

    def get_address(self):
        """Return the address for the curent location."""
        pass


class Name(object):
    """A representation of a possible name."""

    def __init__(self, given=None, family=None, middle=None, nickname=None,
                 prefix=None, suffix=None):
        """Construct a name."""
        self._given = given
        self._family = family
        self._middle = middle
        self._nick = nickname
        self._prefix = prefix
        self._suffix = suffix

    def __str__(self):
        """Return all the variables of the name in a string."""
        return 'Name({})'.format(vars(self))

    def __repr__(self):
        """Use the same string from __str__."""
        return self.__str__()


class PhoneNumber(object):
    """A representation of a phone number."""

    # TODO: Finish the two way phone number input.
    def __init__(self, prefix=None, country=None, provider=None, number=None):
        """Contruct a phone number."""
        if prefix is not None:
            self._prefix = prefix
        if country is not None:
            self._country = country

        self._provider = provider
        self._number = number


class EmailAddress(object):
    """A email representation and validator."""

    EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')

    def __init__(self, email_address):
        """Validate and construct an email."""
        if self.EMAIL_REGEX.match(email_address):
            email_address = email_address.split('@')

            self._local = email_address[0]
            self._domain = email_address[1]
        else:
            raise Exception('Invalid email, {}'.format(email_address))

    def __str__(self):
        """Return all the variables of the email address in a string."""
        return 'EmailAddress({}@{})'.format(self._local, self._domain)

    def __repr__(self):
        """Use the same string from __str__."""
        return self.__str__()


class Day(object):
    """A date parsing class."""

    def __init__(self, date):
        """Validate and store the date as UNIX epoch."""
        pass
