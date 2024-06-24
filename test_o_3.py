import unittest
import sys
sys.path.append('path_to_file_with_logic')  # путь к файлу с логикой

from o import vacancy_info

class TestGetVacancyInfo(unittest.TestCase):

    def test_vacancy_info_exists(self):
        vacancy_info = vacancy_info()
        self.assertTrue(vacancy_info)

if __name__ == '__main__':
    unittest.main()