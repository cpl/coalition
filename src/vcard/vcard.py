"""Main class of the VCARD parser/reader/writer/etc..."""

import os
from utility import Name, Address, PhoneNumber, EmailAddress
from defintions import BEGIN_VCARD, END_VCARD


class VCardObject(object):
    """Class for holding all interesting properties of a vcard."""

    def __init__(self):
        """Construct an empty vcard object."""
        self._name = Name()
        self._address = Address
        self._phonenumber = PhoneNumber

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
        self._content = None
        try:
            with open(filepath, 'r') as file:
                self._content = file.readlines()
        except Exception as exception:
            raise exception

    def parse(self):
        """Parse the vCard File into vCard Python Objects."""
        encounterBegin = False
        for index, line in enumerate(self._content):
            line = line.rstrip()

            # Check for valid vCard
            if not encounterBegin:
                # Check for BEGIN:VCARD, at the start
                if line != BEGIN_VCARD:
                    raise Exception('{} Missing {}'.format(index, BEGIN_VCARD))
                else:
                    encounterBegin = True
            else:
                # Check for END:VCARD, at the end
                if line == END_VCARD:
                    encounterBegin = False
                    print
                elif line == BEGIN_VCARD:
                    raise Exception('{} Missing {}'.format(index, END_VCARD))
                else:
                    print line


if __name__ == '__main__':
    vcard_file = VCardFile('tests/sample.vcf')
    vcard_file.parse()

