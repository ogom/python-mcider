from setuptools import setup, find_packages
import os
import sys

def find_data_files(path):
    data_files = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            data_files.append((root, [os.path.join(root, filename)]))
    return data_files

def set_install_requires():
    install_requires = ['Markdown']
    if sys.version_info < (2, 7):
        install_requires.append('argparse')
    return install_requires

setup(
    name='mcider',
    version='0.1.0',
    description='to convert markdown into slideshow',
    license='Apache 2.0',
    url='http://ogom.github.com/python-mcider',
    download_url='https://github.com/ogom/python-mcider',
    author='ogom',
    author_email='ogom@hotmail.co.jp',
    include_package_data=True,
    packages=find_packages(),
    #data_files=find_data_files('themes'),
    install_requires=set_install_requires(),
    entry_points={
        'console_scripts': [
            'mcider = mcider.main:main',
        ],
    },
)
