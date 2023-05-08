"""Test file for testing the functions in main.py file"""

import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)
from main import largest_sum  # nopep8 pylint: disable=wrong-import-position


class TestLargestSum(unittest.TestCase):
    """Class for testing the main.py file"""

    def test_largest_sum(self):
        """Test the largest_sum function"""
        lista = [1, 2, 3, 4, 5]
        resultado_esperado = (4, 5)
        self.assertEqual(largest_sum(lista), resultado_esperado)

        lista = [5, 4, 3, 2, 1]
        resultado_esperado = (4, 5)
        self.assertEqual(largest_sum(lista), resultado_esperado)

        lista = [10, -5, 20, 15, -30]
        resultado_esperado = (15, 20)
        self.assertEqual(largest_sum(lista), resultado_esperado)

        lista = [0, 0, 0, 0]
        resultado_esperado = (0, 0)
        self.assertEqual(largest_sum(lista), resultado_esperado)

        lista = [-10, -5, -2, -1]
        resultado_esperado = (-2, -1)
        self.assertEqual(largest_sum(lista), resultado_esperado)

        lista = [5]
        resultado_esperado = None
        self.assertEqual(largest_sum(lista), resultado_esperado)

        lista = []
        resultado_esperado = None
        self.assertEqual(largest_sum(lista), resultado_esperado)


if __name__ == "__main__":
    unittest.main()
