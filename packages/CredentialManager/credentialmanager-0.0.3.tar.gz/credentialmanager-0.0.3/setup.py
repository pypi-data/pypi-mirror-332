from setuptools import find_packages, setup


def main():

    with open('src/README.md', 'r') as file:
        long_description = file.read()

    setup(name='CredentialManager',
          version='0.0.3',
          url='https://github.com/windowstweeker/CredentialManager',
          author='windowstweeker',
          author_email='',
          description='Allows User to encrypt/decrypt credential information',
          long_description=long_description,
          long_description_content_type='text/markdown',
          package_dir={'': 'src'},
          packages=find_packages(where='src'),
          # entry_points={"console_scripts": ["command_name = PackageName:FunctionName",],},
          license='GNU GPLv3',
          classifiers=["Programming Language :: Python :: 3.12",
                       "Operating System :: OS Independent"],
          install_requires=["maskpass>=0.3.7", "pycryptodome>=3.21.0"],
          extras_require={'dev': ['setuptools>=75.8.2', 'twine>=4.0.2', 'wheel>=0.45.1'],},
          python_requires='>=3.12')


if __name__ == '__main__':
    main()
    # python setup.py sdist bdist_wheel
    # pip install dist/PackageName.whl
