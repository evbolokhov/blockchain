# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

import json
import re

from bs4 import BeautifulSoup

link = "	https://spb.hh.ru/account/login?backurl=/"

data = {}

responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id = "tool_padding")

print (block)


# =============================================================================
# m = re.search('var elementsArr = (.+);', rs.text)
# 
# if not m:
#     print(f'[-] Не удалось регуляркой найти "var elementsArr"')
#     # И в зависимости от места вызова:
#     # return      # Выходим из функции
#     # sys.exit()  # или завершаем работу скрипта
# 
# data = json.loads(m.group(1))
# points = data['points']
# 
# print(f'Points ({len(points)}):')
# for p in points:
#     print(f"  lat: {p['lat']}, lng: {p['lng']}")
# =============================================================================
