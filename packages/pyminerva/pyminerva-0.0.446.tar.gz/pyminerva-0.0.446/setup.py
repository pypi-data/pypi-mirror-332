from setuptools import setup, find_packages
from os.path import abspath, dirname, join

# Fetches the content from README.md
# This will be used for the "long_description" field.
README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pyminerva',
    version='0.0.446',    # version.directory.file
    description='To get an insight from Financial Data Anlaysis',
    url='',
    author='Jeongmin Kang',
    author_email='jarvisNim@gmail.com',
    license='MIT',
    # packages=['minerv'],
    # install_requires=required(filename='requirements.txt'),
    include_package_data=True,
    # url="https://github.com/driscollis/arithmetic",
    packages=find_packages(exclude="tests"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=', '.join([
        'minerva', 'minerva-api', 'historical-data',
        'financial-data', 'stocks', 'funds', 'etfs',
        'indices', 'currency crosses', 'bonds', 'commodities',
        'crypto currencies'
    ]),
    project_urls={
        'Bug Reports': 'https://github.com/jarvisNim/minerva/issues',
        'Source': 'https://github.com/jarvisNim/minerva',
        'Documentation': 'https://miraelabs.com/'
    },
    python_requires='>=3.6',
)