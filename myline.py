typecolors = {'ノーマル': '#b1b1b1', 'ほのお': '#e4653f', 'みず': '#50abda', 'でんき': '#e8c71a', 'くさ': '#6cbe50', 'こおり': '#53c4e5', 'かくとう': '#e99a3f', 'どく': '#ba79c1', 'じめん': '#c8a841', 'ひこう': '#5e9fe2', 'エスパー': '#e885b2', 'むし': '#9ac30e',  'いわ': '#b08754', 'ゴースト': '#756eb4', 'ドラゴン': '#6c81c8', 'あく': '#5a3c1e', 'はがね': '#919191', 'フェアリー': '#e06cbb'}

def get_flex_json(results):
    contents = []
    cnt = 0
    for result in results:
        for poke in result:
            name = poke[0]
            typename = poke[1]
            text = poke[2]
            color = typecolors.get(typename, '#000000')
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
                            "text": text,
                            "color": "#000000",
                            "wrap": True,
                            "size": "sm"
                        }
                    ]
                }
            }
            contents.append(content)
            cnt += 1
            if cnt == 10:
                break
        else:
            continue
        break


    return {"type": "carousel", "contents": contents}
