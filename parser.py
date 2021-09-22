#import requests
import re
import json

from bs4 import BeautifulSoup

# url = "https://hh.ru/vacancies/data-scientist"
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
#                   "like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open('hh.html','w',encoding='UTF-8') as file:
#     file.write(src)

# with open('hh.html', encoding='UTF-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
#
# blocks_of_info = soup.find("div", class_="vacancy-serp").find_all({"a": {'data-qa':
#                                                               "vacancy-serp__vacancy-title"}})
#
# link = ''
# name_of_vacancy = ''
# name_of_company = ''
# all_vacancies_dict = {}
#
# for item in blocks_of_info:
#     if link != '' and name_of_vacancy != '' and name_of_company != '':
#         all_vacancies_dict[name_of_vacancy + " " + name_of_company.replace('\xa0', " ")] = link
#         link = ''
#         name_of_vacancy = ''
#         name_of_company = ''
#
#     if 'vacancy' in item['href'] and 'https' in item['href']:
#         link = item['href']
#         name_of_vacancy = item.text
#         print(link)
#         print(name_of_vacancy)
#     if 'employer' in item['href'] and item.text != '':
#         name_of_company = item.text.strip()
#         print(name_of_company)
#
# with open("all_vacancies_dict.json", "w", encoding='utf-8') as file:
#     json.dump(all_vacancies_dict, file, indent=4, ensure_ascii=False)
#
#
# print(all_vacancies_dict)





