import unittest
from src.CredentialManager import base_path as start_dir



def test_project(**kwargs):
    loader = unittest.TestLoader()
    suite = loader.discover(kwargs['test_directory'])
    runner = unittest.TextTestRunner()
    runner.run(suite)



if __name__ == '__main__':
    tests = [start_dir]
    for test in tests:
        test_project(test_directory=test)
