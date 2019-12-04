#! /usr/bin/env python3\

'''In the main.py we are importing the module check
from mypackage'''

from CapitalsFolder import capitals

import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'check':
            capitals.check_capital("Germany")
            capitals.check_capital("Honduras")
            capitals.check_state("Rome")
            capitals.check_state("Tokyo")
        else:
            capitals.check_state(sys.argv[1])
            capitals.check_capital(sys.argv[1])
