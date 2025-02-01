import unittest
import importlib.util
import sys

# Path to the student's solution file
STUDENT_SOLUTION_PATH = "solution.py"  # Update this if needed

# Dynamically import student's solution as a module
spec = importlib.util.spec_from_file_location("solution", STUDENT_SOLUTION_PATH)
student_solution = importlib.util.module_from_spec(spec)
sys.modules["solution"] = student_solution
spec.loader.exec_module(student_solution)

# Define test cases
class TestHackathonQuestion(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(student_solution.solve(2, 3), 5)  # Example function call

    def test_case_2(self):
        self.assertEqual(student_solution.solve(10, 15), 25)

    def test_case_3(self):
        self.assertEqual(student_solution.solve(-5, 5), 0)

if __name__ == "__main__":
    unittest.main()
