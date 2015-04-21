"""
:mod:`source.lab2menu` -- Example source code
============================================

The following example code determines the nature of the commands given
"""


def do_something(a=' '):
    """
    Determine what to do with the command given

    :param a: Command
    :type a: str

    :return: 'quitting'
    :rtype: str
    """
    if a == 'X':
        return 'quitting'
    elif a == '?':
            return 'giving options'
    elif a == 'd':
        return 'generating orc listing..'
    elif a == 'ENTer the trees':
        return 'you win'
