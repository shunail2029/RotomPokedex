import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def get_connection():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def get_pokemon(name):
    message_list = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f'''SELECT * FROM pokeinfo WHERE name LIKE '%{name}%' ORDER BY id;''')
            for row in cur:
                message = [row[1], row[2].split('/')[0], f'タイプ: {row[2]}\n-- 種族値 --\nたいりょく: {row[3]}\nこうげき:     {row[4]}\nぼうぎょ:     {row[5]}\nとくこう:     {row[6]}\nとくぼう:     {row[7]}\nすばやさ:     {row[8]}\nごうけい:     {row[9]}']
                message_list.append(message)

    if not message_list:
        message_list.append([name, '', 'このなまえのポケモンは見つからなかったロト...'])
    return message_list
