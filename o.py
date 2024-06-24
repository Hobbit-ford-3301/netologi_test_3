# -

import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import os
import sys

os.environ['PYTHONIOENCODING'] = 'utf-8'

url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
keywords = ['Django', 'Flask']
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110 ',
}
response = requests.get(url, headers = headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    vacancies = soup.find_all("div", class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")
    vacancy_info = []  # Инициализация списка для хранения информации о вакансиях
    for vacancy in vacancies:
        link = vacancy.find('a', class_='bloko-link').get('href')
        company = vacancy.find("span", class_="company-info-text--vgvZouLtf8jwBmaD1xgp").text
        city = vacancy.find("span", class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni").text
        if city:
            city = city.strip()
        else:
            city = "Не указан"
            
        salary = vacancy.find("span", class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
        if salary:
            salary = salary.text.strip()
        else:
            salary = "Не указана"
            
        vacancy_info.append( {
            'link': f"{link}",
            'company': company,
            'city': city,
            'salary': salary
        } )

with open('vacancy_info.json', 'w', encoding='utf-8') as file:
    json.dump(vacancy_info, file, ensure_ascii=False, indent=4)