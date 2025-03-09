import unittest
# from <path_to_file_being_tested> import <relevant_modules_for_test>


class TestName(unittest.TestCase):

    @classmethod
    # Set up class-level resources
    def setUpClass(cls):
        # Runs once before any tests are started
        # Create a database, or load test data into the production database to be used in the testing
        pass

    # Set up test-level resources
    def setUp(self):
        # Runs after setUpClass and before each test
        # Data needed for individual tests that needs to be the same for each test.  I.E. If put in the SetUpClass,
        #    and then it is altered in a test then it would not be the same for the next test.
        pass

    # Clean up test-level resources
    def tearDown(self):
        # Runs after each test, on final test it runs before tearDownClass
        # Alternatively, use tearDown to reset data or general clean up.  If something is created for a test in setUp
        #    and needs to be cleared for the next test if needed.
        pass

    @classmethod
    # Clean up class-level resources
    def tearDownClass(cls):
        # Runs after the last test is completed and the tearDown for the last test is completed.
        # If a test database was created, delete it or delete any test data entered into the production database
        pass

    def test_name_of_test1(self):
        # Setup Test scope here which will return a value to compare against an expected value.
        """
        I.E. if ww made a calc.py and have our own add function.  Then above from calc import add
        then for the test. test_value = calc.add(1, 1), expected_value = 2.
        the next test. test_value = calc.add(1, -1), expected_value = 0.
        the next test. test_value = calc.add(-1, -1), expected_value = -2.
        This would cover all the edge cases where it is most likely to fail.  In the future if you have a failure
        in the calc.add() function then add a case that would catch the error for the future so the same issue will
        not occur
        """
        test_value = 1
        expected_value = 1
        self.assertEqual(test_value, expected_value)
        pass

    def test_name_of_test2(self):
        # Setup Test here
        test_value = 2
        expected_value = 2
        self.assertEqual(test_value, expected_value)
        pass


if __name__ == '__main__':
    unittest.main()
