import unittest
from io import StringIO
from password import add, view

class TestProjectFunctions(unittest.TestCase):
    def setUp(self):
        # Create or clear the password file before each test
        with open("password.txt", "w"):
            pass

    def test_add_and_view(self):
        # Test adding a username and password, then viewing it
        test_username = "test_user"
        test_password = "test_password"

        # Call add function with test data
        add_input = f"{test_username}\n{test_password}\n"
        with StringIO(add_input) as stdin, StringIO() as stdout:
            add()
            # Capture the printed output by redirecting stdout
            view_output = stdout.getvalue().strip()

        # Check if the view function printed the correct output
        expected_output = f"User : {test_username} ,Password : {test_password}"
        self.assertIn(expected_output, view_output)

if __name__ == '__main__':
    unittest.main()
