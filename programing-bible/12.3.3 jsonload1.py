# loads 讀取 json 字串
import json

class_str = """
{
    "一年甲班": [
        {
            "座號": 1,
            "姓名": "Elliot",
            "國文": 65,
            "英文": 62,
            "數學": 40
        },
        {
            "座號": 2,
            "姓名": "Bonnie",
            "國文": 98,
            "英文": 90,
            "數學": 87
        },
        {
            "座號": 3,
            "姓名": "mask",
            "國文": 55,
            "英文": 80,
            "數學": 20
        }
    ]
}
"""

datas = json.loads(class_str)
print(type(datas))
for data in datas["一年甲班"]:
    print(data, data['姓名'])