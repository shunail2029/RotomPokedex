typecolors = {
    'ノーマル': '#b1b1b1',
    'ほのお': '#e4653f',
    'みず': '#50abda',
    'でんき': '#e8c71a',
    'くさ': '#6cbe50',
    'こおり': '#53c4e5',
    'かくとう': '#e99a3f',
    'どく': '#ba79c1',
    'じめん': '#c8a841',
    'ひこう': '#5e9fe2',
    'エスパー': '#e885b2',
    'むし': '#9ac30e',
    'いわ': '#b08754',
    'ゴースト': '#756eb4',
    'ドラゴン': '#6c81c8',
    'あく': '#5a3c1e',
    'はがね': '#919191',
    'フェアリー': '#e06cbb'}


def text_centered(text):
    return {
        "type": "text",
        "text": text,
        "color": "#000000",
        "wrap": True,
        "size": "sm",
        "align": "center"
    }


def get_flex_json(results):
    contents = []
    cnt = 0
    for poke in results:
        name = poke['name']
        if '(' in name:
            name = name.split('(')[0] + '\n(' + name.split('(')[1]
        color = typecolors.get(poke['type'].split('/')[0], '#000000')
        content = {"type": "bubble",
                   "size": "micro",
                   "styles": {"header": {"backgroundColor": color},
                              "body": {"backgroundColor": "#ffffff"}},
                   "header": {"type": "box",
                              "layout": "vertical",
                              "contents": [{"type": "text",
                                            "text": name,
                                            "color": "#ffffff",
                                            "wrap": True,
                                            "size": "sm"}]},
                   "body": {"type": "box",
                            "layout": "vertical",
                            "contents": [text_centered('--- タイプ ---'),
                                         text_centered(poke['type']),
                                         text_centered('--- 種族値 ---'),
                                         {"type": "box",
                                          "layout": "horizontal",
                                          "contents": [{"type": "box",
                                                        "layout": "vertical",
                                                        "contents": [text_centered('たいりょく'),
                                                                     text_centered('こうげき'),
                                                                     text_centered('ぼうぎょ'),
                                                                     text_centered('とくこう'),
                                                                     text_centered('とくぼう'),
                                                                     text_centered('すばやさ'),
                                                                     text_centered('ごうけい')],
                                                        "flex": 1},
                                                       {"type": "box",
                                                        "layout": "vertical",
                                                        "contents": [text_centered(str(poke['hit_point'])),
                                                                     text_centered(str(poke['attack'])),
                                                                     text_centered(str(poke['defense'])),
                                                                     text_centered(str(poke['special_attack'])),
                                                                     text_centered(str(poke['special_defense'])),
                                                                     text_centered(str(poke['speed'])),
                                                                     text_centered(str(poke['sum']))],
                                                        "flex": 1}]}]}}
        contents.append(content)
        cnt += 1
        if cnt == 10:
            break

    return {"type": "carousel", "contents": contents}
