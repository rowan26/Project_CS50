import project

def test_convert():
    assert round(project.convert("Minutes to TV show episodes 🍿", 90), 2) == 2
    assert round(project.convert("Kilograms to cats 🐈", 8), 2) == 2
    assert round(project.convert("Meters to football fields 🏟️", 200), 2) == 2
    assert round(project.convert("Liters to soda cans 🥤", 0.66), 2) == 2

    try:
        project.convert("Invalid choice", 100)
        assert False, "ValueError not raised for invalid choice"
    except ValueError:
        pass  # ✅ attendu

def test_print_menu():
    assert callable(project.print_menu)

def test_get_input():
    assert callable(project.get_input)

def test_print_result():
    assert callable(project.print_result)

if __name__ == "__main__":
    test_convert()
    test_print_menu()
    test_get_input()
    test_print_result()
    print("✅ Tous les tests ont réussi.")
