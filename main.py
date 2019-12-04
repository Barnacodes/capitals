#! /usr/bin/env python3\

'''In the main.py we are importing the module check from mypackage'''
      
from CapitalsFolder import capitals

import sys


if _name_ == "_main_":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'check':
            capitalscopia.check_capital("Germany")
            capitalscopia.check_capital("Honduras")
            capitalscopia.check_state("Rome")
            capitalscopia.check_state("Tokyo")
        else:
            capitalscopia.check_state(sys.argv[1])
            capitalscopia.check_capital(sys.argv[1])



