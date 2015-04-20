"""
:mod:`source.lab2quit` -- Example source code
============================================

The following example code determines if quit command has been given
"""


def do_quit(a=' '):
    """
    Determine if the given command is 'X'

    :param a: QuitCommand
    :type a: int

    :return: 'quitting'
    :rtype: str
    """
    if a == 'X':
        return 'quitting'