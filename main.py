#! /usr/bin/env python3\


#from CapitalsFolder import capitals

import argparse
import csv

from CapitalsFolder.csvcode import check_input

csv_folder = 'CapitalsFolder/capitals.csv'
csv_reader = csv.reader(open(csv_folder, 'r'))

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('name', help ='Please, insert the capital or the state')
    parser.add_argument('-v', '--verbosity',
    help = 'Incrementally increase the verbosity', action='count', default=0)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    #capitals.check_capital(args)
    #capitals.check_state(args)
    check_input(args.name)