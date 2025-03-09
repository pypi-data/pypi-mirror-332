import os
from .main import CredentialManager


base_path = os.path.dirname(__file__)


def main():
    print(base_path)


if __name__ == '__main__':
    main()
