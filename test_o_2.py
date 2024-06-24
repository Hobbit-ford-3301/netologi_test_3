import unittest
import sys

from o import vacancy_info

class TestGetVacancyInfo(unittest.TestCase):

    def test_company_type(self):
        vacancy_info = vacancy_info()
        for vacancy in vacancy_info:
            self.assertTrue(isinstance(vacancy['company'], str))

    def test_links_exist(self):
        vacancy_info = vacancy_info()
        for vacancy in vacancy_info:
            self.assertTrue(vacancy['link'])

if __name__ == '__main__':
    unittest.main()