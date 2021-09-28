#!/usr/bin/env python3
from dev_aberto import hello

import gettext
gettext.install('pacote_python', localedir='locale')

if __name__ == '__main__':
    date, name = hello()
    print(_('Último commit feito em:'), date, _(' por'), name)
