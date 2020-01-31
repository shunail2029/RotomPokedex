from google.cloud import firestore

db = firestore.Client()

def get_pokemon(name):
    message_list = []
    docs = db.collection('pokeinfo').where('keywords', 'array_contains', name).order_by('id').limit(10).stream()
    for doc in docs:
        res = doc.to_dict()
        message = [res['name'], res['type'].split('/')[0], f'''タイプ: {res['type']}\n-- 種族値 --\nたいりょく: {res['hit_point']}\nこうげき:     {res['attack']}\nぼうぎょ:     {res['defense']}\nとくこう:     {res['special_attack']}\nとくぼう:     {res['special_defense']}\nすばやさ:     {res['speed']}\nごうけい:     {res['sum']}''']
        message_list.append(message)

    if not message_list:
        message_list.append([name, False])
    return message_list
