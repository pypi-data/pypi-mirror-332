from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name = 'hellojp',
    version = '0.0.1',
    description = 'Example PyPI package', 
    packages = find_packages(),
    author = 'JPBS',
    author_email = 'jbuusao@jgmail.com',
    install_requires = ['requests'],
    entry_points = {
        'console_scripts': [
            'hellojp = hellojp:hello'
        ]
    },
)
