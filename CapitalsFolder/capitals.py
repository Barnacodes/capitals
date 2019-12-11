'''Here we have a dictionary in which there is a list.
In this list, each line is composed by a state(key) and his capital(value)'''

list_of_capitals = {'Aland Islands': 'Mariehamn',
                    'Albania': 'Tirana',
                    'Andorra': 'Andorra la Vella',
                    'Armenia': 'Yerevan',
                    'Austria': 'Vienna',
                    'Azerbaijan': 'Baku',
                    'Belarus': 'Minsk',
                    'Belgium': 'Brussels',
                    'Bosnia and Herzegovina': 'Sarajevo',
                    'Bulgaria': 'Sofia',
                    'Croatia': 'Zagreb',
                    'Cyprus': 'Nicosia',
                    'Czech Republic': 'Prague',
                    'Denmark': 'Copenhagen',
                    'Estonia': 'Tallinn',
                    'Faroe Islands': 'Torshavn',
                    'Finland': 'Helsinki',
                    'France': 'Paris',
                    'Georgia': 'Tbilisi',
                    'Germany': 'Berlin',
                    'Gibraltar': 'Gibraltar',
                    'Greece': 'Athens',
                    'Guernsey': 'Saint Peter Port',
                    'Hungary': 'Budapest',
                    'Iceland': 'Reykjavik',
                    'Ireland': 'Dublin',
                    'Isle of Man': 'Douglas',
                    'Italy': 'Rome',
                    'Jersey': 'Saint Helier',
                    'Kosovo': 'Pristina',
                    'Latvia': 'Riga',
                    'Liechtenstein': 'Vaduz',
                    'Lithuania': 'Vilnius',
                    'Luxembourg': 'Luxembourg',
                    'Macedonia': 'Skopje',
                    'Malta': 'Valletta',
                    'Moldova': 'Chisinau',
                    'Monaco': 'Monaco',
                    'Montenegro': 'Podgorica',
                    'Netherlands': 'Amsterdam',
                    'Northern Cyprus': 'North Nicosia',
                    'Norway': 'Oslo',
                    'Poland': 'Warsaw',
                    'Portugal': 'Lisbon',
                    'Romania': 'Bucharest',
                    'Russia': 'Moscow',
                    'San Marino': 'San Marino',
                    'Serbia': 'Belgrade',
                    'Slovakia': 'Bratislava',
                    'Slovenia': 'Ljubljana',
                    'Spain': 'Madrid',
                    'Svalbard': 'Longyearbyen',
                    'Sweden': 'Stockholm',
                    'Switzerland': 'Bern',
                    'Turkey': 'Ankara',
                    'Ukraine': 'Kyiv',
                    'United Kingdom': 'London',
                    'Vatican City': 'Vatican City'}

''' The below functions check the given input
    return the State or the Capital.
    They also allow to add different degrees of
    verbosity depending on how much we want the
    output to be deepened '''


def check_capital(args):
    state = ''
    for country, capital in list_of_capitals.items():
        if capital == args.name:
            state = country
    if args.name in list_of_capitals.values():
        if args.verbosity >= 2:
            print('entrato')
            print("We are checking your input in order",
                  "to understand if it is contained in",
                  "the list of capitals... \nThe capital",
                  "of {} is {}".format(state, args.name))
        elif args.verbosity >= 1:
            print("The capital of {} is {}".format(state, args.name))
        else:
            print(state)
    elif capital not in list_of_capitals.values():
        print("Sorry, {} is not the capital",
              "of any European state".format(args.name))


def check_state(args):
    for state, capital in list_of_capitals.items():
        if state == args.name:
            if args.verbosity >= 2:
                print("We are checking your input",
                      "in order to understand if it",
                      "is contained in the list of",
                      "capitals... \nThe European state",
                      "whose capital is {} is {}".format(capital, state))
            elif args.verbosity >= 1:
                print("The European state whose capital",
                      "is {} is {}".format(capital, state))
            else:
                print(capital)
        elif state not in list_of_capitals.keys():
            print("Sorry, {} is not a European state".format(capital))
