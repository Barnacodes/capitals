"""Here we have a dictionary in which there is a list. In this list, each line is composed by a state(key) and his capital(value)"""

list_of_capitals = {'Aland Islands':'Mariehamn',
'Albania':'Tirana',
'Andorra':'Andorra la Vella',
'Armenia':'Yerevan',
'Austria':'Vienna',
'Azerbaijan':'Baku',
'Belarus':'Minsk',
'Belgium':'Brussels',
'Bosnia and Herzegovina':'Sarajevo',
'Bulgaria':'Sofia',
'Croatia':'Zagreb',
'Cyprus':'Nicosia',
'Czech Republic':'Prague',
'Denmark':'Copenhagen',
'Estonia':'Tallinn',
'Faroe Islands':'Torshavn',
'Finland':'Helsinki',
'France':'Paris',
'Georgia':'Tbilisi',
'Germany':'Berlin',
'Gibraltar':'Gibraltar',
'Greece':'Athens',
'Guernsey':'Saint Peter Port',
'Hungary':'Budapest',
'Iceland':'Reykjavik',
'Ireland':'Dublin',
'Isle of Man':'Douglas',
'Italy':'Rome',
'Jersey':'Saint Helier',
'Kosovo':'Pristina',
'Latvia':'Riga',
'Liechtenstein':'Vaduz',
'Lithuania':'Vilnius',
'Luxembourg':'Luxembourg',
'Macedonia':'Skopje',
'Malta':'Valletta',
'Moldova':'Chisinau',
'Monaco':'Monaco',
'Montenegro':'Podgorica',
'Netherlands':'Amsterdam',
'Northern Cyprus':'North Nicosia',
'Norway':'Oslo',
'Poland':'Warsaw',
'Portugal':'Lisbon',
'Romania':'Bucharest',
'Russia':'Moscow',
'San Marino':'San Marino',
'Serbia':'Belgrade',
'Slovakia':'Bratislava',
'Slovenia':'Ljubljana',
'Spain':'Madrid',
'Svalbard':'Longyearbyen',
'Sweden':'Stockholm',
'Switzerland':'Bern',
'Turkey':'Ankara',
'Ukraine':'Kyiv',
'United Kingdom':'London',
'Vatican City':'Vatican City'}


'''This function checks if the input is a state that appears in the list_of_capitals. If the state is within the list, it prints the state's name and his capital; if not, it prints that the state's name does not 
seem to be an European State'''

def check_capital(state_name):
    if state_name in list_of_capitals:
        print("The capital of {} is {}".format(state_name, list_of_capitals[state_name]))
    else:
        print("Sorry, {} does not seem to be an European state".format(state_name))


"""This function checks if the input is a capital that appears in the list_of_capitals. If the capital is within the list, it prints the capital's name and his state; if not, it prints that the capital does not seem to be an European Capital."""

def check_state(capital_name):
    for state, capital in list_of_capitals.items():
        if capital == capital_name:
            print("The European state whose capital is {} is {}".format(capital_name, state))
            return
    print("Sorry, {} is not the capital of any European state".format(capital_name))
