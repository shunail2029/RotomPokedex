def get_type_color(typename):
    if typename == 'ノーマル':
        return "#b1b1b1"
    elif typename == 'ほのお':
        return "#e4653f"
    elif typename == 'みず':
        return "#50abda"
    elif typename == 'でんき':
        return "#e8c71a"
    elif typename == 'くさ':
        return "#6cbe50"
    elif typename == 'こおり':
        return "#53c4e5"
    elif typename == 'かくとう':
        return "#e99a3f"
    elif typename == 'どく':
        return "#ba79c1"
    elif typename == 'じめん':
        return "#c8a841"
    elif typename == 'ひこう':
        return "#5e9fe2"
    elif typename == 'エスパー':
        return "#e885b2"
    elif typename == 'むし':
        return "#9ac30e"
    elif typename == 'いわ':
        return "#b08754"
    elif typename == 'ゴースト':
        return "#756eb4"
    elif typename == 'ドラゴン':
        return "#6c81c8"
    elif typename == 'あく':
        return "#5a3c1e"
    elif typename == 'はがね':
        return "#919191"
    elif typename == 'フェアリー':
        return "#e06cbb"
    else:
        return "#000000"

def get_flex_json(results):
    contents = []
    for result in results:
        for poke in result:
            name = poke[0]
            typename = poke[1]
            text = poke[2]
            color = get_type_color(typename)
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

    return {"type": "carousel", "contents": contents[:10]}
