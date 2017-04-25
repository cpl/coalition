# -*- coding: utf-8 -*-
"""The main file of the coalition software package."""

import vcard
import locale

# VERSION USED BY PYPI
__version__ = '0.0.0dev5'


def main():
    """Main."""
    print 'Main was ran'


def p_vcard():
    """Vcard."""
    print 'Vcard'
    print dir(vcard)


def p_locale():
    """Locale."""
    print 'Locale'
    print dir(locale)


if __name__ == '__main__':
    main()
