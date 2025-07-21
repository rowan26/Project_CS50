import unittest
import project

class TestProject(unittest.TestCase):
    def test_convert(self):
        self.assertAlmostEqual(project.convert("Minutes to TV show episodes 🍿", 90), 2)
        self.assertAlmostEqual(project.convert("Kilograms to cats 🐈", 8), 2)
        self.assertAlmostEqual(project.convert("Meters to football fields 🏟️", 200), 2)
        self.assertAlmostEqual(project.convert("Liters to soda cans 🥤", 0.66), 2)

        with self.assertRaises(ValueError):  # ✅ attendu maintenant
            project.convert("Invalid choice", 100)

    def test_print_menu(self):
        self.assertTrue(callable(project.print_menu))

    def test_get_input(self):
        self.assertTrue(callable(project.get_input))

    def test_print_result(self):
        self.assertTrue(callable(project.print_result))

if __name__ == "__main__":
    unittest.main()
