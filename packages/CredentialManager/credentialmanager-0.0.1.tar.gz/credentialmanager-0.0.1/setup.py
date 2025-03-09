from setuptools import find_packages, setup


def main():

    with open('Readme.md', 'r') as file:
        long_description = file.read()

    setup(name='CredentialManager',
          version='0.0.1',
          url='https://github.com/windowstweeker/CredentialManager',
          author='windowstweeker',
          author_email='',
          description='Allows User to encrypt/decrypt credential information',
          long_description=long_description,
          long_description_content_type='text/markdown',
          #package_dir={'': 'app'},
          #packages=find_packages(where='app'),
          packages=find_packages(),
          # entry_points={"console_scripts": ["command_name = PackageName:FunctionName",],},
          license='',
          classifiers=["Programming Language :: Python :: 3.12",
                       "Operating System :: OS Independent"],
          install_requires=["maskpass>=0.3.7", "pycryptodome>=3.21.0"],
          extras_require={'dev': ['twine>=4.0.2'],},
          #install_requires=["bson >= 0.5.10"],
          #extras_require={'dev': ['pytest>=7.0', 'twine>=4.0.2'],},
          python_requires='>=3.12')


if __name__ == '__main__':
    main()
    # python setup.py sdist bdist_wheel
    # pip install dist/PackageName.whl
