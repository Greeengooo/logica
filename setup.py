from setuptools import setup, find_packages

setup(
    name='logica',
    version='1.3.141',
    author='PolicyEngine team',
    author_email='',
    url='',
    description='logica',
    packages=find_packages(include=['common', 'compiler', 'parser_py', 'logica.py']),
    python_requires='>=3.6',
)