from operator import itemgetter

def alphabetize_names (dict_names):

    final_list_names = [] 
    for people in sorted(dict_names,key=itemgetter('last', 'first')):
        final_list_names.append(f'{people["last"]}, {people["first"]}: {people["email"]}')
    
    return final_list_names
    

PEOPLE = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'}
]

print(alphabetize_names(PEOPLE))
