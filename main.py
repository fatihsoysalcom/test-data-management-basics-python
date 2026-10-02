import re

# --- Simulated Application Logic ---
# This is the "system under test" (SUT), simulating a user registration service.
class UserService:
    def __init__(self):
        self.registered_users = set() # Stores usernames to check for uniqueness

    def register_user(self, username, email, password):
        """
        Simulates user registration with basic validation rules.
        Returns (success: bool, message: str)
        """
        if not username or not email or not password:
            return False, "All fields are required."
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False, "Invalid email format."
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if username in self.registered_users:
            return False, "Username already taken."
        
        # Simulate successful registration
        self.registered_users.add(username)
        return True, f"User '{username}' registered successfully."

# --- Test Automation Logic ---
def run_tests():
    user_service = UserService()

    # This structured list represents well-managed test data.
    # Each dictionary defines a specific test scenario with its input data and expected outcomes.
    # This systematic approach to data is a core "boring but critical" aspect of test automation.
    test_scenarios = [
        {
            "name": "Successful Registration",
            "data": {"username": "testuser1", "email": "test1@example.com", "password": "securepassword123"},
            "expected_success": True,
            "expected_message_part": "registered successfully"
        },
        {
            "name": "Duplicate Username",
            "data": {"username": "testuser1", "email": "test2@example.com", "password": "anotherpassword"},
            "expected_success": False,
            "expected_message_part": "Username already taken"
        },
        {
            "name": "Invalid Email Format",
            "data": {"username": "testuser2", "email": "invalid-email", "password": "securepassword123"},
            "expected_success": False,
            "expected_message_part": "Invalid email format"
        },
        {
            "name": "Password Too Short",
            "data": {"username": "testuser3", "email": "test3@example.com", "password": "short"},
            "expected_success": False,
            "expected_message_part": "Password must be at least 8 characters long"
        },
        {
            "name": "Missing Username",
            "data": {"username": "", "email": "test4@example.com", "password": "securepassword123"},
            "expected_success": False,
            "expected_message_part": "All fields are required"
        },
        {
            "name": "Another Successful Registration",
            "data": {"username": "testuser4", "email": "test4@example.com", "password": "longenoughpassword"},
            "expected_success": True,
            "expected_message_part": "registered successfully"
        },
    ]

    print("--- Running User Registration Tests ---")
    total_tests = len(test_scenarios)
    passed_tests = 0

    for i, scenario in enumerate(test_scenarios):
        print(f"\nScenario {i+1}: {scenario['name']}")
        
        # Extracting test data for the current scenario
        username = scenario['data'].get('username')
        email = scenario['data'].get('email')
        password = scenario['data'].get('password')

        # Call the system under test with structured test data
        success, message = user_service.register_user(username, email, password)

        # Assertions based on expected outcomes defined in the test data.
        # This ensures tests are reliable and predictable, a key aspect of good automation.
        if success == scenario['expected_success'] and scenario['expected_message_part'] in message:
            print(f"  PASS: Expected success={{scenario['expected_success']}}, Actual success={{success}}")
            print(f"        Message: '{message}' (contains '{{scenario['expected_message_part']}}')")
            passed_tests += 1
        else:
            print(f"  FAIL: Expected success={{scenario['expected_success']}}, Actual success={{success}}")
            print(f"        Expected message part: '{{scenario['expected_message_part']}}', Actual message: '{message}'")

    print(f"\n--- Test Summary ---")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")

    if passed_tests == total_tests:
        print("All tests passed!")
    else:
        print("Some tests failed. Review the failures above.")

if __name__ == "__main__":
    run_tests()
