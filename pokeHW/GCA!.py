import requests as r
# import time
# import numpy as np
# import sys






# machamp = r.get('https://pokeapi.co/api/v2/pokemon/machamp')
# if machamp.status_code == 200:
#     machamp = machamp.json()


# name, abilities, types, and weight .
# machamp['game_indices'][5]['version']['name']
# def delay_print(p):
#     for x in p:
#         sys.stdout.write(x)
#         sys.stdout.flush()
#         time.sleep(0.05)

# class Pokemon:
#     def __init__(self, name, name_ability, name_type, name_weight):
#         self.name = name
#         self.name_ability = name_ability
#         self.name_type = name_type
#         self.name_weight = name_weight




names = ['machamp', 'mewtwo', 'espurr','bewear', 'mew', 'metang', 'talonflame', 'magikarp', 'arcanine', 'buzzwole', 'sceptile', 'ditto', 'suicune', 'rotom', 'scizor', 'blaziken', 'lucario', 'greninja', 'metagross', 'squirtle']

for name in names:
    data = r.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if data.status_code == 200:
        data = data.json()
    # name_forms = [v['name'] for v in data['forms']]
    name_ability = [v['ability']['name'] for v in data['abilities']]
    name_type = [v['type']['name'] for v in data['types']]
    name_weight = [data['weight']]
    # print(name, name_ability, name_type, name_weight )
    
    print(input('Welcome Trainer!!\n'))
    name = input('Which pokemon would you like information on?: \n')
    print(name + 'is a great choice!\n')
    print(name, name_ability, name_type, name_weight )    

