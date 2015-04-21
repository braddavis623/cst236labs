"""
:mod:`source.lab2menu` -- Example source code
============================================

The following example code determines the nature of the commands given
"""


def do_something(a=' '):
    """
    Determine what to do with the command given

    :param a: Command
    :type a: char

    :return: 'quitting'
    :rtype: str
    """
    if a == 'X':
        return 'quitting'
    else:
        if a == '?':
            return 'giving options'
