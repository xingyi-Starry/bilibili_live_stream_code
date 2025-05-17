import requests
import json
from data import header

def get_new_partition(cookies: dict):
    url = "https://api.live.bilibili.com/room/v1/Area/getList?show_pinyin=1"
    headers = header

    resp = requests.get(url, cookies=cookies, headers=headers)

    pt_data = resp.json()

    with open("partition.json", "w", encoding="utf-8") as f:
        json.dump(pt_data, f, ensure_ascii=False, indent=4)
