"""Main class of the VCARD parser/reader/writer/etc..."""

import os
from defintions import NAME_COLONS as NAME


class VCardObject(object):
    """Class for holding all interesting properties of a vcard."""

    def __init__(self):
        """Construct an empty vcard object."""
        self._firname = None
        self._surname = None
        self._telephone = None
        self._email = None

    def __str__(self):
        """Return the string containing all variables."""
        return 'VCardObject({})'.format(vars(self))

    def __repr__(self):
        """Return the __str__ string."""
        return self.__str__()


class VCardFile(object):
    """Class for holding and handling a vcard [.vcf] file."""

    def __init__(self, filepath):
        """Construct a file VCard object from a file."""
        # Check that file exists
        if not os.path.isfile(filepath):
            raise IOError('Missing file and/or no read permissions.')

        # Attempt to read file content
        try:
            with open(filepath, 'r') as file:
                content = file.readlines()
        except Exception as exception:
            raise exception

        # Split each line into key/value pairs
        for index, line in enumerate(content):
            line = line.rstrip()
            if not line.startswith(' '):
                line = line.split(':')
                key, value = line[0], line[1]
                if key == NAME:
                    print value
            else:
                pass


if __name__ == '__main__':
    vcard_file = VCardFile('tests/apple.vcf')
    vcard_obj = VCardObject()
