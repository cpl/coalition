"""Main class of the VCARD parser/reader/writer/etc..."""

import os
from .utility import Name, Address, PhoneNumber, EmailAddress
from .defintions import BEGIN_VCARD, END_VCARD


class VCardObject(object):
    """Class for holding all interesting properties of a vcard."""

    def __init__(self):
        """Construct an empty vcard object."""
        self._name = Name()
        self._address = Address
        self._phonenumber = PhoneNumber
        self._email = EmailAddress

    def __str__(self):
        """Return the string containing all variables."""
        return 'VCardObject({})'.format(vars(self))

    def __repr__(self):
        """Return the __str__ string."""
        return self.__str__()

    @staticmethod
    def parse_from_file(vcard_file):
        """Return a VCardObject from a VCardFile."""
        for line in vcard_file:
            print(line)


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

        # Check for empty file
        if os.stat(filepath).st_size == 0:
            raise Exception('Empty file: {}'.format(filepath))

        # Check for missing BEGIN and END, VCARD
        if self._content[0].rstrip() != BEGIN_VCARD \
           or self._content[-1].rstrip() != END_VCARD:
            raise Exception('Invalid VCF file: {}'.format(filepath))

    def split(self):
        """Description."""
        begin = None
        vcard_list = []

        # Process each line
        for index, line in enumerate(self._content):
            line = line.rstrip()

            # Check for begin index
            if begin is None:
                # Assign a new begin index or raise an error
                if line == BEGIN_VCARD:
                    begin = index
                else:
                    raise Exception('Missing BEGIN:VCARD {}'.format(index))
            # Check for end of VCARD
            elif line == END_VCARD:
                vcard_list.append(self._content[begin:index])
                begin = None
            # Error if BEGIN was found after BEGIN and before END
            elif line == BEGIN_VCARD:
                raise Exception('Missing END:VCARD {}:{}'.format(index, begin))

        return vcard_list


if __name__ == '__main__':
    vcard_file = VCardFile('tests/sample.vcf')
    vcard_list = vcard_file.split()

    vcard_object = VCardObject.parse_from_file(vcard_list[0])
