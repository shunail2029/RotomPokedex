from google.cloud import firestore

db = firestore.Client()

def get_pokemon(name):
    message_list = []
    docs = db.collection('pokeinfo').where('keywords', 'array_contains', name).order_by('id').limit(11).stream()
    for doc in docs:
        res = doc.to_dict()
        message = {
            'name': res['name'],
            'type': res['type'],
            'hit_point': res['hit_point'],
            'attack': res['attack'],
            'defense': res['defense'],
            'special_attack': res['special_attack'],
            'special_defense': res['special_defense'],
            'speed': res['speed'],
            'sum': res['sum']
        }
        message_list.append(message)

    if not message_list:
        message_list.append([name, False])
    return message_list
