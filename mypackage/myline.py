typecolors = {'ノーマル': '#b1b1b1', 'ほのお': '#e4653f', 'みず': '#50abda', 'でんき': '#e8c71a', 'くさ': '#6cbe50', 'こおり': '#53c4e5', 'かくとう': '#e99a3f', 'どく': '#ba79c1', 'じめん': '#c8a841', 'ひこう': '#5e9fe2', 'エスパー': '#e885b2', 'むし': '#9ac30e',  'いわ': '#b08754', 'ゴースト': '#756eb4', 'ドラゴン': '#6c81c8', 'あく': '#5a3c1e', 'はがね': '#919191', 'フェアリー': '#e06cbb'}

def get_flex_json(results):
    contents = []
    cnt = 0
    for poke in results:
        name = poke['name']
        if '(' in name:
            name = name.split('(')[0] + '\n(' + name.split('(')[1]
        color = typecolors.get(poke['type'].split('/')[0], '#000000')
        content = {
            "type": "bubble",
            "size": "micro",
            "styles": {
                "header": {
                    "backgroundColor": color
                },
                "body": {
                    "backgroundColor": "#ffffff"
                }
            },
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": name,
                        "color": "#ffffff",
                        "wrap": True,
                        "size": "sm"
                    }
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "タイプ: " + poke['type'],
                        "color": "#000000",
                        "wrap": True,
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "--- 種族値 ---",
                        "color": "#000000",
                        "wrap": True,
                        "size": "sm",
                        "align": "center"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "たいりょく",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "こうげき",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "ぼうぎょ",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "とくこう",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "とくぼう",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "すばやさ",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "ごうけい",
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    }
                                ],
                                "flex": 1
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": str(poke['hit_point']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(poke['attack']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(poke['defense']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(poke['special_attack']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(poke['special_defense']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(poke['speed']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(poke['sum']),
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "sm",
                                        "align": "center"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
        contents.append(content)
        cnt += 1
        if cnt == 10:
            break

    return {"type": "carousel", "contents": contents}
