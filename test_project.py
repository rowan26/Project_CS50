import unittest
from unittest.mock import patch
import project

class TestProject(unittest.TestCase):

    def test_convert(self):
        self.assertAlmostEqual(project.convert("Minutes to TV show episodes 🍿", 90), 2)
        self.assertAlmostEqual(project.convert("Kilograms to cats 🐈", 8), 2)
        self.assertAlmostEqual(project.convert("Meters to football fields 🏟️", 200), 2)
        self.assertAlmostEqual(project.convert("Liters to soda cans 🥤", 0.66), 2)
        self.assertIsNone(project.convert("Invalid choice", 100))

    @patch('streamlit.selectbox')
    def test_print_menu(self, mock_selectbox):
        mock_selectbox.return_value = "Kilograms to cats 🐈"
        choice = project.print_menu()
        self.assertEqual(choice, "Kilograms to cats 🐈")
        mock_selectbox.assert_called_once()

    @patch('streamlit.number_input')
    def test_get_input(self, mock_number_input):
        mock_number_input.return_value = 10
        value = project.get_input()
        self.assertEqual(value, 10)
        mock_number_input.assert_called_once()

    @patch('streamlit.success')
    def test_print_result(self, mock_success):

        project.print_result("Minutes to TV show episodes 🍿", 90, 2)
        project.print_result("Kilograms to cats 🐈", 8, 2)
        project.print_result("Meters to football fields 🏟️", 200, 2)
        project.print_result("Liters to soda cans 🥤", 0.66, 2)

        self.assertTrue(mock_success.call_count, 4)

if __name__ == "__main__":
    unittest.main()

