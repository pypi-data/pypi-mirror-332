from setuptools import setup, find_packages

setup(
    name='mock_requests',
    version='2.0.0',
    packages=find_packages(),
    package_data={
        'mock_requests': ['data/*.json'],
    },
    include_package_data=True)
