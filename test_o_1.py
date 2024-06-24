import unittest
import requests
from bs4 import BeautifulSoup
import json

url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
headers = {
  'user-agent': 'mozilla/5.0 (windows nt 10.0; win64; x64) chrome/58.0.3029.110 ',
}
response = requests.get(url, headers=headers)

class TestScraping(unittest.TestCase):

    def test_response_status_code(self):
        self.assertEqual(response.status_code, 200)

    def test_vacancies_scraping(self):
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        vacancies = soup.find_all("div", class_="vacancy-card--zuxteno7brgzxwvcl7y font-inter")
        self.assertTrue(len(vacancies) > 0)

    def test_json_export(self):
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        vacancies = soup.find_all("div", class_="vacancy-card--zuxteno7brgzxwvcl7y font-inter")
        vacancy_info = []
        for vacancy in vacancies:
            link = vacancy.find('a', class_='bloko-link').get('href')
            company = vacancy.find("span", class_="company-info-text--vgvzoultf8jwbmad1xgp").text
            city = vacancy.find("span", class_="fake-magritte-primary-text--hdw8fvkozzocor4xxwni").text.strip() if vacancy.find("span", class_="fake-magritte-primary-text--hdw8fvkozzocor4xxwni") else "не указан"
            salary = vacancy.find("span", class_="fake-magritte-primary-text--hdw8fvkozzocor4xxwni compensation-text--ktj0_rp54b2vnez3ctt2 separate-line-on-xs--mtby5go4j0ixtqzw38wh").text.strip() if vacancy.find("span", class_="fake-magritte-primary-text--hdw8fvkozzocor4xxwni compensation-text--ktj0_rp54b2vnez3ctt2 separate-line-on-xs--mtby5go4j0ixtqzw38wh") else "не указана"
            vacancy_info.append({
                'link': f"{link}",
                'company': company,
                'city': city,
                'salary': salary
            })

        with open('vacancyinfo.json', 'w', encoding='utf-8') as file:
            json.dump(vacancy_info, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    unittest.main()