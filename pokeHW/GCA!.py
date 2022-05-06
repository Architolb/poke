import requests as r


# machamp = r.get('https://pokeapi.co/api/v2/pokemon/machamp')
# if machamp.status_code == 200:
#     machamp = machamp.json()


# name, abilities, types, and weight .
# machamp['game_indices'][5]['version']['name']


names = ['machamp', 'mewtwo', 'espurr','bewear', 'arceus', 'metang', 'talonflame', 'magikarp', 'arcanine', 'buzzwole', 'sceptile', 'aegislash', 'suicune', 'rotom', 'scizor', 'blaziken', 'lucario', 'greninja', 'metagross', 'mimikyu']

for names in [names]:
    data = r.get(f'https://pokeapi.co/api/v2/pokemon/{names}')
    if data.status_code == 200:
        data = data.json()
    name_data = [v['name'] for v in data['forms']]
    name_data = [v['ability']['name'] for v in data['abilities']]
    name_data = [v['type']['name'] for v in data['types']]
    name_data = [v['weight'] for v in data['weight']]
    print(data[name_data])
    